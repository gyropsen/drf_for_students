from rest_framework.serializers import ModelSerializer, SerializerMethodField, IntegerField

from materials.models import Course, Lesson


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class CourseDetailSerializer(ModelSerializer):
    count_lessons = SerializerMethodField()

    def get_count_lessons(self, instance):
        return len(Lesson.objects.filter(course=instance))

    class Meta:
        model = Course
        fields = "__all__"


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"
