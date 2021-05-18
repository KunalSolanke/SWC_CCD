from django.db import models

# Create your models here.


class Facilities(models.Model):
    image = models.ImageField(upload_to='img')
    description = models.TextField(max_length=1000)
    

class QuickLinks(models.Model):
    Quick_link_name = models.CharField(max_length=300)
    Quick_link_url = models.URLField(max_length=400)
    
class DownloadLinks(models.Model):
    Download_link_name = models.CharField(max_length=300)
    Download_link_url = models.URLField(max_length=400)