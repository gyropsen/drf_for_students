from django.urls import path, include
from rest_framework.routers import SimpleRouter
from rest_framework.permissions import AllowAny

from users.apps import UsersConfig
from users.views import UserViewSet, PaymentViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = UsersConfig.name

router = SimpleRouter()
router.register("user", UserViewSet)
router.register("payments", PaymentViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path('token/', TokenObtainPairView.as_view(permission_classes=(AllowAny,)), name='token_obtain_pair'),
    path('token-refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
