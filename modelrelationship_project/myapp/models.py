from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class product(models.Model):
    title = models.CharField(max_length=20)
    price = models.IntegerField()
    description = models.TextField(max_length=300)

    def __str__(self):
        return self.title

 
class Add_to_cart(models.Model):
    # user = models.OneToOneField(User,on_delete=models.PROTECT)
    user = models.ManyToManyField(User)
    product = models.ManyToManyField(product)
    # product = models.OneToOneField(product,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    
   
