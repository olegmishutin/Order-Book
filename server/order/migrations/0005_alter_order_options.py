# Generated by Django 5.0.4 on 2024-05-05 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_alter_order_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['creation_time'], 'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
    ]
