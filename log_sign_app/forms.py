from django import forms
from django.contrib.auth.models import User
from . models import UserModelProfile

class UserForm(forms.ModelForm):
    class Meta():
        model = User
        fields = ['username','email','password']
        widgets = {
        'password':forms.PasswordInput(),
        }

class UserModelProfileForm(forms.ModelForm):
    class Meta():
        model = UserModelProfile
        fields = ['portfolio_site','portfile_pic']
    
