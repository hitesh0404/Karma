from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.Login.as_view(),name='login'),
    path('logout/',views.logout_customer,name='logout'),
    path('register/',views.Register.as_view(),name='register'),
]