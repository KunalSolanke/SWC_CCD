from django.db import models

# Create your models here.
class contents(models.Model):
    title = models.CharField(max_length=10)
    description = models.CharField(max_length=100)
    link = models.URLField(max_length=40)