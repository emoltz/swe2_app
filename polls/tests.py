from django.test import TestCase
import datetime
from django.utils import timezone

from .models import Question


# Create your tests here.


class QuestionModelsTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        # returns false for questions who pub_date is in the future
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)


class UnitTestCase(TestCase):
    def test_one(self):
        self.assertEqual(1, 1)

    def test_home_homepage_template(self):
        response = self.client.get("/")  # this is the homepage
        self.assertTemplateUsed(response, "polls/base.html")
