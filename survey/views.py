from django.urls import reverse_lazy
from django.views import generic
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
