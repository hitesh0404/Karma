from django.shortcuts import render,redirect,get_object_or_404
from django.views import View
from .forms import ProductForm
from .models import Product,ShoeCategory,Shoe
from django.db.models import Q
from django.core.paginator import Paginator

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
    def get(self,request,slug):
        product = get_object_or_404(Product,slug=slug)
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

def get_products(request,products=None):
    if products ==None:    
        search = request.GET.get('search')
        if search:
            products = search_products(search)
        else:
            products = Product.objects.all()
    paginator = Paginator(products,5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    shoe_category = ShoeCategory.objects.all() 
    context ={
        'products':page_obj.object_list,
        'category':shoe_category,
        'page_obj':page_obj,
        'range':paginator.page_range
    }
    return context

def show_product(request):
    context = get_products(request)
    return render(request,'products/show_product.html',context)


def sort_by_category(request,name):
    cat = ShoeCategory.objects.get(name=name)
    shoecategoryshoe = cat.shoecategoryshoe_set.all()
    products = [product.shoe.product for product in shoecategoryshoe]
    print(products)
    # shoe_category = ShoeCategory.objects.all() 
    # context ={
    #     'products':products,
        # 'category':shoe_category,
    # }
    context = get_products(request=request, products=products)
    return render(request,'products/show_product.html',context)

def sort_by_price(request,name):
    greater_then,less_then = name.split('&')
    products = Product.objects.filter(
        Q(price_inclusive__lt =int(less_then)) 
            &
        Q(price_inclusive__gt=int(greater_then))
        )
    context = get_products(request=request, products=products)

    return render(request,'products/show_product.html',context)

    # shoe_category = ShoeCategory.objects.all() 
    # context ={
    #     'products':products,
    #     'category':shoe_category,
    # }
    # return render(request,'products/show_product.html',context)
