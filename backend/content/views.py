from django.views import generic
from django.views.generic import ListView, UpdateView, DeleteView, CreateView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from content.models import Movie, Serial, Game, Book
from content.forms import MovieForm, SerialForm, BookForm, GameForm
from core.constants_content import COUNT_OBJ_ON_PAGE


class Home(generic.TemplateView):
    """Домашняя страница."""
    template_name = 'content/home.html'


class BaseView(LoginRequiredMixin):
    """Базовый класс для CBV."""

    def get_queryset(self):
        return self.model.objects.select_related(
            'status'
        ).prefetch_related('genre').filter(user=self.request.user)


class CreateBaseView(CreateView):
    """Базоваый класс создания для CBV."""

    def form_valid(self, form):
        new_form = form.save(commit=False)
        new_form.user = self.request.user
        new_form.save()
        return super().form_valid(form)


class MovieListView(BaseView, ListView):
    """Список фильмов."""

    model = Movie
    paginate_by = COUNT_OBJ_ON_PAGE
    template_name = 'content/content.html'


class MovieDetailView(BaseView, DetailView):
    """Запись о фильме."""

    model = Movie
    template_name = 'content/detail.html'


class MovieCreateView(BaseView, CreateBaseView):
    """Cоздание записи о фильме."""

    model = Movie
    form_class = MovieForm
    template_name = 'content/form.html'


class MovieUpdateView(BaseView, UpdateView):
    """Редактирование записи о фильме."""

    model = Movie
    form_class = MovieForm
    template_name = 'content/form.html'


class MovieDeleteView(BaseView, DeleteView):
    """Удаление записи о фильме."""

    model = Movie
    template_name = 'content/delete.html'
    success_url = reverse_lazy('content:movie')


class SerialListView(BaseView, ListView):
    """Список сериалов."""

    model = Serial
    paginate_by = COUNT_OBJ_ON_PAGE
    template_name = 'content/content.html'


class SerialDetailView(BaseView, DetailView):
    """Запись о сериале."""

    model = Serial
    template_name = 'content/detail.html'


class SerialCreateView(BaseView, CreateBaseView):
    """Cоздание записи о сериале."""

    model = Serial
    form_class = SerialForm
    template_name = 'content/form.html'
    success_url = reverse_lazy('content:serial')


class SerialUpdateView(BaseView, UpdateView):
    """Редактирование записи о сериале."""

    model = Serial
    form_class = SerialForm
    template_name = 'content/form.html'
    success_url = reverse_lazy('content:serial')


class SerialDeleteView(BaseView, DeleteView):
    """Удаление записи о сериале."""

    model = Serial
    template_name = 'content/delete.html'
    success_url = reverse_lazy('content:serial')


class GameListView(BaseView, ListView):
    """Список игр."""

    model = Game
    paginate_by = COUNT_OBJ_ON_PAGE
    template_name = 'content/content.html'


class GameDetailView(BaseView, DetailView):
    """Запись о игре."""

    model = Game
    template_name = 'content/detail.html'


class GameCreateView(BaseView, CreateBaseView):
    """Cоздание записи о игре."""

    model = Game
    form_class = GameForm
    template_name = 'content/form.html'
    success_url = reverse_lazy('content:game')


class GameUpdateView(BaseView, UpdateView):
    """Редактирование записи о сериале."""

    model = Game
    form_class = GameForm
    template_name = 'content/form.html'
    success_url = reverse_lazy('content:game')


class GameDeleteView(BaseView, DeleteView):
    """Удаление записи о сериале."""

    model = Game
    template_name = 'content/delete.html'
    success_url = reverse_lazy('content:game')


class BookListView(BaseView, ListView):
    """Список книг."""

    model = Book
    paginate_by = COUNT_OBJ_ON_PAGE
    template_name = 'content/content.html'


class BookDetailView(BaseView, DetailView):
    """Запись о книге."""

    model = Book
    template_name = 'content/detail.html'


class BookCreateView(BaseView, CreateBaseView):
    """Cоздание записи о книге."""

    model = Book
    form_class = BookForm
    template_name = 'content/form.html'
    success_url = reverse_lazy('content:book')


class BookUpdateView(BaseView, UpdateView):
    """Редактирование записи о книге."""

    model = Book
    form_class = BookForm
    template_name = 'content/form.html'
    success_url = reverse_lazy('content:book')


class BookDeleteView(BaseView, DeleteView):
    """Удаление записи о книге."""

    model = Book
    template_name = 'content/delete.html'
    success_url = reverse_lazy('content:book')
