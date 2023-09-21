from django.db import models

# Create your models here.


class details(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    descripation = models.CharField(max_length=300)
    date = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='media')

CITY_CHOICE = (

    ('jaipur','Jaipur'),
    ('udaipur','Udaipur'),
    ('kota','Kota'),
    ('jodhpur','Jodhpur')
)


class student_details(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    mobile_no = models.CharField(max_length=10)
    roll_no = models.IntegerField()
    city = models.CharField(choices=CITY_CHOICE,max_length=50,null=True,blank=True)
    image = models.ImageField()


    def __str__(self):
        return self.name




