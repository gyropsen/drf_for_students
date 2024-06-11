from rest_framework.serializers import ModelSerializer

from users.models import Payment, User


class PaymentSerializer(ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"
        # exclude = ("amount",)


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class UserDetailSerializer(ModelSerializer):
    payments = PaymentSerializer(many=True)

    class Meta:
        model = User
        fields = "__all__"


class UserShortSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = ("password", "last_name")
