from django.urls import path

from content.views import (Home, MovieListView, MovieDetailView, MovieCreateView, MovieUpdateView, MovieDeleteView, BookCreateView,  BookDetailView, BookDeleteView, BookListView, BookUpdateView,
                           GameCreateView, GameDeleteView, GameDetailView, GameListView, GameUpdateView, SerialCreateView,  SerialDetailView, SerialListView, SerialDeleteView, SerialUpdateView)


app_name = 'content'

urlpatterns = [
    path('', Home.as_view(), name='home'),

    path('movie/', MovieListView.as_view(), name='movie'),
    path('movie/<int:pk>', MovieDetailView.as_view(), name='movie_detail'),
    path('movie/create/', MovieCreateView.as_view(), name='movie_create'),
    path('movie/edit/<int:pk>/', MovieUpdateView.as_view(), name='movie_edit'),
    path('movie/delete/<int:pk>/', MovieDeleteView.as_view(), name='movie_delete'),

    path('serial/', SerialListView.as_view(), name='serial'),
    path('serial/<int:pk>', SerialDetailView.as_view(), name='serial_detail'),
    path('serial/create/', SerialCreateView.as_view(), name='serial_create'),
    path('serial/edit/<int:pk>/', SerialUpdateView.as_view(), name='serial_edit'),
    path('serial/delete/<int:pk>/',
         SerialDeleteView.as_view(), name='serial_delete'),

    path('game/', GameListView.as_view(), name='game'),
    path('game/<int:pk>', GameDetailView.as_view(), name='game_detail'),
    path('game/create/', GameCreateView.as_view(), name='game_create'),
    path('game/edit/<int:pk>/', GameUpdateView.as_view(), name='game_edit'),
    path('game/delete/<int:pk>/', GameDeleteView.as_view(), name='game_delete'),


    path('book/', BookListView.as_view(), name='book'),
    path('book/<int:pk>', BookDetailView.as_view(), name='book_detail'),
    path('book/create/', BookCreateView.as_view(), name='book_create'),
    path('book/edit/<int:pk>/', BookUpdateView.as_view(), name='book_edit'),
    path('book/delete/<int:pk>/', BookDeleteView.as_view(), name='book_delete'),
]
