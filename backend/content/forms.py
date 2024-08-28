from django import forms
from django.core.exceptions import ValidationError
from content.models import Movie, Serial, Book, Game


class BaseCreationForm(forms.ModelForm):
    """Базовая форма"""

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super().__init__(*args, **kwargs)

    def clean(self, ):
        cleaned_data = self.cleaned_data
        title = cleaned_data['title']
        year = cleaned_data['year']
        if Movie.objects.filter(title=title, year=year,).exists():
            raise ValidationError('Такая запись уже существует')
        return cleaned_data


class MovieCreationForm(BaseCreationForm):
    """Форма для создания записи о фильме."""

    class Meta:
        model = Movie
        fields = (
            'title',
            'original_title',
            'year',
            'description',
            'genre',
            'status'
        )


class MovieUpdateForm(forms.ModelForm):
    """Форма для обновления записи о фильме."""

    class Meta:
        model = Movie
        fields = (
            'title',
            'original_title',
            'year',
            'description',
            'genre',
        )


class MovieUpdateStatusForm(forms.ModelForm):
    """Форма для обновления статуса фильма."""

    class Meta:
        model = Movie
        fields = (
            'status',
        )


class SerialCreationForm(BaseCreationForm):
    """Форма для создания или обновления записи о сериале."""

    class Meta:
        model = Serial
        fields = (
            'title',
            'original_title',
            'year',
            'description',
            'genre',
            'status'
        )


class SerialUpdateForm(forms.ModelForm):
    """Форма для обновления записи о сериале."""

    class Meta:
        model = Serial
        fields = (
            'title',
            'original_title',
            'year',
            'description',
            'genre',
        )


class SerialUpdateStatusForm(forms.ModelForm):
    """Форма для обновления статуса сериала."""

    class Meta:
        model = Serial
        fields = (
            'status',
        )


class BookCreationForm(BaseCreationForm):
    """Форма для создания записи о книга."""

    class Meta:
        model = Book
        fields = (
            'title',
            'original_title',
            'author',
            'year',
            'description',
            'genre',
            'status'
        )


class BookUpdateForm(forms.ModelForm):
    """Форма для обновления записи о книга."""

    class Meta:
        model = Book
        fields = (
            'title',
            'original_title',
            'author',
            'year',
            'description',
            'genre',
        )


class BookUpdateStatusForm(forms.ModelForm):
    """Форма для обновления статуса книги."""

    class Meta:
        model = Book
        fields = (
            'status',
        )


class GameCreationForm(BaseCreationForm):
    """Форма для создания записи об игре."""

    class Meta:
        model = Game
        fields = (
            'title',
            'year',
            'description',
            'genre',
            'status'
        )


class GameUpdateForm(forms.ModelForm):
    """Форма для обновления записи об игре."""

    class Meta:
        model = Game
        fields = (
            'title',
            'year',
            'description',
            'genre',
        )


class GameUpdateStatusForm(forms.ModelForm):
    """Форма для обновления статуса игры."""

    class Meta:
        model = Game
        fields = (
            'status',
        )
