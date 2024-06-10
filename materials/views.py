from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from django.utils.translation import gettext_lazy as _
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import PermissionDenied

from materials.models import Course, Lesson, Subscription
from materials.paginators import CustomPagination
from materials.permissions import IsModerator, IsOwner
from materials import serializers


# Course
# # # viewsets

class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all().order_by("pk")
    serializer_class = serializers.CourseSerializer
    pagination_class = CustomPagination

    # paginator = self.django_paginator_class(queryset, page_size)

    def get_serializer_class(self):
        if self.action == "retrieve":
            return serializers.CourseDetailSerializer
        return self.serializer_class

    def get_permissions(self):
        """
        Instantiates and returns the create of permissions that this view requires.
        """
        if self.action == 'create':
            permission_classes = (IsAuthenticated, ~IsModerator,)
        elif self.action == 'destroy':
            permission_classes = (IsAuthenticated, IsOwner)
        elif self.action in ['update', 'retrieve', 'partial_update']:
            permission_classes = (IsAuthenticated, IsModerator | IsOwner)
        else:
            permission_classes = (IsAuthenticated,)
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        new_course = serializer.save(owner=self.request.user)
        super().perform_create(new_course)

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.groups.filter(name='moderator').exists():
            return queryset
        return queryset.filter(owner=self.request.user)


# Lesson
# #  generic
# # # Create
class LessonCreateAPIView(generics.CreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = serializers.LessonSerializer
    permission_classes = (IsAuthenticated, ~IsModerator)

    def perform_create(self, serializer):
        new_lesson = serializer.save(owner=self.request.user)
        super().perform_create(new_lesson)


# # # List
class LessonListAPIView(generics.ListAPIView):
    queryset = Lesson.objects.all().order_by("pk")
    serializer_class = serializers.LessonSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(owner=self.request.user)


# # # Retrieve
class LessonRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = serializers.LessonSerializer
    permission_classes = (IsAuthenticated, IsModerator | IsOwner)


# # # Update
class LessonUpdateAPIView(generics.UpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = serializers.LessonSerializer
    permission_classes = (IsAuthenticated, IsModerator | IsOwner)


# # # Destroy
class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = serializers.LessonSerializer
    permission_classes = (IsAuthenticated, IsOwner)


# Subscription
# #  generic
# # # Create
class SubscriptionCreateDestroyAPIView(generics.CreateAPIView):
    queryset = Subscription.objects.all()
    serializer_class = serializers.SubscriptionSerializer
    permission_classes = (IsAuthenticated, ~IsModerator)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        message, stat = self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(message, status=stat, headers=headers)

    def perform_create(self, serializer, *args, **kwargs):
        user = self.request.user
        course_id = self.request.data.get("course_id")
        message = {}

        # Проверить, есть ли курс по pk в базе данных
        course = generics.get_object_or_404(Course.objects.all(), pk=course_id)

        # Проверить, имеется ли подписка на курс у данного пользователя
        old_subscription = Subscription.objects.filter(user=user, course=course)
        if old_subscription.exists():
            # Если подписка на курс есть, удалить
            old_subscription.delete()
            message["success"] = _("subscription removed")
            stat = status.HTTP_204_NO_CONTENT
        else:
            # Иначе создать подписку
            new_subscription = serializer.save(user=user, course=course)
            super().perform_create(new_subscription)
            message["success"] = _("subscription created")
            stat = status.HTTP_201_CREATED
        return message, stat

# class SubscriptionListAPIView(generics.ListAPIView):
#     queryset = Subscription.objects.all()
#     serializer_class = serializers.SubscriptionSerializer
