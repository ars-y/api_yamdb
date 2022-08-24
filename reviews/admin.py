from django.contrib import admin

from reviews.models import Review, Comment


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """Админка для ревью."""
    list_display = (
        'author',
        'title',
        'text',
        'score',
        'created',
    )
    list_editable = ('title', 'score',)
    list_filter = ('created',)
    search_fields = ('author', 'title',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Админка для комментария."""
    list_display = ('author', 'review', 'text', 'created',)
    list_editable = ('review',)
    list_filter = ('created',)
    search_fields = ('author', 'review',)
