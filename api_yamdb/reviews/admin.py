from django.contrib import admin

from reviews.models import (
    User,
    Category,
    Genre,
    Title,
    GenreTitle,
    Review,
    Comment
)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """Админка для ревью."""
    list_display = (
        'author',
        'title',
        'text',
        'score',
        'pub_date',
    )
    list_editable = ('title', 'score',)
    list_filter = ('pub_date',)
    search_fields = ('author', 'title',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Админка для комментария."""
    list_display = ('author', 'review', 'text', 'pub_date',)
    list_editable = ('review',)
    list_filter = ('pub_date',)
    search_fields = ('author', 'review',)

admin.site.register(User)
admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(Title)
admin.site.register(GenreTitle)
