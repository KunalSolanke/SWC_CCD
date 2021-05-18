from django.db import models

# Create your models here.
class About(models.Model):
    about = models.CharField(max_length=100)

class campusrecruitment(models.Model):
    title = models.CharField(max_length=10)
    content1 = models.CharField(max_length=100)
    content2 = models.CharField(max_length=100)
    content3 = models.CharField(max_length=100)

class acknowledgement(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='img',max_length=100)
    content = models.CharField(max_length=100)