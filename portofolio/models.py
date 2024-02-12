from django.db import models


class Experience(models.Model):
    company_logo = models.ImageField(upload_to='images/')
    company_name = models.CharField(max_length=150)
    job_title = models.CharField(max_length=150)
    job_type = models.CharField(max_length=150)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    skills = models.JSONField()


class Project(models.Model):
    project_logo = models.ImageField(upload_to='images/')
    project_title = models.CharField(max_length=150)
    associated_to = models.CharField(max_length=150)
    project_type = models.CharField(max_length=150)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    skills = models.JSONField()


class Education(models.Model):
    institute_logo = models.ImageField(upload_to='images/')
    specialization = models.CharField(max_length=500)
    institute = models.CharField(max_length=150)
    gpa = models.CharField(max_length=10)
    graduation_date = models.DateField()

