from django.shortcuts import render
from .forms import LoginForm
# def login(request):
#     form  = LoginForm()
#     return render(request,'accounts/login.html',{'form':form})




from django.contrib.auth import logout,login,authenticate
from django.views import View
from django.shortcuts import redirect
from .forms import *
from django.contrib.auth.models import User
class Login(View):
    def get(self,request):
        login_form = LoginForm()
        context = {
            'login_form': login_form
        }
        return render(request,'accounts/login.html',context)
    def post(self,request):
        pass

class Register(View):
    def get(self,request):
        user_form = UserRegisterForm()
        customer_form = CustomerRegisterForm()
        context = {
            'user_form':user_form,
            'customer_form': customer_form
        }
        return render(request,'accounts/register.html',context)

    def post(self,request):
        user_form = UserRegisterForm(request.POST)
        customer_form = CustomerRegisterForm(request.POST)
        if user_form.is_valid() and customer_form.is_valid():
            user = user_form.save()
            customer = customer_form.save(commit=False)
            customer.user = user
            customer.save()
            login(request,user)
            return redirect('/')
        #     username = user_form.cleaned_data['username']
        #     first_name = user_form.cleaned_data['first_name']
        #     last_name = user_form.cleaned_data['last_name']
        #     email = user_form.cleaned_data['email']
        #     password = user_form.cleaned_data['password']
        #     user =User.objects.create_user(
        #         username=username,
        #         email = email,
        #         first_name = first_name,
        #         last_name = last_name,
        #         password= password,
        #     )
        return redirect('/')


def logout_customer(request):
    logout(request)
    return redirect('/')