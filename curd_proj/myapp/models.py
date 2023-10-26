from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Curd_model(models.Model):
    
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    roll_no = models.IntegerField(blank=True,null= True)
    date = models.DateField() 
