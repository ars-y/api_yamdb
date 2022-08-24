from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from core.models import CreatedModel


class Review(CreatedModel):
    """Модель отзывов."""
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор',
        related_name='reviews',
    )
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        verbose_name='Произведение',
        related_name='reviews',
    )
    text = models.TextField(
        verbose_name='Текст',
    )
    score = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(10)
        ],
        verbose_name='Оценка'
    )

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        oredering = ['created']
        constraints = [
            models.UniqueConstraint(
                fields=['author, title'],
                name='unique_review'
            )
        ]
