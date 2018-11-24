from django import forms
from . import models

class FormSignUp(forms.ModelForm):
    class Meta():
        model = models.SignUp
        fields = ['username','email','password','re_password']
        widgets = {
        'password':forms.PasswordInput(),
        're_password':forms.PasswordInput()
        }

class FormLogIn(forms.ModelForm):
    class Meta():
        model = models.LogIn
        fields = ['username','password']
        widgets = {
        'password':forms.PasswordInput()
        }
