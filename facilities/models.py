from django.db import models

# Create your models here.


class Facilities(models.Model):
    image = models.ImageField(upload_to='img')
    description = models.TextField(max_length=1000)
    
