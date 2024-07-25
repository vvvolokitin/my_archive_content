from django.contrib import admin

from content.models import Status, MovieGenre, Movie, Serial


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = (
        'status',
    )


@admin.register(MovieGenre)
class MovieGenre(admin.ModelAdmin):
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
