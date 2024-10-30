from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User




class userForm(models.Model):
    user = models.OneToOneField('auth.user', on_delete=models.CASCADE)
    fullname = models.CharField(max_length = 200)
    age = models.IntegerField(null = True)
    mobile = models.IntegerField(null = True)
    gender = models.CharField(max_length=10, null=True)
    disease = models.CharField(max_length=50, null=True)
    doctor = models.CharField(max_length=50, null=True)
   
    saved_time = models.DateTimeField(default=timezone.now)



class userFormnew(models.Model):
    user = models.OneToOneField('auth.user', on_delete=models.CASCADE)
    fullname = models.CharField(max_length = 200)
    department = models.CharField(max_length = 200,default="")
    mobile = models.IntegerField(null = True)

class DoctorUpload(models.Model):
    
    Patient_name = models.CharField(max_length = 200)
    profile=models.ImageField(upload_to='profile',default="")
    saved_time = models.DateTimeField(default=timezone.now)
    




   
    



class userFormadmin(models.Model):
    user = models.OneToOneField('auth.user', on_delete=models.CASCADE)   