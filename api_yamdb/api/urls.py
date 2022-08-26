from rest_framework.routers import DefaultRouter
from django.urls import include, path
from .views import UserRegistrationView, UserGetTokenView

app_name = 'api'
router = DefaultRouter()

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/signup/', UserRegistrationView.as_view(), name='signup'),
    path('v1/auth/token/', UserGetTokenView.as_view(), name='token'),
]
