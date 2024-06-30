from datetime import timedelta

from celery import shared_task

from users.models import User


@shared_task
def check_active():
    for user in User.objects.filter(is_active=True):
        if user.last_login:
            if user.last_login >= timedelta(days=30):
                user.is_active = False
