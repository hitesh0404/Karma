from django.urls import path
from . import views
urlpatterns =[
    path('checkout/',views.checkout,name='checkout'),
    path('proceed-to-pay/',views.payment,name='proceed_to_pay'),
    path('verify-payment/',views.verify_payment,name='verify_payment'),

]