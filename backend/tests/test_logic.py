from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse

from content.models import (
    Book,
    BookGenre,
    Game,
    GameGenre,
    Movie,
    MovieGenre,
    Serial,
    Status,
)


User = get_user_model()


class TestCreate(TestCase):
    """Проверка создания записей."""

    @classmethod
    def setUpTestData(cls):
        cls.author = User.objects.create(username='Автор записи')
        cls.author_client = Client()
        cls.author_client.force_login(cls.author)
        cls.status = Status.objects.create(status='архив')
        cls.movie_genre = MovieGenre.objects.create(name='тест', slug='test')
        cls.movie_data = {
            'title': 'новый фильм',
            'year': 2024,
            'description': 'новое описание',
            'genre_id': [cls.movie_genre.pk,],
            'status_id': cls.status.pk,
            'original_title': 'new_movie',
        }
        cls.serial_data = {
            'title': 'новый сериал',
            'year': 2024,
            'description': 'новое описание',
            'status': cls.status,
            'original_title': 'new_serial',
        }
        cls.book_data = {
            'title': 'новая книга',
            'year': 2024,
            'description': 'новое описание',
            'status': cls.status,
            'original_title': 'new_book',
            'author': 'новый автор'
        }
        cls.game_data = {
            'title': 'новая игра',
            'year': 2024,
            'description': 'новое описание',
            'status': cls.status,
        }

    def test_anonymous_user_cant_create_note(self):
        """Анонимный пользователь не может создать запись."""
        data = (
            ('content:movie_create', Movie, self.movie_data),
            ('content:serial_create', Serial, self.serial_data),
            ('content:book_create', Book, self.book_data),
            ('content:game_create', Game, self.game_data),
        )
        login_url = reverse('login')
        for url_name, model, form_data in data:
            with self.subTest(url_name=url_name, model=model):
                url = reverse(url_name)
                response = self.client.post(
                    url,
                    data=form_data
                )
                self.assertRedirects(
                    response,
                    f'{login_url}?next={url}'
                )
                self.assertEqual(
                    model.objects.count(),
                    0
                )


class TestDetailPage(TestCase):
    """Проверка отдельных страниц."""

    @classmethod
    def setUpTestData(cls):
        cls.author = User.objects.create(username='Автор записи')
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
        cls.movie_data = {
            'title': 'новый фильм',
            'year': 2024,
            'description': 'новое описание',
            'status': cls.status,
            'original_title': 'new_movie',
        }
        cls.serial = Serial.objects.create(
            title='сериал',
            year=2024,
            description='описание',
            status=cls.status,
            original_title='serial',
            user=cls.author
        )
        cls.serial.genre.set((cls.movie_genre,))
        cls.serial_data = {
            'title': 'новый сериал',
            'year': 2024,
            'description': 'новое описание',
            'status': cls.status,
            'original_title': 'new_serial',
        }
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
        cls.book_data = {
            'title': 'новая книга',
            'year': 2024,
            'description': 'новое описание',
            'status': cls.status,
            'original_title': 'new_book',
            'author': 'новый автор'
        }

        cls.game_genre = GameGenre.objects.create(name='тест', slug='test')
        cls.game = Game.objects.create(
            title='игра',
            year=2024,
            description='описание',
            status=cls.status,
            user=cls.author
        )
        cls.game.genre.set((cls.game_genre,))
        cls.game_data = {
            'title': 'новая игра',
            'year': 2024,
            'description': 'новое описание',
            'status': cls.status,
        }

    def test_anonymous_user_cant_create_note(self):
        """Анонимный пользователь не может создать запись."""
        data = (
            ('content:movie_create', Movie, self.movie_data),
            ('content:serial_create', Serial, self.serial_data),
            ('content:book_create', Book, self.book_data),
            ('content:game_create', Game, self.game_data),
        )
        login_url = reverse('login')
        for url_name, model, form_data in data:
            with self.subTest(url_name=url_name, model=model):
                url = reverse(url_name)
                response = self.client.post(
                    url,
                    data=form_data
                )
                self.assertRedirects(
                    response,
                    f'{login_url}?next={url}'
                )
                self.assertEqual(
                    model.objects.count(),
                    1
                )
