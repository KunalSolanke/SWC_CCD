from django.db import models

# Create your models here.
class QuickLinks(models.Model):
    name = models.CharField(max_length=300)
    link_name = models.URLField(max_length=500)


class DownloadLinks(models.Model):
    name = models.CharField(max_length=300)
    link_name = models.URLField(max_length=500)
