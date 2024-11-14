# Generated by Django 5.1 on 2024-10-28 08:59

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=autoslug.fields.AutoSlugField(blank=True, editable=False, populate_from='name', unique=True),
        ),
    ]