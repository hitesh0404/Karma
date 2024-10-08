from django import forms
from django.forms import ModelForm
from .models import Customer
class CustomerRegisterForm(ModelForm):
    class Meta:
        model = Customer
        exclude = 'user'
class UserRegisterForm(ModelForm):
    class Meta:
        model = Customer
        exclude = 'user'



class LoginForm(forms.Form):
    username = forms.CharField(max_length=25)
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password  =forms.CharField(widget=forms.PasswordInput(attrs = {'placeholder':'password'}))