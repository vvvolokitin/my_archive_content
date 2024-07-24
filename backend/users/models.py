from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Модель пользователя."""

    username = models.CharField(
        verbose_name='Юзернейм',
        max_length=50,
        unique=True,
        validators=(UnicodeUsernameValidator(),)
    )

    avatar = models.ImageField(
        verbose_name='Аватар',
        upload_to='users',
        blank=True
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('username',)

    def clean(self):
        if self.username.lower() in ('me', 'em'):
            raise ValidationError(
                'Имя пользователя не может быть "me"'
            )
