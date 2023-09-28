from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Profile_obj(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    token = models.CharField(max_length=100)
    data = models.DateTimeField(auto_now_add=True)
