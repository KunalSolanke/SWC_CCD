from django.db import models

# Create your models here.
#About IITG ..............................

class About_IITG(models.Model):
    intro_text = models.CharField(max_length=1500)
    About_IITG_photo = models.ImageField(upload_to='img')

#Academics ...............................

class academicsintro(models.Model):
    intro_text = models.CharField(max_length=1500)

class UG_programme(models.Model):
    name_of_programme = models.CharField(max_length=200)
    points_text = models.CharField(max_length=800)

class PG_programme(models.Model):
    name_of_programme = models.CharField(max_length=200)
    points_text = models.CharField(max_length=800)


#Graduating Students .........................

class UG_data(models.Model):
    title = models.CharField(max_length=200)
    data_photo1 = models.ImageField(upload_to='img',blank=True, null=True)
    data_photo_2 = models.ImageField(upload_to='img',blank=True, null=True)

class PG_data(models.Model):
    title = models.CharField(max_length=200)
    data_photo_1 = models.ImageField(upload_to='img',blank=True, null=True)
    data_photo_2 = models.ImageField(upload_to='img',blank=True, null=True)

#Research and Development ......................

class R_and_D(models.Model):
    title = models.CharField(max_length=200)
    points_text = models.CharField(max_length=2800)

#Achievements ....................................

class Achievements(models.Model):
    title = models.CharField(max_length=200)
    points_text = models.CharField(max_length=5800)
    

     
     







