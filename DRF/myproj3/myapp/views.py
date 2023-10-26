from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from myapp.serializers import StudentSerializer
from .models import student

# Create your views here.



@api_view(['GET','POST','DELETE'])
def index(request):
    
    if request.method == 'GET':

        data = student.objects.all()
        serializer_data = StudentSerializer(data,many=True)
        return Response(serializer_data.data)

    elif request.method == 'POST':

        data  = request.data 
        serializer_data = StudentSerializer(data=data)

        if serializer_data.is_valid():
            serializer_data.save()
            return Response(serializer_data.data)
        
    elif request.method == 'DELETE':

        data_id = request.data['id']

        obj_data = student.objects.get(id=data_id) 
        obj_data.delete()
        return Response({'message':'data deleted'})



        
