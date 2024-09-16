from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=20)
    price = models.DecimalField(decimal_places=2,max_digits=10)
    def __str__(self) -> str:
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=25)

class ProductType(models.Model):
    id  = models.IntegerField(models.BigAutoField,primary_key=True,auto_created=True)
    name = models.CharField(max_length=25)
    description = models.TextField(verbose_name='desc')
    def __str__(self)->str:
        return self.name

# python manage.py makemigrations
# python manage.py migrate
# # for i in Product.objects.filter(price__in = ( 176.43, 250.60,176.44,150)):
#     print(f'{str(i.id).center(4,' ')} | {i.name.center(20,' ' )} | {i.price}')