from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from content.models import Movie, Serial, Book, Game, Status, BookGenre, MovieGenre, GameGenre


User = get_user_model()



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
