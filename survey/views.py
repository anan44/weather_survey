from datetime import timedelta
from django.db.models import Avg, Max, Min
from django.utils import timezone
from django.urls import reverse_lazy
from django.views import generic
from braces.views import SelectRelatedMixin
from django.shortcuts import render

from .models import Observation, SurveyPoint
# Create your views here.


class CreateObservation(SelectRelatedMixin, generic.CreateView):
    """View to create the actual observations in the available cities
    """
    fields = ("temperature", "survey_point")
    model = Observation
    success_url = reverse_lazy("thanks")


class ListObservatsions(generic.ListView):
    """View for presenting all the data gathered ever
    """
    model = Observation
    ordering = ["-time_stamp"]


class LatestStats(generic.TemplateView):
    """This will be what ever solution will be used for past 24h view
    """
    model = Observation
    template_name = "survey/latest_stats.html"

    def get_context_data(self, *args, **kwargs):
        """creates the context data for the view
        """

        def last_obs(city_name):
            """helper function for getting latest observation
            regardless of the time stamp
            """
            obs = Observation.objects
            obs = obs.filter(survey_point__name=city_name)
            if obs.count() > 0:
                return obs.first().temperature
            else:
                return "n/a"

        # create the context item
        context = super(LatestStats, self).get_context_data(**kwargs)
        # get list of SurveyPoint names
        point_names = [point.name for point in SurveyPoint.objects.all()]

        # get all the Observations in past 24h
        time_from = timezone.now() - timedelta(days=1)
        obs = Observation.objects
        obs = obs.filter(time_stamp__gte=time_from)

        # make a dict of all cities and their data
        all_cities = []
        for pn in point_names:
            city_data = obs.filter(survey_point__name=pn)
            data = {}
            data["name"] = pn
            data["latest"] = last_obs(pn)
            if city_data.count() > 0:
                data["min"] = city_data.aggregate(Min("temperature"))
                data["min"] = data["min"]["temperature__min"]
                data["max"] = city_data.aggregate(Max("temperature"))
                data["max"] = data["max"]["temperature__max"]
                data["avg"] = city_data.aggregate(Avg("temperature"))
                data["avg"] = data["avg"]["temperature__avg"]
            else:
                data["min"] = "n/a"
                data["max"] = "n/a"
                data["avg"] = "n/a"

            all_cities.append(data)

        context["data"] = all_cities
        return context
