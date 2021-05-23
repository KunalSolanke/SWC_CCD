from django.db import models

# Create your models here.
class Policy(models.Model):
    title = models.CharField(max_length=200,default="")
    text = models.TextField(max_length=5000)
    link= models.URLField(max_length=400,null=True)
    file = models.FileField(null=True,upload_to="policies/")


