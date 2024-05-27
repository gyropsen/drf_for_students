from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from materials.models import NULLABLE


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name=_("email"), help_text=_("enter your email"))
    phone_number = PhoneNumberField(**NULLABLE, verbose_name=_("phone"))
    city = models.CharField(max_length=128, **NULLABLE, verbose_name=_("city"))
    avatar = models.ImageField(upload_to="users/avatars/", **NULLABLE, verbose_name=_("avatar"))

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def __str__(self):
        return self.email
