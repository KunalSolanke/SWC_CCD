from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class Location(models.Model):
    link = models.URLField(max_length=400)
    information = models.ArrayField(models.CharField())
    link_name = models.CharField(max_length=200)

    linksArray = models.ArrayField(models.URLField())
    linksNameArray = models.ArrayField(models.CharField())

class Connectivity(models.Model):
    link = models.URLField(max_length=400)
    information = models.ArrayField(models.CharField())
    link_name = models.CharField(max_length=200)

    linksArray = models.ArrayField(models.URLField())
    linksNameArray = models.ArrayField(models.CharField())

class Guwahati_Airport(models.Model):
    link = models.URLField(max_length=400)
    
    information = models.ArrayField(models.CharField())
    
    link_name = models.CharField(max_length=200)
    
    linksArray = models.ArrayField(models.URLField())
    
    linksNameArray = models.ArrayField(models.CharField())


class Hotels_and_Cabs(models.Model):
    link = models.URLField(max_length=400)
    information = models.ArrayField(models.CharField())
    link_name = models.CharField(max_length=200)

    linksArray = models.ArrayField(models.URLField())
    linksNameArray = models.ArrayField(models.CharField())


class QuickLinks(models.Model):
    Quick_link_name = models.ArrayField(models.CharField(max_length=300))
    Quick_link_url = models.ArrayField(models.URLField(max_length=400))
    
class DownloadLinks(models.Model):
    Download_link_name = models.ArrayField(models.CharField(max_length=300))
    Download_link_url = models.ArrayField(models.URLField(max_length=400))