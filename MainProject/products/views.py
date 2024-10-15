from django.shortcuts import render,redirect,get_object_or_404
from django.views import View
from .forms import ProductForm
from .models import Product

class AddProduct(View):
    def get(self,request):
        form = ProductForm()
        return render(request,'products/add_product.html',{'form':form})
    def post(self,request):
        form = ProductForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return render(request,'products/add_product.html',{'form':form})


class UpdateProduct(View):
    def get(self,request,id):
        product = get_object_or_404(Product,id=id)
        # product = Product.objects.get(id=id)
        if product:
            form = ProductForm(instance=product)
            return render(request,'products/update_product.html',{'form':form})
    def post(self,request,id):
        product = get_object_or_404(Product,id=id)
        form = ProductForm(request.POST,request.FILES,instance=product)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            # form = ProductForm(request.POST)
            return render(request,'products/update_product.html',{'form':form})


def show_product(request):
    products = Product.objects.all()
    context ={
        'products':products,
    }
    return render(request,'products/show_product.html',context)