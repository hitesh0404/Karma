from django.shortcuts import render
from .forms import LoginForm

def login(request):
    form  = LoginForm()
    return render(request,'accounts/login.html',{'form':form})