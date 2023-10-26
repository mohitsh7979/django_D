from django.shortcuts import render

# Create your views here.


def setCookie(request):
    response = render(request,'setCookie.html')
    response.set_cookie('name','Rohit',max_age=30)
   
    return response

def getCookie(request):
    # name = request.COOKIES['name']
    name = request.COOKIES.get('name' ,'Guest')
    return render(request,'getCookie.html',{'name':name})


def delCookie(request):
    response = render(request,'deleteCookie.html')
    response.delete_cookie('name')
    return response