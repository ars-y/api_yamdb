from django.db import models
from django.contrib.auth.models import AbstractUser


CHOICES = (
    ('Moderator', 'Модератор'),
    ('Admin', 'Админ'),
    ('User', 'Пользователь')
)


class User(AbstractUser):
    """Модель пользователя."""
    email = models.EmailField(
        'Почта',
        unique=True,
    )
    username = models.CharField(
        verbose_name='Имя пользователя',
        max_length=150,
        null=True,
        unique=True
    )
    bio = models.TextField(
        'Биография',
        blank=True,
    )
    role = models.CharField(
        'Роли',
        max_length=30,
        choices=CHOICES
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
