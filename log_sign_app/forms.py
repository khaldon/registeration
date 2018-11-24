from django import forms
from . import models

class FormSignUp(forms.ModelForm):
    class Meta():
        model = models.SignUp
        fields = ['username','email','password','re_password']
