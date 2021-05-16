from django.db import models

# Create your models here.
class FAQ(models.Model):
    question = models.CharField(max_length=500)
    text = models.TextField(max_length=5000)    