from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    is_hr = models.BooleanField(default=False)
    is_job_seeker = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')], null=True, blank=True)

    # related_name for groups and user_permissions
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='user_set_groups',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='user_set_permissions',
        blank=True
    )

class HRProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="hr_profile")
    company_name = models.CharField(max_length=100)
    company_website = models.URLField(null=True, blank=True)
    company_location = models.CharField(max_length=100, null=True, blank=True)
    company_size = models.IntegerField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
