from django.urls import path
from . import views
urlpatterns= [
    path('add-product/',views.AddProduct.as_view(),name = 'add_product'),
    path('update-product/<int:id>/',views.UpdateProduct.as_view(),name = 'update_product'),
    path('show-product-list/',views.show_product,name = 'product_list'),
    path('show-product-list/sort-by-category/<str:name>/',views.sort_by_category,name = 'sort_by_category'),

]