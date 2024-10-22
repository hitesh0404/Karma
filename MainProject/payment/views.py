import razorpay
from django.shortcuts import render,get_object_or_404,redirect
from json import dumps
from django.conf import settings
from django.http import HttpResponse
from django.contrib.auth.models import User
from cart.models import Cart
from order.models import Order,OrderDetails
from .models import Payment
from accounts.models import Customer,Address
from django.views.decorators.csrf import csrf_exempt

def checkout(request):
    return render(request,'payment/checkout.html')

def payment(request):
    user  = get_object_or_404(User,username=request.user)
    cart = Cart.objects.filter(user = user)
    amount = 0
    for item in cart:
        amount += (item.product.price_inclusive * item.quantity )
    amount *= 100
    amount = int(amount)
    customer_obj = get_object_or_404(Customer,user= user)
    address_obj = Address.objects.filter(user = customer_obj).first()
    order_obj = Order.objects.filter(user= user).filter(status ='CREATED')    
    if order_obj.exists():
        order_obj = order_obj[0]
    else: 
        order_obj = Order.objects.create(
                                    # order_uuid =None,
                                    user=user,
                                    status="CREATED",
                                    total = amount,
                                    # shipping_charges = 1,
                                    shipping_address = address_obj
                                    )
        
    client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID,settings.RAZORPAY_KEY_SECRET ))
    data = { "amount": amount, "currency": "INR", "receipt": str(order_obj.order_uuid) }
    payment = client.order.create(data=data)  
    context =  {
        'RAZORPAY_KEY_ID':settings.RAZORPAY_KEY_ID,
        'payment':payment,
        'callback_url':'/payment/verify-payment/'
    }
    print('\n\n\n\n\n\n',payment,type(payment),'\n\n\n\n\n\n')
    Payment.objects.create(
            user=user,
            razorpay_order_id = payment['id'],
            amount = order_obj.total/100,
            status = 'PENDING',
            method = 'RAZORPAY',
            order = order_obj
        )
    data = dumps(context,indent=4)
    print(type(data),data,order_obj.__dict__)
    return HttpResponse(data)

@csrf_exempt
def verify_payment(request):
    try:
        client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID,settings.RAZORPAY_KEY_SECRET ))
        pay ={                                  'razorpay_order_id': request.POST.get('razorpay_order_id'),
                                                'razorpay_payment_id': request.POST.get('razorpay_payment_id'),
                                                'razorpay_signature': request.POST.get('razorpay_signature'),
                                                }
        print(pay)
        client.utility.verify_payment_signature({
                                                'razorpay_order_id': request.POST.get('razorpay_order_id'),
                                                'razorpay_payment_id': request.POST.get('razorpay_payment_id'),
                                                'razorpay_signature': request.POST.get('razorpay_signature'),
                                                })
        
        print('done succesful Payment')
        payment_obj = Payment.objects.get(razorpay_order_id =str(request.POST.get('razorpay_order_id')))
        cart = Cart.objects.filter(user = payment_obj.user)
        print(cart)
        order_obj = payment_obj.order
        payment_obj.razorpay_payment_id = str(request.POST.get('razorpay_payment_id'))
        payment_obj.payment_signature = str( request.POST.get('razorpay_signature'))
        payment_obj.status = "COMPLETED"
        payment_obj.save()
        for item in cart:
            OrderDetails.objects.create(
                order_id = order_obj,
                product = item.product,
                quantity = item.quantity,
                price = item.product.price_inclusive
            )
        cart.delete()
        return redirect('/')
    except Exception as e:
        print(e)
        return redirect('cart')

