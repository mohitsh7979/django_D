from django.shortcuts import render,HttpResponse

# Create your views here.



def index(request,no):
    
    if no%2 ==0:
      return HttpResponse('even')
    
    else:
       return HttpResponse('odd')



def output(request):
    return render(request,'index.html')
