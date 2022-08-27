from rest_framework.routers import DefaultRouter
from django.urls import include, path
from api.views import UserRegistrationView, UserGetTokenView, UserViewSet, TitleViewSet, GenreViewSet, CategoryViewSet

app_name = 'api'
router = DefaultRouter()
router.register('users', UserViewSet)
router.register('categories', CategoryViewSet, basename='category')
router.register('genres', GenreViewSet, basename='genre')
router.register('titles', TitleViewSet, basename='title')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/signup/', UserRegistrationView.as_view(), name='signup'),
    path('v1/auth/token/', UserGetTokenView.as_view(), name='token'),
]
