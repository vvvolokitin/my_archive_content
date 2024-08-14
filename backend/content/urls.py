from django.urls import path

from content.views import Home, movie, game, serial, book

app_name = 'content'

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('movie/', movie, name='movie'),
    path('serial/', serial, name='serial'),
    path('game/', game, name='game'),
    path('book/', book, name='book'),
]
