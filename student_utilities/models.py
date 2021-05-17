from django.db import models

# Create your models here.

#master-cv

class UG_programme(models.Model):
    title = models.CharField(max_length=100)
    points_text = models.CharField(max_length=500)
    buttons = models.CharField(max_length=100)
