from rest_framework.routers import DefaultRouter
from django.urls import include, path

from api.views import UserRegistrationView, UserGetTokenView, UserViewSet, ReviewViewset, CommentViewset


router = DefaultRouter()
router.register('users', UserViewSet)
router.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewset, basename='reviews'
)
router.register(
     r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
     CommentViewset, basename='comments'
)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/signup/', UserRegistrationView.as_view(), name='signup'),
    path('v1/auth/token/', UserGetTokenView.as_view(), name='token'),
]
