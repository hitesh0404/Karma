from django.shortcuts import render
# def login(request):
#     form  = LoginForm()
#     return render(request,'accounts/login.html',{'form':form})




from django.contrib.auth import logout,login,authenticate
from django.views import View
from django.shortcuts import redirect
from .forms import *
from django.contrib.auth.models import User
from django.contrib import messages
from cart.models import Cart
class Login(View):
    def get(self,request):
        return render(request,'accounts/login.html')
    def post(self,request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        next_url = request.GET.get('next', '/')
        user  = authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            messages.success(request,'Login Successfully Done')
            count =Cart.objects.filter(user = user).count() 
            request.session['cart_item_count'] = count
            
            return redirect(next_url)
        
        else:
            return redirect('login')

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
            user =User.objects.create_user(
                                            username = user_form.cleaned_data['username'],
                                            first_name = user_form.cleaned_data['first_name'],
                                            last_name = user_form.cleaned_data['last_name'],
                                            email = user_form.cleaned_data['email'],
                                            password = user_form.cleaned_data['password'],
                                        )
            customer = customer_form.save(commit=False)
            customer.user = user
            customer.save()
            login(request,user)
            return redirect('/')   
        context = {
            'user_form':user_form,
            'customer_form': customer_form
        }
        return render(request,'accounts/register.html',context)


def logout_customer(request):
    logout(request)
    return redirect('/')