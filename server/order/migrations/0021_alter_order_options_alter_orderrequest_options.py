# Generated by Django 5.0.4 on 2024-05-20 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0020_alter_orderrequest_order'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['-creation_time'], 'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
        migrations.AlterModelOptions(
            name='orderrequest',
            options={'ordering': ['-order__creation_time'], 'verbose_name': 'Запрос на заказ', 'verbose_name_plural': 'Запросы на заказы'},
        ),
    ]