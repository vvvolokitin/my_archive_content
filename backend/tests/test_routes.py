from http import HTTPStatus

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from content.models import (
    Book,
    BookGenre,
    Game,
    GameGenre,
    Movie,
    MovieGenre,
    Serial,
    Status
)

User = get_user_model()


class TestRoute(TestCase):
    """Проверка путей."""

    @classmethod
    def setUpTestData(cls):
        cls.author = User.objects.create(username='Автор записи')
        cls.not_author = User.objects.create(username='Не автор записи')
        cls.status = Status.objects.create(status='архив')
        cls.movie_genre = MovieGenre.objects.create(name='тест', slug='test')
        cls.movie = Movie.objects.create(
            title='фильм',
            year=2024,
            description='описание',
            status=cls.status,
            original_title='movie',
            user=cls.author
        )
        cls.movie.genre.set((cls.movie_genre,))
        cls.serial = Serial.objects.create(
            title='сериал',
            year=2024,
            description='описание',
            status=cls.status,
            original_title='serial',
            user=cls.author
        )
        cls.serial.genre.set((cls.movie_genre,))

        cls.book_genre = BookGenre.objects.create(name='тест', slug='test')
        cls.book = Book.objects.create(
            title='книга',
            year=2024,
            description='описание',
            status=cls.status,
            original_title='book',
            author='автор',
            user=cls.author
        )
        cls.book.genre.set((cls.book_genre,))

        cls.game_genre = GameGenre.objects.create(name='тест', slug='test')
        cls.game = Game.objects.create(
            title='игра',
            year=2024,
            description='описание',
            status=cls.status,
            user=cls.author
        )
        cls.game.genre.set((cls.game_genre,))

    def test_pages_availability_for_anonymous(self):
        """Проверка доступности страниц для анонимного пользователя."""
        url_names = (
            'content:home',
            'login',
            'registration',
            'password_reset'
        )

        for url_name in url_names:
            with self.subTest(url_name=url_name):
                response = self.client.get(reverse(url_name))
                self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_availability_for_authenticated_client(self):
        """Проверка доступности страниц для аутентифицированного пользователя."""
        url_names = (
            ('content:movie'),
            ('content:movie_create'),
            ('content:book'),
            ('content:book_create'),
            ('content:serial'),
            ('content:serial_create'),
            ('content:game'),
            ('content:game_create'),
            ('password_reset'),
        )
        for url_name in url_names:
            self.client.force_login(self.author)
            with self.subTest(url_name=url_name):
                response = self.client.get(reverse(url_name))
                self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_availability_detail_edit_and_delete(self):
        """Проверка доступности к записям, редактированию и удалению."""
        data = (
            ('content:movie_detail', self.author, HTTPStatus.OK, self.movie.pk),
            ('content:movie_detail', self.not_author,
             HTTPStatus.NOT_FOUND, self.movie.pk),
            ('content:movie_edit', self.author, HTTPStatus.OK, self.movie.pk),
            ('content:movie_edit', self.not_author,
             HTTPStatus.NOT_FOUND, self.movie.pk),
            ('content:movie_delete', self.author, HTTPStatus.OK, self.movie.pk),
            ('content:movie_delete', self.not_author,
             HTTPStatus.NOT_FOUND, self.movie.pk),

            ('content:serial_detail', self.author, HTTPStatus.OK, self.serial.pk),
            ('content:serial_detail', self.not_author,
             HTTPStatus.NOT_FOUND, self.serial.pk),
            ('content:serial_edit', self.author, HTTPStatus.OK, self.serial.pk),
            ('content:serial_edit', self.not_author,
             HTTPStatus.NOT_FOUND, self.serial.pk),
            ('content:serial_delete', self.author, HTTPStatus.OK, self.serial.pk),
            ('content:serial_delete', self.not_author,
             HTTPStatus.NOT_FOUND, self.serial.pk),

            ('content:book_detail', self.author, HTTPStatus.OK, self.book.pk),
            ('content:book_detail', self.not_author,
             HTTPStatus.NOT_FOUND, self.book.pk),
            ('content:book_edit', self.author, HTTPStatus.OK, self.book.pk),
            ('content:book_edit', self.not_author,
             HTTPStatus.NOT_FOUND, self.book.pk),
            ('content:book_delete', self.author, HTTPStatus.OK, self.book.pk),
            ('content:book_delete', self.not_author,
             HTTPStatus.NOT_FOUND, self.book.pk),

            ('content:game_detail', self.author, HTTPStatus.OK, self.game.pk),
            ('content:game_detail', self.not_author,
             HTTPStatus.NOT_FOUND, self.game.pk),
            ('content:game_edit', self.author, HTTPStatus.OK, self.game.pk),
            ('content:game_edit', self.not_author,
             HTTPStatus.NOT_FOUND, self.game.pk),
            ('content:game_delete', self.author, HTTPStatus.OK, self.game.pk),
            ('content:game_delete', self.not_author,
             HTTPStatus.NOT_FOUND, self.game.pk),

        )
        for url_name, user, status, pk in data:
            self.client.force_login(user)
            with self.subTest(user=user, url_name=url_name):
                response = self.client.get(reverse(url_name, args=(pk,)))
                self.assertEqual(response.status_code, status)

    def test_redirect_for_anonymous_client(self):
        """Провекра редиректа для анонимного пользователя."""
        login_url = reverse('login')
        data = (
            ('content:movie', None),
            ('content:movie_create', None),
            ('content:movie_detail', self.movie.pk),
            ('content:movie_edit', self.movie.pk),
            ('content:movie_delete', self.movie.pk),

            ('content:book', None),
            ('content:book_create', None),
            ('content:book_detail', self.book.pk),
            ('content:book_edit', self.book.pk),
            ('content:book_delete', self.book.pk),

            ('content:serial', None),
            ('content:serial_create', None),
            ('content:serial_detail', self.serial.pk),
            ('content:serial_edit', self.serial.pk),
            ('content:serial_delete', self.serial.pk),

            ('content:game', None),
            ('content:game_create', None),
            ('content:game_detail', self.game.pk),
            ('content:game_edit', self.game.pk),
            ('content:game_delete', self.game.pk),
        )

        for url_name, pk in data:
            with self.subTest(url_name=url_name):
                url = reverse(url_name, args=(pk,) if pk else None)
                redirect_url = f'{login_url}?next={url}'
                response = self.client.get(url)
                self.assertRedirects(response, redirect_url)
