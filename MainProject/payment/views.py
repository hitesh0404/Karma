from django.shortcuts import render
from json import dumps
from django.conf import settings
import razorpay
from django.http import HttpResponse
def checkout(request):
    return render(request,'payment/checkout.html')
def payment(request):
    client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID,settings.RAZORPAY_KEY_SECRET ))
    data = { "amount": 500, "currency": "INR", "receipt": "order_rcptid_11" }
    payment = client.order.create(data=data)  
    context =  {
        'RAZORPAY_KEY_ID':settings.RAZORPAY_KEY_ID,
        'payment':payment
    }
    data = dumps(context,indent=4)
    return HttpResponse(data)