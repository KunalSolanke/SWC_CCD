from django.db import models

# Create your models here.
class Contents(models.Model):
    title = models.CharField(max_length=100,default=" ")
    description = models.CharField(max_length=1000,default=" ")
    link = models.URLField(max_length=100,default=" ")