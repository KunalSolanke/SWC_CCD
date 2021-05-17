from django.db import models

# Create your models here.
class contents(models.Model):
    title = models.CharField
    description = models.CharField(max_length=100)