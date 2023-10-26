from django.db import models

# Create your models here.


class student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    city = models.CharField(max_length=50)
    mobile_no = models.CharField(max_length=10)
    
