from django.db import models
class contact(models.Model):
    firstname=models.CharField(max_length=255)
    timestamp=models.DateTimeField()
    
# Create your models here.
