from django.urls import path

from content.views import (Home, book, book_create, book_delete, game,
                           game_create, game_delete, movie, movie_create,
                           movie_delete, serial, serial_create, serial_delete)


app_name = 'content'

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('movie/', movie, name='movie'),
    path('movie/create/', movie_create, name='movie_create'),
    path('movie/edit/<int:pk>/', movie_create, name='movie_edit'),
    path('movie/delete/<int:pk>/', movie_delete, name='movie_delete'),

    path('serial/', serial, name='serial'),
    path('serial/create/', serial_create, name='serial_create'),
    path('serial/edit/<int:pk>/', serial_create, name='serial_edit'),
    path('movie/delete/<int:pk>/', serial_delete, name='serial_delete'),

    path('game/', game, name='game'),
    path('game/create/', game_create, name='game_create'),
    path('game/edit/<int:pk>/', game_create, name='game_edit'),
    path('movie/delete/<int:pk>/', game_delete, name='game_delete'),


    path('book/', book, name='book'),
    path('book/create/', book_create, name='book_create'),
    path('book/edit/<int:pk>/', book_create, name='book_edit'),
    path('movie/delete/<int:pk>/', book_delete, name='book_delete'),
]
