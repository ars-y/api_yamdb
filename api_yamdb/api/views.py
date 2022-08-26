from rest_framework import viewsets
from django.shortcuts import get_object_or_404

from reviews.models import Review, Comment
from api.permissions import AuthorOrReadOnly
from api.serializers import ReviewSerializer, CommentSerializer


class ReviewViewset(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = [AuthorOrReadOnly]

    def get_queryset(self):
        pass

    def perform_create(self, serializer):
        pass


class CommentViewset(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [AuthorOrReadOnly]

    def get_queryset(self):
        review = get_object_or_404(Review, pk=self.kwargs.get('review_id'))
        return review.comments

    def perform_create(self, serializer):
        review = get_object_or_404(
            Review,
            pk=self.kwargs.get('review_id'),
            title=self.kwargs.get('title_id')
        )
        serializer.save(author=self.request.user, review=review)
