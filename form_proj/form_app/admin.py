from django.contrib import admin
from .models import details,student_details

# Register your models here.


@admin.register(details)

class DetailAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','descripation','date','image']


admin.site.register(student_details)




