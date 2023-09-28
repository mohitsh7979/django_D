from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import Profile_obj
from .helpers import send_forget_password_mail
# Create your views here.


def create_account(request):
    if request.method == "POST":

        uname = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2= request.POST['password2']

        if User.objects.filter(username=uname).first():
            messages.success(request,'username already taken')

        elif User.objects.filter(email=email).first():
            messages.success(request,'email is already taken')
        
        elif password1!=password2:
            messages.success(request,'Both field are should be same')
        
        else:
            user = User(username=uname,first_name=first_name,last_name=last_name,email=email)
            user.set_password(password1)
            user.save()
            messages.success(request,'Account successfully created !!!')
            

        print(uname,first_name,last_name,email,password1,password2)

    return render(request,'regeister.html')


def loginhandle(request):
    if request.method == "POST":
        uname = request.POST['username']
        upass = request.POST['password']
        print(uname,upass)

        user_obj = User.objects.filter(username=uname).first()
        user = authenticate(username = uname,password =upass)
        print(user_obj)
        if not uname or not upass:
            messages.success(request,'Both field are required')
        
        elif user_obj is None:
            messages.success(request,'user not found !!')

        elif user is not None:
            login(request,user)
            return render(request,'index.html')
        
        else:
            messages.success(request,'wrong password !!!')
            

        
    return render(request,'login.html')


def logouthandle(request):
    logout(request)
    return redirect('/signup/')


import uuid
def forgetpassword(request):
    if request.method == "POST":
        uname = request.POST['username']
        user = User.objects.filter(username=uname).first()

        if user is None:
            messages.success(request,'user not found')

        else:
            user_obj = User.objects.get(username=uname)
            print(user_obj)
            token = str(uuid.uuid4())
            print(token)
            profile_obj = Profile_obj(user=user_obj,token=token)
            profile_obj.save()
            send_forget_password_mail(user_obj.email,token)
            messages.success(request,'Message sent')
            return redirect('/forget-password/')



    return render(request,'forget_password.html')


def changepassword(request,token):
    
    if request.method == "POST":
        new_password = request.POST['new_password']
        confirm_password = request.POST['re-confirm_password']
        user_id = request.POST['user_id']

        if user_id is None:
            messages.success(request,'No user id found')
            return redirect(f'/change-password/{token}/')
        
        if new_password != confirm_password:
            messages.success(request,'both should be equal')
            return redirect(f'/change-password/{token}/')
        
        user_obj = User.objects.get(id=user_id)
        user_obj.set_password(new_password)
        user_obj.save()
        return redirect('/login/')
        
    

    profile_obj = Profile_obj.objects.filter(token=token).first()
    context = {

        'user_id':profile_obj.user.id
    }
    return render(request,'change_password.html',context)
