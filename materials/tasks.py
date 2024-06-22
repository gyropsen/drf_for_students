from django.core.mail import send_mail
from celery import shared_task
from config import settings
from materials.models import Subscription, Course
from django.shortcuts import get_object_or_404


@shared_task
def send_update_course(course_pk: int):
    course = get_object_or_404(Course, pk=course_pk)
    subscriptions = Subscription.objects.filter(course=course.pk)
    recipient_list = [sub.user.email for sub in subscriptions] if subscriptions else None
    print(recipient_list)
    if recipient_list:
        send_mail(
            subject="Update course",
            message=f"The owner {course.owner.email} updated his course {course.name}",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=recipient_list,
        )
