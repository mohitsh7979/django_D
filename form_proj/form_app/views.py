from django.shortcuts import render,HttpResponse,redirect
from .models import  details,student_details
from .forms import Student_form

# Create your views here.


def form_output(request):

    if request.method == "POST":

        a = Student_form(request.POST,request.FILES)
        print('a>>>>>>>>>',a)

        if a.is_valid():
            a.save()

            return HttpResponse('Data Saved !!')

    a = Student_form(label_suffix=':')
    # a.order_fields(field_order=['email','name','image','roll_no'])
    context = {

        'a':a
    }

    return render(request,'form.html',context)


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



def data(request):

    details(name="Ankit",email='ankit@gmail.com',descripation='this my page',image='abc').save()
    

