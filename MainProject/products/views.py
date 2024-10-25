from django.shortcuts import render,redirect,get_object_or_404
from django.views import View
from .forms import ProductForm
from .models import Product,ShoeCategory,Shoe
from django.db.models import Q
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

def search_products(search):
    products = Product.objects.filter(name__icontains = search)
    if not products.exists():
        products = Product.objects.filter(description__icontains = search)
    return products


def show_product(request):
    search = request.GET.get('search')
    if search:
        products = search_products(search)
    else:
        products = Product.objects.all()
    shoe_category = ShoeCategory.objects.all() 
    context ={
        'products':products,
        'category':shoe_category,
    }
    return render(request,'products/show_product.html',context)


def sort_by_category(request,name):
    cat = ShoeCategory.objects.get(name=name)
    shoecategoryshoe = cat.shoecategoryshoe_set.all()
    products = [product.shoe.product for product in shoecategoryshoe]
    print(products)
    shoe_category = ShoeCategory.objects.all() 
    context ={
        'products':products,
        'category':shoe_category,
    }
    return render(request,'products/show_product.html',context)

def sort_by_price(request,name):
    greater_then,less_then = name.split('&')
    products = Product.objects.filter(
        Q(price_inclusive__lt =int(less_then)) 
            &
        Q(price_inclusive__gt=int(greater_then))
         
        )
    

    shoe_category = ShoeCategory.objects.all() 
    context ={
        'products':products,
        'category':shoe_category,
    }
    return render(request,'products/show_product.html',context)
