from django.urls import path
from . import views

app_name = "survey"

urlpatterns = [
    path("new/", views.CreateObservation.as_view(), name="create"),
    path("all_data/", views.ListObservatsions.as_view(), name="list"),
]
