# Generated by Django 5.1 on 2024-10-10 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_product_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='C:\\Users\\admin\\Project\\karma-master\\MainProject\\static\\img\\product\\p2.jpg', upload_to='products/'),
        ),
    ]