from rest_framework import viewsets

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
        pass

    def perform_create(self, serializer):
        pass
