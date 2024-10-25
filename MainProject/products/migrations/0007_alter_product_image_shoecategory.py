# Generated by Django 5.1 on 2024-10-15 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='\\products\\p7.jpg', upload_to='products/'),
        ),
        migrations.CreateModel(
            name='ShoeCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('description', models.CharField(max_length=100)),
                ('shoe', models.ManyToManyField(to='products.shoe')),
            ],
            options={
                'db_table': 'Shoe_Category',
            },
        ),
    ]
