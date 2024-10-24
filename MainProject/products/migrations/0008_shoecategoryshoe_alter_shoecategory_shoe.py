# Generated by Django 5.1 on 2024-10-24 08:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_alter_product_image_shoecategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShoeCategoryShoe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.shoecategory')),
                ('shoe', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.shoe')),
            ],
            options={
                'db_table': 'Shoe_Category_shoe',
                'unique_together': {('shoe', 'category')},
            },
        ),
        migrations.AlterField(
            model_name='shoecategory',
            name='shoe',
            field=models.ManyToManyField(through='products.ShoeCategoryShoe', to='products.shoe'),
        ),
    ]