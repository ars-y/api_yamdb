from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import TitleViewSet, GenreViewSet
from api.views import CategoryViewSet


router = DefaultRouter()
router.register('categories', CategoryViewSet, basename='categories')
router.register('genres', GenreViewSet, basename='genres')
router.register('titles', TitleViewSet, basename='titles')

urlpatterns = [
    path('v1/', include(router.urls)),
]
