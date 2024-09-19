from django.urls import path
from . import views

urlpatterns = [
    path('product_list/',views.products,name='products'),
    path('product_types/',views.product_types,name='product_types'),
    path('add-product/',views.add_product,name='add_product'),
    path('update-product/<int:id>/',views.update_product,name='update_product'),
    path('delete-product/<int:id>/',views.delete_product,name='delete_product'),
    path('delete-product-type/<int:id>/',views.delete_product_type,name='delete_product_type'),
    path('confirm-delete-product-type/<int:id>/',views.confirm_delete_product_type,name='confirm_delete_product_type'),

]