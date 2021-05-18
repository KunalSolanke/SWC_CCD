from django.db import models

# Create your models here.

class PastRecruiters(models.Model):
    name = models.CharField(max_length=300)

class QuickLinks(models.Model):
    Quick_link_name = models.CharField(max_length=300)
    Quick_link_url = models.URLField(max_length=400)
    
class DownloadLinks(models.Model):
    Download_link_name = models.CharField(max_length=300)
    Download_link_url = models.URLField(max_length=400)