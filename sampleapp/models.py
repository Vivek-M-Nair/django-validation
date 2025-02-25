from django.db import models
class contact_for(models.Model):
    first_name=models.TextField(max_length=100)
    email=models.CharField(max_length=100)
    subject=models.CharField(max_length=200)
    message=models.CharField(max_length=600)

    
# Create your models here.
