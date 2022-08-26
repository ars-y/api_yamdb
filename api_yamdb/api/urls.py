from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import ReviewViewset, CommentViewset


router = DefaultRouter()
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
]
