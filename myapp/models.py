from django.db import models

# Create your models here.

from datetime import datetime





class Blog(models.Model):
    title=models.CharField(max_length=255, default='untitled')
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    image=models.ImageField(upload_to='uploads/', default='default.jpg') 
    def __str__(self):
        return self.title
