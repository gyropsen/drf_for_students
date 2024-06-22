from datetime import timedelta
from celery import shared_task
from users.models import User


@shared_task
def check_active():
    for user in User.objects.all():
        if user.last_login:
            if user.last_login >= timedelta(days=30):
                user.is_active = False
