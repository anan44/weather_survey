from survey.models import Observation, SurveyPoint
from django.views.generic import TemplateView
# Create your views here.


class HomePage(TemplateView):
    """view presentting the home page and latest observations for each city
    on it
    """
    template_name = "index.html"
    model = Observation

    def get_context_data(self, *args, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)
        cities = [city.name for city in SurveyPoint.objects.all()]

        def last_obs(city):
            obs = Observation.objects.filter(survey_point__name=city)
            if obs:
                return obs.last()
            else:
                return {"survey_point": city,
                        "temperature": "No data. Please help us by \
                        contributing"}

        data = [last_obs(city) for city in cities]
        context["data"] = data

        print(data)
        return context


class ThanksPage(TemplateView):
    """Very basic Thanks view
    """
    template_name = "thanks.html"
