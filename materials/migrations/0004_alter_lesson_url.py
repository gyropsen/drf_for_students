# Generated by Django 5.0.6 on 2024-05-27 14:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("materials", "0003_alter_lesson_course"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lesson",
            name="url",
            field=models.URLField(blank=True, null=True, verbose_name="url"),
        ),
    ]
