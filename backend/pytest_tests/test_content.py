from django.urls import reverse
import pytest

from core.constants_content import COUNT_OBJ_ON_PAGE
from content.forms import (
    BookCreationForm,
    BookUpdateForm,
    BookUpdateStatusForm,
    GameCreationForm,
    GameUpdateForm,
    GameUpdateStatusForm,
    MovieCreationForm,
    MovieUpdateForm,
    MovieUpdateStatusForm,
    SerialCreationForm,
    SerialUpdateForm,
    SerialUpdateStatusForm
)


@pytest.mark.parametrize(
    'url_name, content',
    (
        ('content:movie', pytest.lazy_fixture('movies')),
        ('content:serial', pytest.lazy_fixture('serials')),
        ('content:book', pytest.lazy_fixture('books')),
        ('content:game', pytest.lazy_fixture('games')),
    )
)
def test_objects_count(author_client, url_name, content):
    """Проверка количества записей на странице."""
    response = author_client.get(reverse(url_name))
    object_list = response.context.get('page_obj')
    assert len(object_list) == COUNT_OBJ_ON_PAGE


@pytest.mark.parametrize(
    'parametrized_client, object_in_list',
    (
        (pytest.lazy_fixture('author_client'), True),
        (pytest.lazy_fixture('not_author_client'), False),
    )
)
@pytest.mark.parametrize(
    'url_name, content',
    (
        ('content:movie', pytest.lazy_fixture('movie')),
        ('content:serial', pytest.lazy_fixture('serial')),
        ('content:book', pytest.lazy_fixture('book')),
        ('content:game', pytest.lazy_fixture('game')),
    )
)
def test_bject_list_for_different_users(
    parametrized_client, object_in_list, url_name, content
):
    """Проверка наличия записей на странице для разных пользователей."""
    response = parametrized_client.get(reverse(url_name))
    object_list = response.context.get('page_obj')
    assert (content in object_list) is object_in_list


@pytest.mark.parametrize(
    'content_name, url_name, content_pk',
    (
        (
            'movie',
            'content:movie_detail',
            pytest.lazy_fixture('movie_pk')
        ),
        (
            'serial',
            'content:serial_detail',
            pytest.lazy_fixture('serial_pk')
        ),
        (
            'book',
            'content:book_detail',
            pytest.lazy_fixture('book_pk')
        ),
        (
            'game',
            'content:game_detail',
            pytest.lazy_fixture('game_pk')
        ),
    )
)
def test_detail_page(author_client, content_name, url_name, content_pk):
    """Проверка детальных страниц."""
    response = author_client.get(reverse(url_name, args=content_pk))
    assert content_name in response.context


@pytest.mark.parametrize(
    'url_name, form, content_pk',
    (
        ('content:movie_create', MovieCreationForm, None),
        ('content:movie_edit', MovieUpdateForm, pytest.lazy_fixture('movie_pk')),
        ('content:movie_edit_status', MovieUpdateStatusForm,
         pytest.lazy_fixture('movie_pk')),

        ('content:serial_create', SerialCreationForm, None),
        ('content:serial_edit', SerialUpdateForm, pytest.lazy_fixture('serial_pk')),
        ('content:serial_edit_status', SerialUpdateStatusForm,
         pytest.lazy_fixture('serial_pk')),

        ('content:book_create', BookCreationForm, None),
        ('content:book_edit', BookUpdateForm, pytest.lazy_fixture('book_pk')),
        ('content:book_edit_status', BookUpdateStatusForm,
         pytest.lazy_fixture('book_pk')),

        ('content:game_create', GameCreationForm, None),
        ('content:game_edit', GameUpdateForm, pytest.lazy_fixture('game_pk')),
        ('content:game_edit_status', GameUpdateStatusForm,
         pytest.lazy_fixture('game_pk')),
    )
)
def test_authenticated_client_has_form(author_client, url_name, form, content_pk):
    """Проверка наличия формы у аутентифицированного пользователя."""
    response = author_client.get(reverse(url_name, args=content_pk))
    assert 'form' in response.context
    assert isinstance(response.context.get('form'), form)
