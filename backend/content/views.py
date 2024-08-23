from django.views import generic
from django.views.generic import ListView, UpdateView, DeleteView, CreateView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from content.models import Movie, Serial, Game, Book
from content.forms import MovieForm, SerialForm, BookForm, GameForm
from core.constants_content import COUNT_OBJ_ON_PAGE
from content.mixins import CheckUserObject


class Home(generic.TemplateView):
    """Домашняя страница."""
    template_name = 'content/home.html'


class BaseView(LoginRequiredMixin):
    """Базовый класс для CBV."""

    def get_queryset(self):
        queryset = self.model.objects.select_related(
            'status'
        ).prefetch_related('genre').filter(user=self.request.user)
        if self.request.GET.get('status'):
            queryset = queryset.filter(
                status__status=self.request.GET.get('status')
            )

        return queryset


class CreateBaseView(CreateView):
    """Базоваый класс создания для CBV."""

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class MovieListView(BaseView, ListView):
    """Список фильмов."""

    model = Movie
    paginate_by = COUNT_OBJ_ON_PAGE
    template_name = 'content/content.html'


class MovieDetailView(BaseView, CheckUserObject, DetailView):
    """Запись о фильме."""

    model = Movie
    template_name = 'content/detail.html'


class MovieCreateView(BaseView, CreateBaseView):
    """Cоздание записи о фильме."""

    model = Movie
    form_class = MovieForm
    template_name = 'content/form.html'


class MovieUpdateView(BaseView, CheckUserObject, UpdateView):
    """Редактирование записи о фильме."""

    model = Movie
    form_class = MovieForm
    template_name = 'content/form.html'


class MovieDeleteView(BaseView, CheckUserObject, DeleteView):
    """Удаление записи о фильме."""

    model = Movie
    template_name = 'content/delete.html'
    success_url = reverse_lazy('content:movie')


class SerialListView(BaseView, ListView):
    """Список сериалов."""

    model = Serial
    paginate_by = COUNT_OBJ_ON_PAGE
    template_name = 'content/content.html'


class SerialDetailView(BaseView, CheckUserObject, DetailView):
    """Запись о сериале."""

    model = Serial
    template_name = 'content/detail.html'


class SerialCreateView(BaseView, CreateBaseView):
    """Cоздание записи о сериале."""

    model = Serial
    form_class = SerialForm
    template_name = 'content/form.html'
    success_url = reverse_lazy('content:serial')


class SerialUpdateView(BaseView, CheckUserObject, UpdateView):
    """Редактирование записи о сериале."""

    model = Serial
    form_class = SerialForm
    template_name = 'content/form.html'
    success_url = reverse_lazy('content:serial')


class SerialDeleteView(BaseView, CheckUserObject, DeleteView):
    """Удаление записи о сериале."""

    model = Serial
    template_name = 'content/delete.html'
    success_url = reverse_lazy('content:serial')


class GameListView(BaseView, ListView):
    """Список игр."""

    model = Game
    paginate_by = COUNT_OBJ_ON_PAGE
    template_name = 'content/content.html'


class GameDetailView(BaseView, CheckUserObject, DetailView):
    """Запись о игре."""

    model = Game
    template_name = 'content/detail.html'


class GameCreateView(BaseView, CreateBaseView):
    """Cоздание записи о игре."""

    model = Game
    form_class = GameForm
    template_name = 'content/form.html'
    success_url = reverse_lazy('content:game')


class GameUpdateView(BaseView, CheckUserObject, UpdateView):
    """Редактирование записи о сериале."""

    model = Game
    form_class = GameForm
    template_name = 'content/form.html'
    success_url = reverse_lazy('content:game')


class GameDeleteView(BaseView, CheckUserObject, DeleteView):
    """Удаление записи о сериале."""

    model = Game
    template_name = 'content/delete.html'
    success_url = reverse_lazy('content:game')


class BookListView(BaseView, ListView):
    """Список книг."""

    model = Book
    paginate_by = COUNT_OBJ_ON_PAGE
    template_name = 'content/content.html'


class BookDetailView(BaseView, CheckUserObject, DetailView):
    """Запись о книге."""

    model = Book
    template_name = 'content/detail.html'


class BookCreateView(BaseView, CreateBaseView):
    """Cоздание записи о книге."""

    model = Book
    form_class = BookForm
    template_name = 'content/form.html'
    success_url = reverse_lazy('content:book')


class BookUpdateView(BaseView, CheckUserObject, UpdateView):
    """Редактирование записи о книге."""

    model = Book
    form_class = BookForm
    template_name = 'content/form.html'
    success_url = reverse_lazy('content:book')


class BookDeleteView(BaseView, CheckUserObject, DeleteView):
    """Удаление записи о книге."""

    model = Book
    template_name = 'content/delete.html'
    success_url = reverse_lazy('content:book')
