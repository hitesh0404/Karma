from django.shortcuts import render
from .models import Product,Category
# Create your views here.
def products(request):
    data = Product.objects.all()
    cate = Category.objects.all()
    context = {
        'products':data,
        'categories':cate
    }
    return render(request, 'product/products_list.html',context)

def add_product(request):
    if request.method == 'POST':
        return render(request, 'product/products_list.html',)#trial
    elif request.method == 'GET':
        return render(request, 'product/add_product.html')
# p1=Product()
# p1.save()