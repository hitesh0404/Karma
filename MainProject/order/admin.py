from django.contrib import admin

# Register your models here.
from .models import Order,OrderDetails


admin.site.register([Order,OrderDetails])