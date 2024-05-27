# Generated by Django 5.0.6 on 2024-05-27 10:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Course",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=128, verbose_name="name")),
                (
                    "preview",
                    models.ImageField(
                        blank=True,
                        help_text="indicate a preview",
                        null=True,
                        upload_to="materials/course_previews/",
                        verbose_name="preview",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True, help_text="please provide a description", null=True, verbose_name="description"
                    ),
                ),
            ],
            options={
                "verbose_name": "course",
                "verbose_name_plural": "courses",
            },
        ),
        migrations.CreateModel(
            name="Lesson",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=128, verbose_name="name")),
                (
                    "description",
                    models.TextField(
                        blank=True, help_text="please provide a description", null=True, verbose_name="description"
                    ),
                ),
                (
                    "preview",
                    models.ImageField(
                        blank=True,
                        help_text="indicate a preview",
                        null=True,
                        upload_to="materials/lesson_previews/",
                        verbose_name="preview",
                    ),
                ),
                ("url", models.TextField()),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="materials.course", verbose_name="course"
                    ),
                ),
            ],
            options={
                "verbose_name": "lesson",
                "verbose_name_plural": "lessons",
            },
        ),
    ]
