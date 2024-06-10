from rest_framework.test import APITestCase
from materials.models import Course, Lesson
from users.models import User
from django.urls import reverse


class CourseTestCase(APITestCase):

    def setUp(self) -> None:
        super().setUp()
        self.test_user = User.objects.create(
            email="test_user@gmail.com",
            first_name="test_user",
            last_name="test_user",
            is_superuser=False,
            is_staff=False,
            is_active=True,
        )

        self.test_course = Course.objects.create(name="test_course", owner=self.test_user)
        self.test_lesson = Lesson.objects.create(name="test_lesson", course=self.test_course, owner=self.test_user)

    def test_getting_course_list(self):
        """
            Тестирование получения списка курсов
        """
        url = reverse("materials:courses", args=[self.test_course.pk])
        response = self.client.get(url)
        print(response)
        # response = self.client.get(
        #     '/materials/courses/'
        # )
        #
        # self.assertEqual(
        #     response.body,
        #     [
        #         {
        #             'name': self.test_course.first_name,
        #         }
        #     ]
        # )
