from django.db import models
from users.models import User
# Create your models here.

class UploadedFile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='files')
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
