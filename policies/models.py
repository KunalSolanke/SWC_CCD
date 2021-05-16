from django.db import models

# Create your models here.
class Internship_policy(models.Model):
    text = models.TextField(max_length=2000)


class placement_policy(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(max_length=5000)