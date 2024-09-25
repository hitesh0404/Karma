from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField(null=True, blank=True)
    # image = models.ImageField(upload_to='brands/', null=True, blank=True)
    class Meta:
        db_table = 'Brand'
    def __str__(self):
        return f'({self.name}) : {self.description}'



class Product(models.Model):
    name = models.CharField(max_length=20)
    price = models.DecimalField(decimal_places=2,max_digits=10)
    description = models.TextField(default='default Description')
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return f'({self.name}) from {self.brand.name}'
    # image = models.ImageField(upload_to='products/')
    class Meta:
        db_table = 'Product'

class Shoe(models.Model):
    product = models.OneToOneField(Product,on_delete=models.CASCADE,null=True)
    class Meta:
        db_table='Shoe'
    def __str__(self):
        return f'({self.product}) : ₹ {self.product.price:.2f}  '

class Style(models.Model):
    color = models.CharField(max_length=20)
    size = models.IntegerField(default=7)
    type = models.CharField(max_length=20)
    material = models.CharField(max_length=20)
    shoe = models.ManyToManyField(Shoe,through='ShoeStyle')
    class Meta:
        unique_together = ('color', 'size','material')
        db_table = 'Style'
    def __str__(self):
        return f'color: {self.color} and type: {self.type} made with {self.material}'

class ShoeStyle(models.Model):
    shoe = models.ForeignKey(Shoe, on_delete=models.CASCADE,null=True)
    style = models.ForeignKey(Style, on_delete=models.CASCADE,null=True)
    class Meta:
        unique_together = (('shoe', 'style'),)
        db_table = 'ShoeStyle'
    def __str__(self):
        return f'{self.shoe}  {self.style}' 

