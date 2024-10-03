from django.db import models
class HsnCode(models.Model):
    index = models.BigAutoField(primary_key=True)
    item_code = models.BigIntegerField(verbose_name='Item Code',null=True) 
    item_name = models.TextField(verbose_name='Item Name',null=True) 
    item_type = models.TextField(verbose_name='Item Type',null=True) 
    GSTe = models.DecimalField(max_digits=5,decimal_places=2,verbose_name=r'GST %e',null=True)
    hsn_code = models.BigIntegerField(verbose_name='HSN Code',null=True)
    GST = models.DecimalField(max_digits=5,decimal_places=2,verbose_name='GST %',null=True)
    
    # class Meta:
    #     db_table = 'hsn_code'
    def __str__(self) -> str:
        return f'{self.item_code}-{self.GSTe}%--{self.hsn_code}--{self.GST}'


class Brand(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField(null=True, blank=True)
    # image = models.ImageField(upload_to='brands/', null=True, blank=True)
    class Meta:
        db_table = 'Brand'
    def __str__(self):
        return f'({self.name}) : {self.description}'


    
from django.shortcuts import get_object_or_404
class Product(models.Model):
    name = models.CharField(max_length=20)
    price_inclusive = models.DecimalField(decimal_places=2,max_digits=10)
    description = models.TextField(default='default Description')
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE,null=True)
    gst_rate = models.DecimalField(max_digits=5,decimal_places=2,default=5.00)
    hsn_code = models.CharField(max_length=10,default=None)
    # def save(self,commit=False):
    #     data = get_object_or_404(HsnCode,item_code=self.hsn_code)
    #     if (data):
    #         self.gst_rate = data.GSTe
    #     super().save()
    @property
    def price_exclusive(self):
        return self.price_inclusive / (1 + (self.gst_rate / 100))
    @property
    def gst_amount(self):
        return self.price_inclusive - self.price_exclusive
    
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

