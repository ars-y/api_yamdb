from django.db import models
from django.contrib.auth.models import AbstractUser

CHOICES = (
    ('Moderator', 'Модератор'),
    ('Admin', 'Админ'),
    ('User', 'Пользователь')
)


class Users(AbstractUser):
    email = models.EmailField(
        'Почта',
        unique=True,
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
