from django.contrib import admin

from content.models import Status, MovieGenre, Movie, Serial, Game, GameGenre, Book, BookGenre


admin.site.empty_value_display = 'Не задано'


class MovieInline(admin.TabularInline):
    model = Movie
    extra = 0


class SerailInline(admin.TabularInline):
    model = Serial
    extra = 0


class GameInline(admin.TabularInline):
    model = Game
    extra = 0


class BookInline(admin.TabularInline):
    model = Book
    extra = 0


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = (
        'status',
    )
    inlines = (
        MovieInline,
        SerailInline,
        GameInline,
        BookInline
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
    list_editable = (
        'status',
    )
    list_filter = (
        'year',
        'genre',
        'status',
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
    list_editable = (
        'status',
    )
    list_filter = (
        'year',
        'genre',
        'status',
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
    list_editable = (
        'status',
    )
    list_filter = (
        'year',
        'genre',
        'status',
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
    list_editable = (
        'status',
    )
    list_filter = (
        'year',
        'genre',
        'status',
    )
    filter_horizontal = ('genre',)
