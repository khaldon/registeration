from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import FormSignUp
# Create your views here.

def index(request):
    return render(request,'index.html')

def get_sign_up(request):
    if request.method == 'Post':
        form = FormSignUp(method.POST)
        if form.is_valid():
            username    = form.cleaned_data['username']
            email       = form.cleaned_data['email']
            password    = form.cleaned_data['password']
            re_password = form.cleaned_data['re_password']
            print(username,email,password,re_password)
    else:
        form = FormSignUp()
    return render(request,'sign_up/sign_up.html',{'form':form})


def log_in(request):
    return render(request,'log_in/log_in.html')
