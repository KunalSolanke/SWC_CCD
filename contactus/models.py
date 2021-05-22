from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.

#Head of the Centre

class Head_of_center(models.Model):
    photo_head = models.ImageField(upload_to='img')
    name = models.CharField(max_length=200,default=" ")
    creds = models.CharField(max_length=200,default=" ")
    designation = models.CharField(max_length=200,default=" ")
    email = ArrayField(models.URLField(max_length=100, blank=True),default=list)
    phone = ArrayField(models.CharField(max_length=100, blank=True),default=list) 
    homepage = models.URLField(max_length=100,default=" ")
    former_heads =ArrayField(models.CharField(max_length=1000, blank=True),default=list)

#Faculty members/coordinators

class Faculty_members(models.Model):
    photo_head = models.ImageField(upload_to='img')
    name = models.CharField(max_length=200,default=" ")
    role = models.CharField(max_length=200,default=" ")
    designation = models.CharField(max_length=200,default=" ")
    email = ArrayField(models.URLField(max_length=100, blank=True),default=list)
    phone = ArrayField(models.CharField(max_length=100, blank=True),default=list)
    homepage = models.URLField(max_length=100,default=" ")
    former_coords =ArrayField(models.CharField(max_length=1000, blank=True),default=list)

class Department_reps(models.Model):    
    department = models.CharField(max_length=200,default=" ")
    name = models.CharField(max_length=200,default=" ")
    email = ArrayField(models.URLField(max_length=100, blank=True),default=list)
    homepage1 = models.URLField(max_length=100,default=" ")

#ccd-office

class Ccd_office_cont(models.Model):
    address=models.CharField(max_length=2000,default=" ")
    email = ArrayField(models.URLField(max_length=100, blank=True),default=list)

class Admin_staff(models.Model):    
    photo_head = models.ImageField(upload_to='img')
    name = models.CharField(max_length=200,default=" ")
    role = models.CharField(max_length=200,default=" ")
    email = ArrayField(models.URLField(max_length=100, blank=True),default=list)
    phone = models.CharField(max_length=200,default=" ")

#Student Coordinators

class Contacts(models.Model):
    topic = models.CharField(max_length=100,default=" ") #redundant maybe
    email = ArrayField(models.URLField(max_length=100, blank=True),default=list)
    linkedin = ArrayField(models.URLField(max_length=100, blank=True),default=list)#maybe not arrayfield

class Placement_coordinators(models.Model):
    photo_coord = models.ImageField(upload_to='img')
    name = models.CharField(max_length=200,default=" ")
    mobile = models.CharField(max_length=100,default=" ")
    areas = ArrayField(models.CharField(max_length=100, blank=True),default=list)

class Intern_coordinators(models.Model):
    name = models.CharField(max_length=200,default=" ")
    department = models.CharField(max_length=200,default=" ")


#iitg directory : iitg.ac.in/phones no models relevant

    
    
