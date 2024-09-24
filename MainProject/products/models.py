from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField(null=True, blank=True)
    # image = models.ImageField(upload_to='brands/', null=True, blank=True)
    class Meta:
        db_table = 'Brand'


class Product(models.Model):
    name = models.CharField(max_length=20)
    price = models.DecimalField(decimal_places=2,max_digits=10)
    description = models.TextField(default='default Description')
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE,null=True)

    # image = models.ImageField(upload_to='products/')
    def __str__(self) -> str:
        return self.name
    class Meta:
        db_table = 'Product'

class Shoe(models.Model):
    product = models.OneToOneField(Product,on_delete=models.CASCADE,null=True)
    class Meta:
        db_table='Shoe'

class Style(models.Model):
    color = models.CharField(max_length=20)
    size = models.IntegerField(default=7)
    type = models.CharField(max_length=20)
    material = models.CharField(max_length=20)
    shoe = models.ManyToManyField(Shoe,through='ShoeStyle')
    class Meta:
        unique_together = ('color', 'size','material')
        db_table = 'Style'

class ShoeStyle(models.Model):
    shoe = models.ForeignKey(Shoe, on_delete=models.CASCADE,null=True)
    style = models.ForeignKey(Style, on_delete=models.CASCADE,null=True)
    class Meta:
        unique_together = (('shoe', 'style'),)
        db_table = 'ShoeStyle'

