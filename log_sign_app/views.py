from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.hashers import make_password
from . import forms
from . import models
# Create your views here.

def index(request):
    return render(request,'index.html')

def get_sign_up(request):
    if request.method == 'POST':
        form = forms.FormSignUp(request.POST)
        if form.is_valid():
            username    = form.cleaned_data['username']
            email       = form.cleaned_data['email']
            password    = form.cleaned_data['password']
            re_password = form.cleaned_data['re_password']
            make_password(password)
            form.save()

    else:
        form = forms.FormSignUp()
    return render(request,'sign_up/sign_up.html',{'form':form})


def log_in(request):

    if request.method == 'POST':
        form = forms.FormLogIn(request.POST)
        if form.is_valid():
            username    = form.cleaned_data['username']
            password    = form.cleaned_data['password']
            data_get    = models.SignUp.objects.order_by('username')
            for i in data_get:
                if i.username == username and i.password == password:
                    print("HEllo word")
                else:
                    print("Error in user")
    else:
        form = forms.FormLogIn()
    return render(request,'log_in/log_in.html',{'form':form})
