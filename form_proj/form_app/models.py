from django.db import models

# Create your models here.


class details(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    descripation = models.CharField(max_length=300)
    date = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='media')



