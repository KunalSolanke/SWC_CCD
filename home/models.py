from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class About(models.Model):
    about = models.CharField(max_length=100)

class Campusrecruitment(models.Model):
    title = models.CharField(max_length=50)
    content = ArrayField(models.CharField(max_length=100),max_length=4)
    # content1 = models.CharField(max_length=100)
    # content2 = models.CharField(max_length=100)
    # content3 = models.CharField(max_length=100)

class Acknowledgement(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='img',max_length=100)
    content = models.CharField(max_length=1000)
    link = models.URLField(max_length=100)