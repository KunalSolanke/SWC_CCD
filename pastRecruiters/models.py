from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class PastRecruiters(models.Model):
    name = models.CharField(max_length=300)
    links = models.URLField(max_length=400)
    description = models.TextField(max_length=1000)
    names_of_companies = ArrayField(models.CharField(max_length=2000))
    