from django.db import models

# Create your models here.

class LessorDetails(models.Model):
    First_Name = models.CharField(max_length=20)
    Last_Name = models.CharField(max_length=20)
    Email = models.EmailField()
    Phone_No = models.CharField(max_length=10)
    Country = models.CharField(max_length=30)
    State = models.CharField(max_length=30)
    City = models.CharField(max_length=30)
    Username = models.CharField(max_length=20)
    Password = models.CharField(max_length=20)

class LesseeDetails(models.Model):
    First_Name = models.CharField(max_length=20)
    Last_Name = models.CharField(max_length=20)
    Email = models.EmailField()
    Phone_No = models.CharField(max_length=10)
    Company = models.CharField(max_length=50)
    Country = models.CharField(max_length=30)
    State = models.CharField(max_length=30)
    City = models.CharField(max_length=30)
    Username = models.CharField(max_length=20)
    Password = models.CharField(max_length=20)
