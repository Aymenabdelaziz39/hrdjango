from django.db import models
from users.models import User
# Create your models here.

class Industry(models.Model):
    category = models.CharField(max_length=255)

class Experience(models.Model):
    level = models.CharField(max_length=255)

class EducationLevel(models.Model):
    level = models.CharField(max_length=255)

class Wilaya(models.Model):
    name = models.CharField(max_length=255)

class JobPost(models.Model):
    hr = models.ForeignKey(User, on_delete=models.CASCADE, related_name="job_posts")
    job_title = models.CharField(max_length=255)
    job_description = models.TextField()
    wilaya = models.ForeignKey(Wilaya, on_delete=models.CASCADE)
    industry = models.ForeignKey(Industry, on_delete=models.CASCADE)
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE)
    education_level = models.ForeignKey(EducationLevel, on_delete=models.CASCADE)
    employment_type = models.CharField(max_length=20, choices=[('Full-time', 'Full-time'), ('Part-time', 'Part-time'), ('Contract', 'Contract')])
    salary_range_min = models.IntegerField(null=True, blank=True)
    salary_range_max = models.IntegerField(null=True, blank=True)
    requirements = models.TextField()
    application_deadline = models.DateField()
    date_posted = models.DateTimeField(auto_now_add=True)

class Application(models.Model):
    job_post = models.ForeignKey(JobPost, on_delete=models.CASCADE, related_name="applications")
    job_seeker = models.ForeignKey(User, on_delete=models.CASCADE, related_name="applications")
    evaluation_mark = models.IntegerField(null=True, blank=True)
    feedback = models.TextField(null=True, blank=True)
    application_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected')], default='Pending')
