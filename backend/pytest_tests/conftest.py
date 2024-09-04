import pytest

from django.test.client import Client

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


@pytest.fixture
def author(django_user_model):
    return django_user_model.objects.create(username='Автор')


@pytest.fixture
def not_author(django_user_model):
    return django_user_model.objects.create(username='Не автор')


@pytest.fixture
def author_client(author):
    client = Client()
    client.force_login(author)
    return client


@pytest.fixture
def not_author_client(not_author):
    client = Client()
    client.force_login(not_author)
    return client


@pytest.fixture
def status():
    return Status.objects.create(status='архив')


@pytest.fixture
def movie_genre():
    return MovieGenre.objects.create(
        name='Тест',
        slug='test'
    )


@pytest.fixture
def movie(author, movie_genre, status):
    movie = Movie.objects.create(
        title='фильм',
        year=2024,
        description='описание',
        status=status,
        original_title='movie',
        user=author
    )
    movie.genre.set((movie_genre,))
    return movie


@pytest.fixture
def movie_pk(movie):
    return (movie.pk,)


@pytest.fixture
def serial(author, movie_genre, status):
    serial = Serial.objects.create(
        title='сериал',
        year=2024,
        description='описание',
        status=status,
        original_title='serial',
        user=author
    )
    serial.genre.set((movie_genre,))
    return serial


@pytest.fixture
def serial_pk(serial):
    return (serial.pk,)


@pytest.fixture
def book_genre():
    return BookGenre.objects.create(
        name='тест',
        slug='test'
    )


@pytest.fixture
def book(author, book_genre, status):
    book = Book.objects.create(
        title='книга',
        year=2024,
        description='описание',
        status=status,
        original_title='book',
        author='автор',
        user=author
    )
    book.genre.set((book_genre,))
    return book


@pytest.fixture
def book_pk(book):
    return (book.pk,)


@pytest.fixture
def game_genre():
    return GameGenre.objects.create(
        name='тест',
        slug='test'
    )


@pytest.fixture
def game(author, game_genre, status):
    game = Game.objects.create(
        title='игра',
        year=2024,
        description='описание',
        status=status,
        user=author
    )
    game.genre.set((game_genre,))
    return game


@pytest.fixture
def game_pk(game):
    return (game.pk,)
