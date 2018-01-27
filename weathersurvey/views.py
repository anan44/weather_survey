from survey.models import Observation
from django.views.generic import TemplateView
from django.db import connection
# Create your views here.


class HomePage(TemplateView):
    """view presentting the home page and latest observations for each city
    on it
    """
    template_name = "index.html"
    model = Observation

    def get_context_data(self, *args, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)
        query = """
        SELECT survey_observation.id, survey_surveypoint.name, temperature
        FROM survey_observation
        JOIN survey_surveypoint
        ON survey_observation.survey_point_id = survey_surveypoint.id
        WHERE survey_observation.id IN (
        SELECT MAX(id)
        FROM survey_observation
        GROUP BY survey_point_id)
        ORDER BY survey_observation.id DESC
        """

        cursor = connection.cursor().execute(query).fetchall()
        cursor.execute(query)

        data = cursor.fetchall()

        context["data"] = data
        return context


class ThanksPage(TemplateView):
    """Very basic Thanks view
    """
    template_name = "thanks.html"
