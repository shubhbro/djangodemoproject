from django.db import models
from django.contrib.auth.models import User

# Create your models here

class Patient(models.Model):
    def __str__(self):
        return self.name
    name = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    age = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

class Doctor(models.Model):
    def __str__(self):
        return self.name
    name = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    age = models.CharField(max_length=200)
    specialist = models.CharField(max_length=200)
    
