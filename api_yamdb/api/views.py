from rest_framework import viewsets

from reviews.models import Review, Comment
from api.serializers import ReviewSerializer, CommentSerializer


class ReviewViewset(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        pass

    def perform_create(self, serializer):
        pass


class CommentViewset(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        pass

    def perform_create(self, serializer):
        pass
