# Generated by Django 5.0.6 on 2024-05-28 13:02

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0005_alter_payment_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="payment",
            name="user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="payments",
                to=settings.AUTH_USER_MODEL,
                verbose_name="user",
            ),
        ),
    ]
