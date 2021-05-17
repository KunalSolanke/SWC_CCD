from django.db import models

# Create your models here.
class About(models.Model):
    about = models.CharField(max_length=100)

class campusrecruitment(models.Model):
    title = models.CharField(max_length=10)
    content1 = models.CharField
    content2 = models.CharField
    content3 = models.CharField

class acknowledgement(models.Model):
    title = models.CharField
    image = models.ImageField
    content = models.CharField