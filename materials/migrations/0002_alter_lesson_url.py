# Generated by Django 5.0.6 on 2024-05-27 13:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("materials", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lesson",
            name="url",
            field=models.TextField(blank=True, null=True, verbose_name="url"),
        ),
    ]
