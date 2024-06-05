from django.db import models
from django.utils.translation import gettext_lazy as _
from config import settings

NULLABLE = {"blank": True, "null": True}


class Course(models.Model):
    name = models.CharField(max_length=128, verbose_name=_("name"))
    preview = models.ImageField(
        upload_to="materials/course_previews/",
        **NULLABLE,
        verbose_name=_("preview"),
        help_text=_("indicate a preview")
    )
    description = models.TextField(
        **NULLABLE, verbose_name=_("description"), help_text=_("please provide a description")
    )
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE, verbose_name=_("owner"))

    class Meta:
        verbose_name = _("course")
        verbose_name_plural = _("courses")


class Lesson(models.Model):
    name = models.CharField(max_length=128, verbose_name=_("name"))
    description = models.TextField(
        **NULLABLE, verbose_name=_("description"), help_text=_("please provide a description")
    )
    preview = models.ImageField(
        upload_to="materials/lesson_previews/",
        **NULLABLE,
        verbose_name=_("preview"),
        help_text=_("indicate a preview")
    )
    url = models.URLField(**NULLABLE, verbose_name=_("url"))
    course = models.ForeignKey(Course, on_delete=models.CASCADE, **NULLABLE, verbose_name=_("course"),
                               related_name="lessons")

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE, verbose_name=_("owner"))

    class Meta:
        verbose_name = _("lesson")
        verbose_name_plural = _("lessons")
