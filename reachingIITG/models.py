from django.db import models

# Create your models here.

class Location(models.Model):
    link_name = models.URLField(max_length=400)
    information = models.TextField(max_length=1000)

class Connectivity(models.Model):
    link_name = models.URLField(max_length=400)
    information = models.TextField(max_length=1000)

class Guwahati_Airport(models.Model):
    link_name = models.URLField(max_length=400)
    information = models.TextField(max_length=1000)

class Hotels_and_Cabs(models.Model):
    link_name1 = models.URLField(max_length=400)
    information = models.TextField(max_length=1000)
    link_name_redirect = models.URLField(max_length=400)

class QuickLinks(models.Model):
    Quick_link_name = models.CharField(max_length=300)
    Quick_link_url = models.URLField(max_length=400)
    
class DownloadLinks(models.Model):
    Download_link_name = models.CharField(max_length=300)
    Download_link_url = models.URLField(max_length=400)