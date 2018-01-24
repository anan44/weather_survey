from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class SurveyPoint(models.Model):
    """Individual survey point for data collection
    """
    name = models.CharField(max_length=255,
                            unique=True)
    x_Coordinate = models.FloatField()
    y_Coordinate = models.FloatField()

    def __str__(self):
        return self.name


class Observation(models.Model):
    """Individual weather Observation on a single SurveyPoint
    """
    temperature = models.IntegerField(validators=[MaxValueValidator(60),
                                                  MinValueValidator(-40)])
    time_stamp = models.DateTimeField(auto_now_add=True)
    survey_point = models.ForeignKey(SurveyPoint,
                                     on_delete=models.CASCADE)

    def __str__(self):
        return "{}: {}".format(self.survey_point, str(self.temperature))
