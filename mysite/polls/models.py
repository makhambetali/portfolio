from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    image = models.ImageField(upload_to ='uploads/')
    date = models.DateTimeField(auto_now_add=True)

class Request(models.Model):
    name = models.CharField(max_length=20)
    message = models.TextField()
    email = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)