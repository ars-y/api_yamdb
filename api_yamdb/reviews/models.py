from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=256,
        verbose_name='Категория',
    )
    slug = models.SlugField(
        unique=True,
        max_length=50,
        verbose_name='Идентификатор',
    )

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(
        max_length=256,
        verbose_name='Жанр',
    )
    slug = models.SlugField(
        unique=True,
        max_length=50,
        verbose_name='Идентификатор',
    )

    class Meta:
        ordering = ['name', ]

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name='Имя произведения',
    )
    year = models.PositiveIntegerField(
        db_index=True,
        validators=[validate_year],
        verbose_name='Год',
    )
    description = models.TextField(
        null=True,
        verbose_name='Описание',
    )
    genre = models.ManyToManyField(
        Genre,
        blank=True,
        verbose_name='Жанр',
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Категория',
    )

    class Meta:
        ordering = ['name', ]

    def __str__(self):
        return self.name
