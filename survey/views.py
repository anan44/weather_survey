from datetime import timedelta
from django.db.models import Avg, Max, Min
from django.utils import timezone
from django.urls import reverse_lazy
from django.views import generic
from braces.views import SelectRelatedMixin
from django.shortcuts import render

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
    context_object_name = "data"

    def get_context_data(self, **kwargs):
        context = super(LatestStats, self).get_context_data(**kwargs)
        time_from = timezone.now() - timedelta(days=1)
        past_24h = Observation.objects.filter(time_stamp__gte=time_from)
        context["avg_temp"] = past_24h.aggregate(Avg("temperature"))["temperature__avg"]
        context["max_temp"] = past_24h.aggregate(Max("temperature"))["temperature__max"]
        context["min_temp"] = past_24h.aggregate(Min("temperature"))["temperature__min"]
        return context
