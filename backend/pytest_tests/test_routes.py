from http import HTTPStatus

from django.urls import reverse
from pytest_django.asserts import assertRedirects
import pytest


@pytest.mark.parametrize(
    'url_name',
    ('content:home', 'login', 'registration', 'password_reset')
)
def test_pages_availability_for_anonymous(client, url_name):
    """Проверка доступности страниц для анонимного пользователя."""
    url = reverse(url_name)
    response = client.get(url)
    assert response.status_code == HTTPStatus.OK


@pytest.mark.parametrize(
    'url_name',
    (
        'content:movie',
        'content:movie_create',
        'content:book',
        'content:book_create',
        'content:serial',
        'content:serial_create',
        'content:game',
        'content:game_create',
        'password_reset'
    )
)
def test_availability_for_authenticated_client(not_author_client, url_name):
    """Проверка доступности страниц для аутентифицированного пользователя."""
    url = reverse(url_name)
    response = not_author_client.get(url)
    assert response.status_code == HTTPStatus.OK


@pytest.mark.parametrize(
    'parametrized_client, expected_status',
    (
        (pytest.lazy_fixture('not_author_client'), HTTPStatus.NOT_FOUND),
        (pytest.lazy_fixture('author_client'), HTTPStatus.OK)
    ),
)
@pytest.mark.parametrize(
    'url_name, content_pk',
    (
        ('content:movie_detail', pytest.lazy_fixture('movie_pk')),
        ('content:movie_edit', pytest.lazy_fixture('movie_pk')),
        ('content:movie_delete', pytest.lazy_fixture('movie_pk')),

        ('content:serial_detail', pytest.lazy_fixture('serial_pk')),
        ('content:serial_edit', pytest.lazy_fixture('serial_pk')),
        ('content:serial_delete', pytest.lazy_fixture('serial_pk')),

        ('content:book_detail', pytest.lazy_fixture('book_pk')),
        ('content:book_edit', pytest.lazy_fixture('book_pk')),
        ('content:book_delete', pytest.lazy_fixture('book_pk')),

        ('content:game_detail', pytest.lazy_fixture('game_pk')),
        ('content:game_edit', pytest.lazy_fixture('game_pk')),
        ('content:game_delete', pytest.lazy_fixture('game_pk')),
    )
)
def test_availability_detail_edit_and_delete(
    parametrized_client, url_name, content_pk, expected_status
):
    """Проверка доступности к записям, редактированию и удалению."""
    url = reverse(url_name, args=content_pk)
    response = parametrized_client.get(url)
    assert response.status_code == expected_status


@pytest.mark.parametrize(
    'url_name, content_pk',
    (
        ('content:movie', None),
        ('content:movie_create', None),
        ('content:movie_detail', pytest.lazy_fixture('movie_pk')),
        ('content:movie_edit', pytest.lazy_fixture('movie_pk')),
        ('content:movie_delete', pytest.lazy_fixture('movie_pk')),

        ('content:book', None),
        ('content:book_create', None),
        ('content:book_detail', pytest.lazy_fixture('book_pk')),
        ('content:book_edit', pytest.lazy_fixture('book_pk')),
        ('content:book_delete', pytest.lazy_fixture('book_pk')),

        ('content:serial', None),
        ('content:serial_create', None),
        ('content:serial_detail', pytest.lazy_fixture('serial_pk')),
        ('content:serial_edit', pytest.lazy_fixture('serial_pk')),
        ('content:serial_delete', pytest.lazy_fixture('serial_pk')),

        ('content:game', None),
        ('content:game_create', None),
        ('content:game_detail', pytest.lazy_fixture('game_pk')),
        ('content:game_edit', pytest.lazy_fixture('game_pk')),
        ('content:game_delete', pytest.lazy_fixture('game_pk')),
    )
)
def test_redirect_for_anonymous_client(client, url_name, content_pk):
    """Провекра редиректа для анонимного пользователя."""
    login_url = reverse('login')
    url = reverse(url_name, args=content_pk)
    expected_url = f'{login_url}?next={url}'
    response = client.get(url)
    assertRedirects(response, expected_url)
