from django import forms

from content.models import Movie, Serial, Book, Game


class MovieForm(forms.ModelForm):
    """Форма для создания или обновления записи о фильме."""

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


class SerialForm(forms.ModelForm):
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


class BookForm(forms.ModelForm):
    """Форма для создания или обновления записи о книга."""

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


class GameForm(forms.ModelForm):
    """Форма для создания или обновления записи о сериале."""

    class Meta:
        model = Game
        fields = (
            'title',
            'year',
            'description',
            'genre',
            'status'
        )
