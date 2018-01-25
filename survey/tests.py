from .models import SurveyPoint, Observation
from django.test import TestCase

# Create your tests here.
TEST_SURVEYPOINTS = [
    ["Tokio", 35.6584421, 139.7328635],
    ["Helsinki", 60.1697530, 24.9490830],
    ["New York", 40.7406905, -73.9938438],
    ["Amsterdam", 52.3650691, 4.9040238],
    ["Dubai", 25.092535, 55.1562243],
]


def create_surveypoints(sp_list):
    for sp in sp_list:
        SurveyPoint.objects.create(name=sp[0],
                                   x_coordinate=sp[1],
                                   y_coordinate=sp[2])


class CreateSurveyPointsTest(TestCase):

    def test_was_able_to_create_multiple_sp(self):
        """test creation of 5 SurveyPoints
        """
        create_surveypoints(TEST_SURVEYPOINTS)

        self.assertIs(SurveyPoint.objects.all().count(), 5)

    def test_was_able_to_create_single_sp(self):
        """tries to create single SurveyPoint
        """
        create_surveypoints([TEST_SURVEYPOINTS[0]])
        self.assertIs(SurveyPoint.objects.all().count(), 1)
