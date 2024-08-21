from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.core.paginator import Paginator

from content.models import Movie, Serial, Game, Book
from content.forms import MovieForm, SerialForm, BookForm, GameForm

from core.constants_content import COUNT_OBJ_ON_PAGE


class Home(generic.TemplateView):
    """Домашняя страница."""
    template_name = 'content/home.html'


def movie(request):
    """Страница фильмов."""

    movies = Movie.objects.select_related(
        'status'
    ).prefetch_related('genre')
    paginator = Paginator(movies, COUNT_OBJ_ON_PAGE)
    page_obj = paginator.get_page(request.GET.get('page'))
    context = {
        'page_obj': page_obj
    }
    return render(
        request,
        'content/content.html',
        context
    )


def movie_create(request, pk=None):
    if pk:
        instance = get_object_or_404(Movie, pk=pk)
    else:
        instance = None
    form = MovieForm(
        request.POST or None,
        instance=instance
    )
    context = {'form': form}
    if form.is_valid():
        new_form = form.save(commit=False)
        new_form.user = request.user
        new_form.save()
        return redirect('content:movie')
    return render(
        request,
        'content/form.html',
        context
    )


def movie_delete(request, pk):
    instance = get_object_or_404(Movie, pk=pk)
    context = {'note': instance}
    if request.method == 'POST':
        instance.delete()
        return redirect('content:movie')
    return render(
        request,
        'content/delete.html',
        context
    )


def serial(request):
    """Страница сериалов."""

    serials = Serial.objects.select_related(
        'status'
    ).prefetch_related('genre')
    paginator = Paginator(serials, COUNT_OBJ_ON_PAGE)
    page_obj = paginator.get_page(request.GET.get('page'))
    context = {
        'page_obj': page_obj
    }
    return render(
        request,
        'content/content.html',
        context
    )


def serial_create(request, pk=None):
    if pk:
        instance = get_object_or_404(Serial, pk=pk)
    else:
        instance = None
    form = SerialForm(
        request.POST or None,
        instance=instance
    )
    context = {'form': form}
    if form.is_valid():
        new_form = form.save(commit=False)
        new_form.user = request.user
        new_form.save()
        return redirect('content:serial')
    return render(
        request,
        'content/form.html',
        context
    )


def serial_delete(request, pk):
    instance = get_object_or_404(Serial, pk=pk)
    context = {'note': instance}
    if request.method == 'POST':
        instance.delete()
        return redirect('content:serial')
    return render(
        request,
        'content/delete.html',
        context
    )


def game(request):
    """Страница игр."""

    games = Game.objects.select_related(
        'status'
    ).prefetch_related('genre')
    paginator = Paginator(games, COUNT_OBJ_ON_PAGE)
    page_obj = paginator.get_page(request.GET.get('page'))
    context = {
        'page_obj': page_obj
    }
    return render(
        request,
        'content/content.html',
        context
    )


def game_create(request, pk=None):
    if pk:
        instance = get_object_or_404(Game, pk=pk)
    else:
        instance = None
    form = GameForm(
        request.POST or None,
        instance=instance
    )
    context = {'form': form}
    if form.is_valid():
        new_form = form.save(commit=False)
        new_form.user = request.user
        new_form.save()
        return redirect('content:game')
    return render(
        request,
        'content/form.html',
        context
    )


def game_delete(request, pk):
    instance = get_object_or_404(Game, pk=pk)
    context = {'note': instance}
    if request.method == 'POST':
        instance.delete()
        return redirect('content:game')
    return render(
        request,
        'content/delete.html',
        context
    )


def book(request):
    """Страница книг."""

    books = Book.objects.select_related(
        'status'
    ).prefetch_related('genre')
    paginator = Paginator(books, COUNT_OBJ_ON_PAGE)
    page_obj = paginator.get_page(request.GET.get('page'))
    context = {
        'page_obj': page_obj
    }
    return render(
        request,
        'content/content.html',
        context
    )


def book_create(request, pk=None):
    if pk:
        instance = get_object_or_404(Book, pk=pk)
    else:
        instance = None
    form = BookForm(
        request.POST or None,
        instance=instance
    )
    context = {'form': form}
    if form.is_valid():
        new_form = form.save(commit=False)
        new_form.user = request.user
        new_form.save()
        return redirect('content:book')
    return render(
        request,
        'content/form.html',
        context
    )


def book_delete(request, pk):
    instance = get_object_or_404(Book, pk=pk)
    context = {'note': instance}
    if request.method == 'POST':
        instance.delete()
        return redirect('content:book')
    return render(
        request,
        'content/delete.html',
        context
    )
