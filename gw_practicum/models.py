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
class PracticumPlan(models.Model):
    title = models.CharField(max_length=255)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=False)
    competencies = models.TextField(null=False)
    l_obj1 = models.TextField(null=False)
    l_obj2 = models.TextField(null=True)
    l_obj3 = models.TextField(null=True)
    l_obj4 = models.TextField(null=True)
    l_obj5 = models.TextField(null=True)
    request_on = models.DateField(auto_now=False, auto_now_add=True)
    updated = models.DateField(auto_now=True, auto_now_add=False)
    agreement = models.BooleanField()
    preceptor_approval = models.BooleanField()
    pd_approval = models.BooleanField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=False)
    site = models.ForeignKey(Site, on_delete=models.CASCADE, null=False)
    preceptor = models.ForeignKey(Preceptor, on_delete=models.CASCADE, null=False)
    practicum_director = models.ForeignKey(PracticumDirector, on_delete=models.CASCADE, null=False)

"""
    MIDPOINT EVALUATION MODELS 
"""
class MidpointEvaluation(models.Model):
    competencies = models.TextField(null=False)
    l_obj1 = models.TextField(null=False)
    l_activities1 = models.TextField(null=False)
    l_activities2 = models.TextField(null=True)
    l_activities3 = models.TextField(null=True)
    l_activities4 = models.TextField(null=True)
    l_activities5 = models.TextField(null=True)
    agreement = models.BooleanField()
    request_on = models.DateField(auto_now=False, auto_now_add=True)
    updated = models.DateField(auto_now=True, auto_now_add=False)
    preceptor_approval = models.BooleanField()
    pd_approval = models.BooleanField()
    practicum_plan = models.ForeignKey(PracticumPlan, on_delete=models.CASCADE, null=False)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=False)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=False)
    site = models.ForeignKey(Site, on_delete=models.CASCADE, null=False)
    preceptor = models.ForeignKey(Preceptor, on_delete=models.CASCADE, null=False)
    practicum_director = models.ForeignKey(PracticumDirector, on_delete=models.CASCADE, null=False)

"""
    STUDENT SELF EVALUATION MODELS
"""
class StudentSelfEvaluation(models.Model):
    class Evals(models.IntegerChoices):
        EXCELLENT = 1
        GOOD = 2
        POOR = 3
        BAD = 4
    orientation = models.IntegerField(choices=Evals.choices)
    achievement = models.IntegerField(choices=Evals.choices)
    communication = models.IntegerField(choices=Evals.choices)
    feedback = models.IntegerField(choices=Evals.choices)
    discussion = models.IntegerField(choices=Evals.choices)
    l_objects = models.TextField(null=False)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=False)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=False)
    practicum_plan = models.ForeignKey(PracticumPlan, on_delete=models.CASCADE, null=False)
    site = models.ForeignKey(Site, on_delete=models.CASCADE, null=False)
    request_on = models.DateField(auto_now=False, auto_now_add=True)
    updated = models.DateField(auto_now=True, auto_now_add=False)

"""
    FINAL EVALUATION MODELS
"""
class PreceptorFinalEvaluation(models.Model):
    class Evals(models.IntegerChoices):
        EXCELLENT = 1
        GOOD = 2
        POOR = 3
        BAD = 4
    reliable = models.IntegerField(choices=Evals.choices)
    behavior = models.IntegerField(choices=Evals.choices)
    initiative = models.IntegerField(choices=Evals.choices)
    independent_work = models.IntegerField(choices=Evals.choices)
    projects = models.IntegerField(choices=Evals.choices)
    overall_work = models.TextField(null=False)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=False)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=False)
    practicum_plan = models.ForeignKey(PracticumPlan, on_delete=models.CASCADE, null=False)
    site = models.ForeignKey(Site, on_delete=models.CASCADE, null=False)
    preceptor = models.ForeignKey(Preceptor, on_delete=models.CASCADE, null=False)
    practicum_director = models.ForeignKey(PracticumDirector, on_delete=models.CASCADE, null=False)
    pd_approval = models.BooleanField()
    request_on = models.DateField(auto_now=False, auto_now_add=True)
    updated = models.DateField(auto_now=True, auto_now_add=False)