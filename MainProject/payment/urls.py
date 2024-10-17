from django.urls import path
from . import views
urlpatterns =[
    path('checkout/',views.checkout,name='checkout'),
    path('proceed-to-pay/',views.payment,name='payment'),
]