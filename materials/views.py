from rest_framework.generics import CreateAPIView, DestroyAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from materials.models import Course, Lesson
from materials.permissions import IsModerator, IsOwner
from materials.serializers import CourseSerializer, LessonSerializer, CourseDetailSerializer


# Course
class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get_serializer_class(self):
        if self.action == "retrieve":
            return CourseDetailSerializer
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
            permission_classes = (IsAuthenticated, )
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        new_course = serializer.save(owner=self.request.user)
        super().perform_create(new_course)


# Lesson
class LessonCreateAPIView(CreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (IsAuthenticated, ~IsModerator)

    def perform_create(self, serializer):
        new_lesson = serializer.save(owner=self.request.user)
        super().perform_create(new_lesson)


class LessonListAPIView(ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonRetrieveAPIView(RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (IsAuthenticated, IsModerator | IsOwner)


class LessonUpdateAPIView(UpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (IsAuthenticated, IsModerator | IsOwner)


class LessonDestroyAPIView(DestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (IsAuthenticated, IsOwner)
