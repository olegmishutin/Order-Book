# Generated by Django 5.0.4 on 2024-05-05 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0007_alter_order_identification_number_alter_order_user'),
        ('product', '0009_remove_product_weight_product_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(editable=False, related_name='orders', through='order.OrderProduct', to='product.product'),
        ),
    ]