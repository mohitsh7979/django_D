from django.shortcuts import render,HttpResponse
from .forms import resister_form



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