from django import forms
from .models import Curd_model  

class Curd_Form(forms.ModelForm):

    class Meta:

        model = Curd_model
        fields = ('__all__')