from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import PaymentViewSet, UserViewSet

app_name = UsersConfig.name

router = SimpleRouter()
router.register(r"user", UserViewSet)
router.register(r"payments", PaymentViewSet)

urlpatterns = [
    path("token/", TokenObtainPairView.as_view(permission_classes=(AllowAny,)), name="token_obtain_pair"),
    path("token-refresh/", TokenRefreshView.as_view(permission_classes=(AllowAny,)), name="token_refresh"),
] + router.urls
