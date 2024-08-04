from django.urls import path

from content.views import Home

app_name = 'content'

urlpatterns = [
    path('', Home.as_view(), name='home'),
]
