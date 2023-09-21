from django.contrib import admin
from django.urls import path,include
from auth_app import views


urlpatterns = [

    path('create_account/',views.create_account),
 
    
]