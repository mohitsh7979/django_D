from django.shortcuts import render,HttpResponse,redirect
from .forms import resister_form,login_form
from django.contrib.auth import authenticate,login,logout





# Create your views here.



def create_account(request):

    if request.method == "POST":
        data = resister_form(request.POST)
        if data.is_valid():
            data.save()
            return HttpResponse('Account Successfully created !!!')
            

    data = resister_form()
    context = {

        'data':data
    }
    return render(request,'auth_app/register.html',context)



def login_account(request):
    if request.method == "POST":
        data = login_form(data=request.POST)
        if data.is_valid():
            uname = data.cleaned_data['username']
            passw = data.cleaned_data['password']
            print(uname,passw)
            user = authenticate(username=uname,password=passw)
            print(user,'>>>>>>user')

            if user is not None:
                login(request,user)
                return redirect('/output/')

        
    data = login_form()
    context = {
        'data':data
    }
    return render(request,'auth_app/login.html',context)