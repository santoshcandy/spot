from django.db import models

class Plumber(models.Model):
    Name = models.CharField(max_length=100)
    Location = models.CharField(max_length=100)
    Phone = models.CharField(max_length=15)
    Service = models.TextField(max_length=100)
    message=models.TextField(max_length=300)
    Datetime= models.DateTimeField(auto_now_add=True)
# Create your models here.
