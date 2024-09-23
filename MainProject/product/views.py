from django.shortcuts import render,redirect,get_object_or_404
from .models import Product,Category,ProductType
# Create your views here.
def products(request):
    data = Product.objects.all()
    # cate = Category.objects.all()
    context = {
        'products':data,
        # 'categories':cate
    }
    return render(request, 'product/products_list.html',context)

def product_types(request):
    data = ProductType.objects.all()
    context = {
        'product_types':data
    }
    return render(request,'product/product_types.html',context)


def add_product(request):
    if request.method == 'POST':
        print(request.POST)
        n = request.POST.get('name')
        p = request.POST.get('price')
        Product.objects.create(name=n,price= p)
        return render(request, 'product/products_list.html',)#trial
    elif request.method == 'GET':
        return render(request, 'product/add_product.html')

def update_product(request,id):
    # product = Product.objects.get(id=id)
    product = get_object_or_404(Product,id=id)
    if request.method == 'POST':
        product.name = request.POST.get('name')
        product.price = request.POST.get('price')
        product.save()
        return redirect('products')
    elif request.method =='GET':
        return render(request, 'product/update_product.html',{'product':product})



def delete_product(request,id):
    product = get_object_or_404(Product,id=id)
    if request.method=="POST":
        product.delete()
        return redirect('products')
    elif request.method=="GET":
        return render(request,'product/confirm_delete.html',{'product':product})


# p1=Product()
# p1.save()




def delete_product_type(request,id):
    product_type = get_object_or_404(ProductType,id=id)
    return render(request,'product/confirm.html',{'product_type': product_type})



def confirm_delete_product_type(request,id):
    product_type = get_object_or_404(ProductType,id=id)
    product_type.delete()
    return redirect('products')


def create_product_type(request):
    if request.method == 'GET':
        return render(request, 'product/create_product_type.html')
    elif request.method == 'POST':
        
        n = request.POST.get('name')
        d = request.POST.get('desc') 
        if n and d:
            ProductType.objects.create(name=n,desc=d)
            return redirect('product_types')
        else:
            return render(request, 'product/create_product_type.html',{'error':'Please fill all fields'})
        


def update_product_type(request):
    data  = ProductType.objects.all()
    return render(request,'product/update_product_types.html',{'types':data})


def update_data(request,id):
    product_type = get_object_or_404(ProductType,id=id)
    return render(request,'product/update_product_data.html',{'product_type':product_type})


def confirm_update_product_type(request,id):
    product_type = get_object_or_404(ProductType,id=id)
    n = request.GET.get('name')
    d = request.GET.get('description')
    
    product_type.name = n
    product_type.description = d
    if n and d:
        product_type.save()
        return redirect('update_product_type')
    else:
        return render(request,'product/update_product_data.html',{'product_type':product_type})
