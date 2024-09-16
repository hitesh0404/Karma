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


# p1=Product()
# p1.save()