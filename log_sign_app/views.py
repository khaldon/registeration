from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')

def sign_up(request):
    return render(request,'sign_up/sign_up.html')


def log_in(request):
    return render(request,'log_in/log_in.html')
