from http import HTTPStatus

from django.urls import reverse
import pytest
from pytest_django.asserts import assertRedirects

from content.models import Book, Game, Movie, Serial


@pytest.mark.parametrize(
    'url_name, success_url_name, model, content_pk',
    (
        (
            'content:movie_delete',
            'content:movie',
            Movie,
            pytest.lazy_fixture('movie_pk')
        ),
        (
            'content:serial_delete',
            'content:serial',
            Serial,
            pytest.lazy_fixture('serial_pk')
        ),
        (
            'content:book_delete',
            'content:book',
            Book,
            pytest.lazy_fixture('book_pk')
        ),
        (
            'content:game_delete',
            'content:game',
            Game,
            pytest.lazy_fixture('game_pk')
        ),
    )
)
def test_author_can_delete(author_client, url_name, success_url_name, model, content_pk):
    url = reverse(url_name, args=content_pk)
    response = author_client.post(url)
    assertRedirects(response, reverse(success_url_name))
    assert model.objects.count() == 0


@pytest.mark.parametrize(
    'url_name, model, content_pk',
    (
        (
            'content:movie_delete',
            Movie,
            pytest.lazy_fixture('movie_pk')
        ),
        (
            'content:serial_delete',
            Serial,
            pytest.lazy_fixture('serial_pk')
        ),
        (
            'content:book_delete',
            Book,
            pytest.lazy_fixture('book_pk')
        ),
        (
            'content:game_delete',
            Game,
            pytest.lazy_fixture('game_pk')
        ),
    )
)
def test_other_user_cant_delete(not_author_client, url_name, model, content_pk):
    url = reverse(url_name, args=content_pk)
    response = not_author_client.post(url)
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert model.objects.count() == 1
