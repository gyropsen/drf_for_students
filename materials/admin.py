from django.contrib import admin

from materials.models import Course, Lesson


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
    )
    search_fields = ("name", "description")


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "url",
        "course",
    )
    search_fields = ("name", "description")
    list_filter = ("course",)
