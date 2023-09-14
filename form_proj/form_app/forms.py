from django import forms 


class Student_form(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    mobile_no = forms.CharField(max_length=10)
    roll_no = forms.IntegerField()
    image = forms.ImageField()
