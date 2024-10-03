from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register([Brand,Product,Shoe,Style,ShoeStyle,HsnCode])