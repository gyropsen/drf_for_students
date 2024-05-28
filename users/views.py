from rest_framework.viewsets import ModelViewSet
from django_filters import rest_framework as filters
from rest_framework.filters import OrderingFilter

from users.models import User, Payment
from users.serializers import UserSerializer, PaymentSerializer, UserDetailSerializer


# Course
class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_serializer_class(self):
        if self.action == "retrieve":
            return UserDetailSerializer
        return self.serializer_class


# Payment
class PaymentViewSet(ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = (filters.DjangoFilterBackend, OrderingFilter)
    filterset_fields = ("paid_course", "paid_lesson", "method")
    ordering_fields = ("date_payment",)
