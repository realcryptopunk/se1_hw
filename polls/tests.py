import coverage

# Start coverage before running tests
cov = coverage.Coverage()
cov.start()

# Create your tests here.
import datetime

from django.test import TestCase
from django.utils import timezone

from polls.models import Question


class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

# Run your tests here
# For example, if using unittest:
import unittest
from polls.tests import QuestionModelTests

suite = unittest.TestLoader().loadTestsFromTestCase(QuestionModelTests)
unittest.TextTestRunner().run(suite)

# Stop coverage and report results
cov.stop()
cov.save()
cov.report()
