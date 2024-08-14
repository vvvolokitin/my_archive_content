from django.shortcuts import render
from django.views import generic

from content.models import Movie, Serial, Game, Book


class Home(generic.TemplateView):
    """Домашняя страница."""
    template_name = 'content/home.html'


def movie(request):
    """Страница фильмов."""

    template = 'content/content.html'
    object_list = Movie.objects.all()
    context = {
        'object_list': object_list
    }
    return render(request, template, context)


def serial(request):
    """Страница сериалов."""

    template = 'content/content.html'
    object_list = Serial.objects.all()
    context = {
        'object_list': object_list
    }
    return render(request, template, context)


def game(request):
    """Страница игр."""

    template = 'content/content.html'
    object_list = Game.objects.all()
    context = {
        'object_list': object_list
    }
    return render(request, template, context)


def book(request):
    """Страница книг."""

    template = 'content/content.html'
    object_list = Book.objects.all()
    context = {
        'object_list': object_list
    }
    return render(request, template, context)
