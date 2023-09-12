from django.shortcuts import render,HttpResponse
from .models import  details

# Create your views here.


def form_output(request):
    return render(request,'form.html')


def take_data(request):
    
    if request.method == "POST":

        user_name = request.POST['username']
        user_email = request.POST['user_email']
        user_desc = request.POST['descripation']
        
        details(name=user_name,email=user_email,descripation=user_desc).save()
  
        print(user_name,user_email,user_desc)

        return HttpResponse('Your data Saved')
    
