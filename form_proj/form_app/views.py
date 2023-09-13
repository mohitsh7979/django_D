from django.shortcuts import render,HttpResponse,redirect
from .models import  details

# Create your views here.


def form_output(request):

    return render(request,'form.html')


def take_data(request):
    
    if request.method == "POST":

        user_name = request.POST['username']
        user_email = request.POST['user_email']
        user_desc = request.POST['descripation']
        user_image = request.FILES['user_image']

        
        details(name=user_name,email=user_email,descripation=user_desc,image=user_image).save()
  
        print(user_name,user_email,user_desc)

        return redirect('/data_output/')
    

def data_output(request):
    data = details.objects.all()
    context = {
       'data':data
    }
    return render(request,'data.html',context)
    
