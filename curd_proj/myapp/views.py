from django.shortcuts import render,redirect
from .forms import Curd_Form
from django.contrib import messages
from .models import Curd_model
# Create your views here.


def curd_view(request):
    
    if request.method == "POST":

        a = Curd_Form(request.POST)

        if a.is_valid():

            a.save()
            messages.success(request,'date saved')


    a = Curd_Form()
    data = Curd_model.objects.all()
    return render(request,'create.html',{'a':a,'data':data})

            

def delete(request,id):
    delete_data = Curd_model.objects.get(id=id)
    delete_data.delete()
    messages.success(request,'data deleted')
    return redirect('/')

def update(request,id):

    if request.method == "POST":

        form_data = Curd_model.objects.get(id=id)
        form = Curd_Form(request.POST,instance = form_data)

        if form.is_valid():
            form.save()
            messages.success(request,'Data updated !')
            return redirect('/')

    form_data = Curd_model.objects.get(id=id)
    form = Curd_Form(instance=form_data)
    return render(request,'update.html',{'form':form})

    
        


