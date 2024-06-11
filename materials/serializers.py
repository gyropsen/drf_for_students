from rest_framework.serializers import ModelSerializer, SerializerMethodField, URLField

from materials.models import Course, Lesson, Subscription
from materials.validators import URLCorrectValidator


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"
        validators = [URLCorrectValidator(field="url", url="https://www.youtube.com/")]


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class CourseDetailSerializer(ModelSerializer):
    count_lessons = SerializerMethodField()
    lessons = LessonSerializer(many=True)
    subscription = SerializerMethodField()

    def get_subscription(self, instance):
        return Subscription.objects.filter(course=instance, user=self.context["request"].user).exists()

    def get_count_lessons(self, instance):
        return Lesson.objects.filter(course=instance).count()

    class Meta:
        model = Course
        fields = "__all__"


class SubscriptionSerializer(ModelSerializer):
    class Meta:
        model = Subscription
        fields = "__all__"
