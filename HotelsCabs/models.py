# Create your models here.

from django.db import models
from django.core.validators import RegexValidator


class Hotels(models.Model):

    hotel_name = models.CharField(max_length=100)
    address_name = models.TextField(max_length=1000)
    website_link = models.URLField(max_length=400)
    phone_number = models.CharField(max_length=100)
    distance_in_km_from_campus = models.IntegerField()


class Cabs(models.Model):

    cab_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=100)
    information = models.TextField(max_length=1000)

class HotelLinks(models.Model):
    information = models.TextField(max_length=1000)
    website_link = models.URLField(max_length=400)