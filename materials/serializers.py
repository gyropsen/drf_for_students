from rest_framework.serializers import ModelSerializer, SerializerMethodField, IntegerField

from materials.models import Course, Lesson


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class CourseDetailSerializer(ModelSerializer):
    count_lessons = SerializerMethodField()
    lessons = LessonSerializer(many=True)

    def get_count_lessons(self, instance):
        return Lesson.objects.filter(course=instance).count()

    class Meta:
        model = Course
        fields = "__all__"
