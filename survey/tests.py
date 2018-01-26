from .models import SurveyPoint, Observation
from .views import LatestStats
from weathersurvey.views import HomePage
from django.test import TestCase
from django_webtest import WebTest

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
    """Tests for creating Survey Points
    """

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
        self.assertEquals(SurveyPoint.objects.all()[0].name, "Tokio")


class CreateObservationTest(TestCase):
    """Tests for creation of Observations
    """

    def test_was_able_to_create_observation(self):
        """Test for creating a single observation
        """
        create_surveypoints(TEST_SURVEYPOINTS)

        point = SurveyPoint.objects.first()
        Observation.objects.create(temperature=5, survey_point=point)

        self.assertEqual(Observation.objects.first().survey_point, point)
        self.assertIs(Observation.objects.first().temperature, 5)

    def test_observations_in_right_order(self):
        """Creates few observations and checks that they are in correct order
        """
        create_surveypoints(TEST_SURVEYPOINTS)

        point = SurveyPoint.objects.last()
        Observation.objects.create(temperature=-3, survey_point=point)
        Observation.objects.create(temperature=15, survey_point=point)
        Observation.objects.create(temperature=32, survey_point=point)

        self.assertIs(Observation.objects.all()
                                 .order_by("time_stamp")[0].temperature, -3)
        self.assertIs(Observation.objects.all()
                                 .order_by("time_stamp")[1].temperature, 15)
        self.assertIs(Observation.objects.all()
                                 .order_by("time_stamp")[2].temperature, 32)


class PageTest(WebTest):
    """Test for creation of observations
    """
    def test_check_make_observation(self):
        """tests to check that make observation page exists
        """
        res = self.app.get("/survey/new/")
        self.assertEqual(res.status, "200 OK")

    def test_check_index(self):
        """tests to check index page exists
        """
        res = self.app.get("/")
        self.assertEqual(res.status, "200 OK")

    def test_check_latest_stats(self):
        """tests to check latest_stats exists
        """
        res = self.app.get("/survey/latest_stats/")
        self.assertEqual(res.status, "200 OK")

    def test_check_all_data(self):
        """tests to check all data page exists
        """
        res = self.app.get("/survey/all_data/")
        self.assertEqual(res.status, "200 OK")


class QueryTest(TestCase):
    """to test database queries used
    """
    def test_latest_stats_query(self):
        """checks if the latest stats query returns the correct data
        """
        create_surveypoints(TEST_SURVEYPOINTS)

        points = SurveyPoint.objects.all()

        Observation.objects.create(temperature=-5, survey_point=points[1])
        Observation.objects.create(temperature=10, survey_point=points[1])
        Observation.objects.create(temperature=12, survey_point=points[0])
        Observation.objects.create(temperature=20, survey_point=points[0])
        Observation.objects.create(temperature=28, survey_point=points[2])
        Observation.objects.create(temperature=-11, survey_point=points[1])

        context = LatestStats().get_context_data()["data"]
        self.assertEqual(context[0]["temperature__min"], -11)
        self.assertEqual(context[0]["temperature__max"], 10)
        self.assertEqual(context[2]["temperature__min"], 12)
        self.assertEqual(context[2]["temperature__max"], 20)
        self.assertEqual(context[1]["temperature__min"], 28)
        self.assertEqual(context[1]["temperature__max"], 28)

    def test_home_page_query(self):
        """check if the query in latest stats works as inteded
        """
        create_surveypoints(TEST_SURVEYPOINTS)

        points = SurveyPoint.objects.all()

        Observation.objects.create(temperature=-5, survey_point=points[1])
        Observation.objects.create(temperature=10, survey_point=points[1])
        Observation.objects.create(temperature=12, survey_point=points[0])

        context = HomePage().get_context_data()["data"]
        self.assertEqual(context[0][2], 12)
        self.assertEqual(context[1][2], 10)
