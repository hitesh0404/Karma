from django.shortcuts import get_object_or_404, redirect,render
from django.contrib.auth.models import User
from .models import Cart
from products.models import Product
from django.contrib.auth.decorators import login_required

@login_required
def add_to_cart(request,id):
    user = request.user
    user = get_object_or_404(User,username=user)
    product = get_object_or_404(Product,id =id)
    # item , create = Cart.objects.get_or_create(user=cust_obj,product=prod_obj)
    # if create:
    #     print('item created')
    # else:
    #     item.quantity+=1
    #     item.save()
    # return cart(request,cust_obj)
    try:
        obj = Cart.objects.get(user=user,product=product)
        obj.quantity +=1
        obj.save()
        return redirect('product_list')
    except Cart.DoesNotExist as e:
        #request.session['cart_item_count'] +=1
        Cart.objects.create(user=user,product = product,quantity=1)
    return redirect('product_list')
@login_required 
def cart(request):
    user  = get_object_or_404(User,username=request.user)
    cart = Cart.objects.filter(user = user)
    return render(request,'cart/cart.html',{'cart':cart})
@login_required
def clear_cart(request):
    #request.session['cart_item_count'] = 0
    user  = get_object_or_404(User,username=request.user)
    Cart.objects.filter(user = user).delete()
    return redirect('product_list')

@login_required
def update_cart(request):
    user  = get_object_or_404(User,username=request.user)
    cart = Cart.objects.filter(user = user)
    for item in cart:
        # print(request.GET)
        # # print(request.GET.get(item.id))
        # print(item.id)
        # print(request.GET.get(str(item.id)))
        quantity = request.GET.get(str(item.id))
        if int(quantity)<1:
            item.delete()
            #request.session['cart_item_count'] -=1
        else:
            item.quantity = quantity
            item.save()
    return redirect('cart')


@login_required    
def remove_item_from_cart(request,id):
    Cart.objects.get(id = id).delete()
    #request.session['cart_item_count'] -=1
    return redirect('cart')
