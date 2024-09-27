from django.forms import ModelForm
from django import forms
# from django.forms import Form
from .models import Product

class ProductForm(ModelForm):
    title = forms.CharField(max_length=10)
    class Meta:
        model = Product
        fields = '__all__' #('name' ,'price')
                           #exclude = ('')
    field_order=['title']
    



class LoginForm(forms.Form):
    name = forms.CharField(max_length=20)
    description = forms.CharField(max_length=50)


