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
