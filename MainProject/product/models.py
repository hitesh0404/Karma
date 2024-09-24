from django.db import models
# Create your models here.


class Brand(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField(null=True, blank=True)
    # image = models.ImageField(upload_to='brands/', null=True, blank=True)
    class Meta:
        db_table = 'Brand'


class Product(models.Model):
    name = models.CharField(max_length=20)
    price = models.DecimalField(decimal_places=2,max_digits=10)
    description = models.TextField()
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE)

    # image = models.ImageField(upload_to='products/')
    def __str__(self) -> str:
        return self.name
    class Meta:
        db_table = 'Product'

class Shoe(models.Model):
    product = models.OneToOneField(Product,on_delete=models.CASCADE)
    class Meta:
        db_table='Shoe'

class Style(models.Model):
    color = models.CharField(max_length=20)
    size = models.IntegerField()
    type = models.CharField(max_length=20)
    material = models.CharField(max_length=20)
    shoe = models.ManyToManyField(Shoe,through='ShoeStyle')
    class Meta:
        unique_together = ('color', 'size','material')
        db_table = 'Style'

class ShoeStyle(models.Model):
    shoe = models.ForeignKey(Shoe, on_delete=models.CASCADE)
    style = models.ForeignKey(Style, on_delete=models.CASCADE)
    class Meta:
        unique_together = (('shoe', 'style'),)
        db_table = 'ShoeStyle'

# class Category(models.Model):
#     name = models.CharField(max_length=25)

# class ProductType(models.Model):
#     id  = models.IntegerField(models.BigAutoField,primary_key=True,auto_created=True)
#     name = models.CharField(max_length=25)
#     description = models.TextField(verbose_name='desc')
#     def __str__(self)->str:
#         return self.name

# python manage.py makemigrations
# python manage.py migrate
# # for i in Product.objects.filter(price__in = ( 176.43, 250.60,176.44,150)):
#     print(f'{str(i.id).center(4,' ')} | {i.name.center(20,' ' )} | {i.price}')