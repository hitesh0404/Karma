from django.db import models
from django.contrib.auth.models import User
from products.models import Product

# Create your models here.
STATUSCHOICE=[
    ('PENDING','PENDING'),
    ('DISPACHED','DISPACHED'),
    ('PROCESSING','PROCESSING'),
    ('OUT FOR DELIVERY','OUT FOR DELIVERY'),
    ('DELIVERED','DELIVERED'),
    ('CANCELED','CANCELED') ]

class Order(models.Model):
    order_uuid = models.UUIDField(primary_key=True,max_length=128)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    status = models.CharField(max_length=20,choices=STATUSCHOICE,default='PENDING')
    order_on = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    total = models.DecimalField(max_digits=12,decimal_places=2)
    # shipping_address = models.ForeignKey(Address,on_delete=models.CASCADE) 
    shipping_charges = models.IntegerChoices("Type", "Express Standard Night")

class OrderDetails(models.Model):
    order_id = models.ForeignKey(Order,on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product,on_delete=models.DO_NOTHING)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=12,decimal_places=2)
