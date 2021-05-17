from django.db import models
#from django.contrib.postgres.fields import ArrayField
# Create your models here.

#Head of the Centre

class Head_of_center(models.Model):
    photo_head = models.ImageField(upload_to='img')
    text_head = models.CharField(max_length=500)
    #points =models.ArrayField(models.CharField(max_length=2000))
    points_text = models.CharField(max_length=6000)

#Faculty members/coordinators

class Faculty_members(models.Model):
    photo_head = models.ImageField(upload_to='img')
    text_head = models.CharField(max_length=500)
    former_text = models.CharField(max_length=2000)

class Department_reps(models.Model):    
    department = models.CharField(max_length=200)
    points_text = models.CharField(max_length=6000)

#ccd-office

class Ccd_office(models.Model):
    title = models.CharField(max_length=200)
    points_text = models.CharField(max_length=5000)
    photo_head = models.ImageField(upload_to='img')
    text_head = models.CharField(max_length=500)

#Student Coordinators

class Contacts(models.Model):
    topic = models.CharField(max_length=100)
    email = models.URLField(max_length=100)

class Placement_coordinators(models.Model):
    photo_coord = models.ImageField(upload_to='img')
    text_coord = models.CharField(max_length=500)

class Intern_coordinators(models.Model):
    text_coord = models.CharField(max_length=500)


#iitg directory : iitg.ac.in/phones no models relevant

    
    
