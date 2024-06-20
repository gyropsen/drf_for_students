# Generated by Django 5.0.6 on 2024-06-11 17:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0006_alter_payment_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="payment",
            name="session_id",
            field=models.CharField(blank=True, max_length=127, null=True, verbose_name="session"),
        ),
        migrations.AddField(
            model_name="payment",
            name="url",
            field=models.URLField(blank=True, max_length=511, null=True, verbose_name="url"),
        ),
    ]
