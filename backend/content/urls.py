from django.urls import path

from content.views import (BookCreateView, BookDeleteView, BookDetailView,
                           BookListView, BookStatusUpdateView, BookUpdateView,
                           GameCreateView, GameDeleteView, GameDetailView,
                           GameListView, GameStatusUpdateView, GameUpdateView,
                           Home, MovieCreateView, MovieDeleteView,
                           MovieDetailView, MovieListView,
                           MovieStatusUpdateView, MovieUpdateView,
                           SerialCreateView, SerialDeleteView,
                           SerialDetailView, SerialListView,
                           SerialStatusUpdateView, SerialUpdateView)

app_name = 'content'

urlpatterns = [
    path('', Home.as_view(), name='home'),

    path('movie/', MovieListView.as_view(), name='movie'),
    path('movie/<int:pk>', MovieDetailView.as_view(), name='movie_detail'),
    path('movie/create/', MovieCreateView.as_view(), name='movie_create'),
    path('movie/edit/<int:pk>/', MovieUpdateView.as_view(), name='movie_edit'),
    path('movie/edit_status/<int:pk>/', MovieStatusUpdateView.as_view(), name='movie_edit_status'),
    path('movie/delete/<int:pk>/', MovieDeleteView.as_view(), name='movie_delete'),

    path('serial/', SerialListView.as_view(), name='serial'),
    path('serial/<int:pk>', SerialDetailView.as_view(), name='serial_detail'),
    path('serial/create/', SerialCreateView.as_view(), name='serial_create'),
    path('serial/edit/<int:pk>/', SerialUpdateView.as_view(), name='serial_edit'),
    path('serial/edit_status/<int:pk>/', SerialStatusUpdateView.as_view(), name='serial_edit_status'),
    path('serial/delete/<int:pk>/',
         SerialDeleteView.as_view(), name='serial_delete'),

    path('game/', GameListView.as_view(), name='game'),
    path('game/<int:pk>', GameDetailView.as_view(), name='game_detail'),
    path('game/create/', GameCreateView.as_view(), name='game_create'),
    path('game/edit/<int:pk>/', GameUpdateView.as_view(), name='game_edit'),
    path('game/edit_status/<int:pk>/', GameStatusUpdateView.as_view(), name='game_edit_status'),
    path('game/delete/<int:pk>/', GameDeleteView.as_view(), name='game_delete'),


    path('book/', BookListView.as_view(), name='book'),
    path('book/<int:pk>', BookDetailView.as_view(), name='book_detail'),
    path('book/create/', BookCreateView.as_view(), name='book_create'),
    path('book/edit/<int:pk>/', BookUpdateView.as_view(), name='book_edit'),
    path('book/edit_status/<int:pk>/', BookStatusUpdateView.as_view(), name='book_edit_status'),
    path('book/delete/<int:pk>/', BookDeleteView.as_view(), name='book_delete'),
]
