from django.urls import path, include
from rest_framework.routers import SimpleRouter

from materials.apps import MaterialsConfig
from materials.views import (CourseViewSet, LessonCreateAPIView, LessonDestroyAPIView, LessonListAPIView,
                             LessonRetrieveAPIView, LessonUpdateAPIView)

app_name = MaterialsConfig.name

router = SimpleRouter()
router.register("", CourseViewSet)

urlpatterns = [
    path("courses/", include(router.urls)),
    path("lessons/", LessonListAPIView.as_view(), name="lessons_list"),
    path("lessons/create/", LessonCreateAPIView.as_view(), name="lessons_create"),
    path("lessons/<int:pk>/update/", LessonUpdateAPIView.as_view(), name="lessons_update"),
    path("lessons/<int:pk>/delete/", LessonDestroyAPIView.as_view(), name="lessons_delete"),
    path("lessons/<int:pk>/", LessonRetrieveAPIView.as_view(), name="lessons_retrieve"),
]
