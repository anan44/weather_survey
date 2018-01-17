from django.db import models

# Create your models here.


class SurveyPoint(models.Model):
    """Individual survey point for data collection
    """
    name = models.CharField(max_length=255,
                            unique=True)
    x_Coordinate = models.FloatField()
    y_Coordinate = models.FloatField()


class Observation(models.Model):
    """Individual weather Observation on a single SurveyPoint
    """
    temperature = models.IntegerField()
    time_stamp = models.DateTimeField(auto_now_add=True)
    survey_point = models.ForeignKey(SurveyPoint,
                                     on_delete=models.CASCADE)
