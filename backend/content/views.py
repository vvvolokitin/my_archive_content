from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic

from content.models import Movie, Serial, Game, Book
from content.forms import MovieForm, SerialForm, BookForm, GameForm


class Home(generic.TemplateView):
    """Домашняя страница."""
    template_name = 'content/home.html'


def movie(request):
    """Страница фильмов."""

    template = 'content/content.html'
    object_list = Movie.objects.select_related(
        'status'
    ).prefetch_related('genre')
    context = {
        'object_list': object_list
    }
    return render(request, template, context)


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

    template = 'content/content.html'
    object_list = Serial.objects.select_related(
        'status'
    ).prefetch_related('genre')
    context = {
        'object_list': object_list
    }
    return render(request, template, context)


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

    template = 'content/content.html'
    object_list = Game.objects.select_related(
        'status'
    ).prefetch_related('genre')
    context = {
        'object_list': object_list
    }
    return render(request, template, context)


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

    template = 'content/content.html'
    object_list = Book.objects.select_related(
        'status'
    ).prefetch_related('genre')
    context = {
        'object_list': object_list
    }
    return render(request, template, context)


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
