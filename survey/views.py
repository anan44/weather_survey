from datetime import timedelta
from django.db.models import Min, Max, Avg
from django.utils import timezone
from django.urls import reverse_lazy
from django.views import generic
from django.db import connection
from braces.views import SelectRelatedMixin

from .models import Observation
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
        # create the context item
        context = super(LatestStats, self).get_context_data(**kwargs)
        # get list of SurveyPoint names
        time_from = timezone.now() - timedelta(days=1)

        data = Observation.objects.filter(time_stamp__gte=time_from) \
                          .values("survey_point__name") \
                          .annotate(Min("temperature"),
                                    Max("temperature"),
                                    Avg("temperature"))

        context["data"] = data
        return context
