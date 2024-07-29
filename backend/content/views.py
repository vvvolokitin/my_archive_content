from django.shortcuts import render
from django.views import generic


class Home(generic.TemplateView):
    """Домашняя страница."""
    template_name = 'content/home.html'
