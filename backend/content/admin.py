from django.contrib import admin

from content.models import Status, MovieGenre, Movie, Serial, Game, GameGenre, Book, BookGenre


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = (
        'status',
    )


@admin.register(MovieGenre)
class MovieGenreAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'slug'
    )


@admin.register(GameGenre)
class GameGenreAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'slug'
    )


@admin.register(BookGenre)
class BookGenreAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'slug'
    )


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'original_title',
        'year',
        'status'
    )
    search_fields = (
        'title',
        'original_title',
        'genre'
    )
    filter_horizontal = ('genre',)


@admin.register(Serial)
class SerialAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'original_title',
        'year',
        'status'
    )
    search_fields = (
        'title',
        'original_title',
        'genre'
    )
    filter_horizontal = ('genre',)


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'year',
        'status'
    )
    search_fields = (
        'title',
        'genre'
    )
    filter_horizontal = ('genre',)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'year',
        'author',
        'status'
    )
    search_fields = (
        'title',
        'genre'
    )
    filter_horizontal = ('genre',)
