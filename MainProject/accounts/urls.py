from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.Login.as_view(),name='login'),
    path('logout/',views.logout_customer,name='logout'),
    path('register/',views.Register.as_view(),name='register'),
    path('forgot-password/',views.ForgotPassword.as_view(),name ='forgot_password'),
    path('verify-otp/',views.verify_otp,name='verify_otp'),
]