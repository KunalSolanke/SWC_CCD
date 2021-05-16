from django.db import models

# Create your models here.

#Head of the Centre

class head_of_center(models.Model):
    photo_head = models.ImageField(upload_to='img')
    text_head = models.CharField(max_length=500)
    points_text = models.CharField(max_length=6000)

#Faculty members/coordinators

class faculty_members(models.Model):
    photo_head = models.ImageField(upload_to='img')
    text_head = models.CharField(max_length=500)
    former_text = models.CharField(max_length=2000)

class department_reps(models.Model):    
    department = models.CharField(max_length=200)
    points_text = models.CharField(max_length=6000)

#ccd-office

class ccd_office(models.Model):
    title = models.CharField(max_length=200)
    points_text = models.CharField(max_length=5000)
    photo_head = models.ImageField(upload_to='img')
    text_head = models.CharField(max_length=500)

#Student Coordinators

class placement_coordinators(models.Model):
    contact_det = models.CharField(max_length=500)
    photo_coord = models.ImageField(upload_to='img')
    text_coord = models.CharField(max_length=500)

class intern_coordinators(models.Model):
    text_coord = models.CharField(max_length=500)


#iitg directory : iitg.ac.in/phones no models relevant

    
    
