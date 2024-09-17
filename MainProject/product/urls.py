from django.urls import path
from . import views

urlpatterns = [
    path('product_list/',views.products,name='products'),
    path('add-product/',views.add_product,name='add_product'),
]