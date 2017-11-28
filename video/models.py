from django.db import models


class Camera(models.Model):
    url = models.URLField(unique=True)
    district = models.CharField(max_length=200)
    street = models.CharField(max_length=200)
    longitude = models.FloatField()
    latitude = models.FloatField()

