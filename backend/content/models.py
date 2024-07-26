from django.db import models
from django.contrib.auth import get_user_model

from core.constants_content import LENGTH_NAME_TITLE


User = get_user_model()


class BaseGenreModel(models.Model):
    name = models.CharField(
        verbose_name='Название',
        max_length=LENGTH_NAME_TITLE,
        unique=True,
    )
    slug = models.SlugField(
        verbose_name='Слаг',
        unique=True,
        help_text=(
            'Идентификатор для слага; '
            'разрешены символы латиницы, цифры, дефис и подчёркивание.'
        )
    )

    class Meta:
        ordering = ('name')
        abstract = True

    def __str__(self) -> str:
        return self.name


class MovieGenre(BaseGenreModel):
    """Модель жанров фильмов/сериалов."""

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class GameGenre(BaseGenreModel):
    """Модель жанров игр."""

    class Meta:
        verbose_name = 'Жанр игры'
        verbose_name_plural = 'Жанры игр'


class BookGenre(BaseGenreModel):
    """Модель жанров книг."""

    class Meta:
        verbose_name = 'Жанр книги'
        verbose_name_plural = 'Жанры книг'


class Status(models.Model):
    """Модель статуса."""

    status = models.CharField(
        verbose_name='Статус',
        max_length=50
    )

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'

    def __str__(self) -> str:
        return self.status


class BaseContentModel(models.Model):
    """Базовая модель для контента."""

    title = models.CharField(
        verbose_name='Название',
        max_length=LENGTH_NAME_TITLE
    )
    year = models.PositiveSmallIntegerField(
        verbose_name='Год выхода'
    )
    description = models.TextField(
        verbose_name='Описание',
        blank=True
    )
    pub_date = models.DateTimeField(
        verbose_name='Дата добавления',
        auto_now_add=True,
        db_index=True
    )
    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT
    )

    class Meta:
        ordering = ('pub_date')
        abstract = True


class Movie(BaseContentModel):
    """Модель фильмов."""

    original_title = models.CharField(
        verbose_name='Оригинальное название',
        max_length=LENGTH_NAME_TITLE
    )
    genre = models.ManyToManyField(
        MovieGenre,
        related_name='movies'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        related_name='movies'
    )

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'
        constraints = [
            models.UniqueConstraint(
                fields=['title', 'year', 'user'],
                name='unique_movie'
            )
        ]


class Serial(BaseContentModel):
    """Модель сериалов."""

    original_title = models.CharField(
        verbose_name='Оригинальное название',
        max_length=LENGTH_NAME_TITLE
    )
    genre = models.ManyToManyField(
        MovieGenre,
        related_name='serials'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        related_name='serials'
    )

    class Meta:
        verbose_name = 'Сериал'
        verbose_name_plural = 'Сериалы'
        constraints = [
            models.UniqueConstraint(
                fields=['title', 'year', 'user'],
                name='unique_serial'
            )
        ]


class Game(BaseContentModel):
    """Модель игр."""

    genre = models.ManyToManyField(
        GameGenre,
        related_name='games'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        related_name='games'
    )

    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'
        constraints = [
            models.UniqueConstraint(
                fields=['title', 'year', 'user'],
                name='unique_game'
            )
        ]


class Book(BaseContentModel):
    """Модель книг."""

    original_title = models.CharField(
        verbose_name='Оригинальное название',
        max_length=LENGTH_NAME_TITLE
    )
    author = models.CharField(
        verbose_name='Автор',
        max_length=250
    )
    genre = models.ManyToManyField(
        BookGenre,
        related_name='books'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        related_name='books'
    )

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        constraints = [
            models.UniqueConstraint(
                fields=['title', 'year', 'user'],
                name='unique_book'
            )
        ]
