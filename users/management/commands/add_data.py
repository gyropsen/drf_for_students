from django.core.management.base import BaseCommand

from materials.models import Course, Lesson
from users.models import Payment, User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email="user3@gmail.com",
            first_name="user3",
            last_name="user3",
            is_superuser=False,
            is_staff=False,
            is_active=True,
        )

        user.set_password("12345")
        user.save()

        course = Course.objects.create(name="DRF")
        lesson = Lesson.objects.create(name="serializers", course=course)

        course.save()
        lesson.save()

        payment1 = Payment.objects.create(user=user, paid_course=course, amount=1000, method="CASH")
        payment2 = Payment.objects.create(user=user, paid_lesson=lesson, amount=1000)
        payment1.save()
        payment2.save()
