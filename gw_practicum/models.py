from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    first_name = models.CharField(max_length=128)
    middle_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.CharField(max_length=128)

    def __str__(self):
        return self.username

class Department(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Major(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class DegreeLevel(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class PracticumDirector(models.Model):
    user_data = models.ForeignKey(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

class Site(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip = models.IntegerField()

    def __str__(self):
        return self.name

class Preceptor(models.Model):
    user_data = models.ForeignKey(User, on_delete=models.CASCADE)
    site = models.ForeignKey(Site, on_delete=models.CASCADE, null=True)
    profile = models.TextField()
    phone = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.user_data.username

class Student(models.Model):
    user_data = models.ForeignKey(User, on_delete=models.CASCADE)
    gwid = models.CharField(max_length=120)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    degree = models.ForeignKey(DegreeLevel, on_delete=models.CASCADE)
    major = models.ForeignKey(Major, on_delete=models.CASCADE)

    def __str__(self):
        return self.user_data.username

"""
    PRACTICUM PLAN MODELS 
"""

"""
    MIDPOINT EVALUATION MODELS 
"""

"""
    FINAL EVALUATION MODELS
"""
