from django import forms
from django.forms import ModelForm
from .models import Customer,Address
from django.contrib.auth.models import User
class CustomerRegisterForm(ModelForm):
    class Meta:
        model = Customer
        exclude = ['user']
class UserRegisterForm(ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs = {'placeholder':'confirm password'}))
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password']
    field_order = [ 'first_name','last_name','email','username','password','confirm_password']
class AddressForm(ModelForm):
    class Meta:
        model = Address
        exclude = ['user']
# class LoginForm(forms.Form):
#     username = forms.CharField(max_length=25)
#     password = forms.CharField(widget=forms.PasswordInput(attrs = {'placeholder':'password'}))
    