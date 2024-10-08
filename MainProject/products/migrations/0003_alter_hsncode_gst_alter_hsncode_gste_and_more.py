# Generated by Django 5.1 on 2024-09-30 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_hsncode_rename_price_product_price_inclusive_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hsncode',
            name='GST',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True, verbose_name='GST %'),
        ),
        migrations.AlterField(
            model_name='hsncode',
            name='GSTe',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True, verbose_name='GST %e'),
        ),
        migrations.AlterField(
            model_name='hsncode',
            name='hsn_code',
            field=models.BigIntegerField(null=True, verbose_name='HSN Code'),
        ),
        migrations.AlterField(
            model_name='hsncode',
            name='item_code',
            field=models.BigIntegerField(null=True, verbose_name='Item Code'),
        ),
        migrations.AlterField(
            model_name='hsncode',
            name='item_name',
            field=models.TextField(null=True, verbose_name='Item Name'),
        ),
        migrations.AlterField(
            model_name='hsncode',
            name='item_type',
            field=models.TextField(null=True, verbose_name='Item Type'),
        ),
    ]
