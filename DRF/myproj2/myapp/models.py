from django.db import models

# Create your models here.



class Teacher(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    subject = models.CharField(max_length=40)
    