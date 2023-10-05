from django.shortcuts import render

# Create your views here.


def set(request):
    request.session['name'] = 'Aman'
    return render(request,'set.html')


def get(request):
    data = request.session['name']
    return render(request,'get.html',{'data':data})

def delete(request):

    if 'name' in request.session:
        del request.session['name']

        return render(request,'del.html')
