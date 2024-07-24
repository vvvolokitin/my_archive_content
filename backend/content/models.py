from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class BaseGenreModel(models.Model):
    name = models.CharField(
        verbose_name='Название',
        max_length=250,
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
        verbose_name_plural = 'Жанры книг',


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


class Movie(models.Model):
    """Модель фильмов."""

    title = models.CharField(
        verbose_name='title',
        max_length=250,
    )
    original_title = models.CharField(
        verbose_name='Оригинальное название',
        max_length=250
    )
    year = models.PositiveSmallIntegerField(
        verbose_name='Год выхода',
    )
    description = models.TextField(
        verbose_name='Описание',
        blank=True
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
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'
        constraints = [
            models.UniqueConstraint(
                fields=['title', 'year', 'user'],
                name='unique_movie'
            )
        ]
