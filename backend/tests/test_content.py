from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from core.constants_content import COUNT_OBJ_ON_PAGE
from content.models import Movie, Serial, Book, Game, Status, BookGenre, MovieGenre, GameGenre
from content.forms import MovieCreationForm, SerialCreationForm, BookCreationForm, GameCreationForm


User = get_user_model()


class TestContentPages(TestCase):
    """Проверка страниц контента."""

    @classmethod
    def setUpTestData(cls):
        cls.author = User.objects.create(username='Автор записи')
        cls.status = cls.status = Status.objects.create(status='архив')

        Movie.objects.bulk_create(
            Movie(
                title=f'фильм {index}',
                year=2024,
                description='описание',
                status=cls.status,
                original_title='movie',
                user=cls.author
            ) for index in range(COUNT_OBJ_ON_PAGE+1)
        )

        Serial.objects.bulk_create(
            Serial(
                title=f'сериал {index}',
                year=2024,
                description='описание',
                status=cls.status,
                original_title='serial',
                user=cls.author
            ) for index in range(COUNT_OBJ_ON_PAGE+1)
        )

        Book.objects.bulk_create(
            Book(
                title=f'книга {index}',
                year=2024,
                description='описание',
                status=cls.status,
                original_title='book',
                author='автор',
                user=cls.author
            ) for index in range(COUNT_OBJ_ON_PAGE+1)
        )

        Game.objects.bulk_create(
            Game(
                title=f'игра {index}',
                year=2024,
                description='описание',
                status=cls.status,
                user=cls.author
            ) for index in range(COUNT_OBJ_ON_PAGE+1)
        )

    def test_objects_count(self):
        """Проверка количества записей на странице."""
        url_names = (
            'content:movie',
            'content:serial',
            'content:book',
            'content:game'
        )

        for url_name in url_names:
            self.client.force_login(self.author)
            with self.subTest(url_name=url_name):
                response = self.client.get(reverse(url_name))
                object_list = response.context.get('page_obj')
                self.assertEqual(len(object_list), COUNT_OBJ_ON_PAGE)


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

    def test_detail_page(self):
        """Проверка детальных страниц."""
        data = (
            ('movie', 'content:movie_detail', self.movie.pk),
            ('serial', 'content:serial_detail', self.serial.pk),
            ('book', 'content:book_detail', self.book.pk),
            ('game', 'content:game_detail', self.game.pk),
        )
        for object_name, url_name, pk in data:
            self.client.force_login(self.author)
            with self.subTest(object_name=object_name, url_name=url_name):
                response = self.client.get(reverse(url_name, args=(pk,)))
                self.assertIn(object_name, response.context)

    def test_authenticated_client_has_form(self):
        """Проверка наличия формы у аутенитфицированного пользователя."""
        data = (
            ('content:movie_create', MovieCreationForm),
            ('content:serial_create', SerialCreationForm),
            ('content:book_create', BookCreationForm),
            ('content:game_create', GameCreationForm),
        )

        for url_name, form in data:
            self.client.force_login(self.author)
            with self.subTest(url_name=url_name, form=form):
                response = self.client.get(reverse(url_name))
                self.assertIn('form', response.context)
                self.assertIsInstance(response.context.get('form'), form)
