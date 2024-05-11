# Generated by Django 5.0.4 on 2024-05-08 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0018_alter_orderrequest_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderrequest',
            name='status',
            field=models.CharField(choices=[('Н', 'Новый'), ('О', 'В обработке'), ('Р', 'Решен'), ('ОТ', 'Отклонен')], default='Н', max_length=46),
        ),
    ]