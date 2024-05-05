# Generated by Django 5.0.4 on 2024-05-05 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0010_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Н', 'Не одобрено'), ('Р', 'Рассмотрение'), ('С', 'Склад'), ('Д', 'Доставка'), ('П', 'Получено')], default='Р', max_length=46),
        ),
    ]
