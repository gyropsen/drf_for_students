from django.core.management.base import BaseCommand

from materials.models import Course, Lesson
from users.models import Payment, User


class Command(BaseCommand):
    help = "Runs APScheduler."

    def handle(self, *args, **options):
        user = User.objects.create(
            email="user2@gmail.com",
            first_name="user2",
            last_name="user2",
            is_superuser=False,
            is_staff=False,
            is_active=True,
        )

        user.set_password("12345")
        user.save()

        payment1 = Payment.objects.create(user=user, paid_course=Course.objects.get(pk=2), amount=1000, method="CASH")
        payment2 = Payment.objects.create(user=user, paid_lesson=Lesson.objects.get(pk=6), amount=1000)
        payment1.save()
        payment2.save()
