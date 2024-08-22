from django.urls import path, include, reverse_lazy
from django.views.generic.edit import CreateView

from users.forms import CustomUserCreationForm


urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path(
        'auth/registration/',
        CreateView.as_view(
            template_name='registration/registration_form.html',
            form_class=CustomUserCreationForm,
            success_url=reverse_lazy('content:home'),
        ),
        name='registration',
    ),
]
