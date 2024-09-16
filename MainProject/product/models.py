from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=20)
    price = models.DecimalField(decimal_places=2,max_digits=10)
    def __str__(self) -> str:
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=25)
