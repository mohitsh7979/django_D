from django import forms 
from .models import student_details
# from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

class Student_form(forms.ModelForm):

    class Meta:

        model = student_details
        fields = ('__all__')
        labels = {

            'name':'Enter Your Name'
        }
        widgets = {

            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'username'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Your email'}),
            'mobile_no':forms.TextInput(attrs={'class':'form-control','placeholder':'Mobile No'}),
            'roll_no':forms.TextInput(attrs={'class':'form-control','placeholder':'roll no'}),
            'image':forms.FileInput(attrs={'class':'form-control'}),
            'city':forms.Select(attrs={'class':'form-control'})
        }






