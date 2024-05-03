# Generated by Django 5.0.4 on 2024-05-03 11:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product_weight_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productphoto',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='product.product'),
        ),
    ]
