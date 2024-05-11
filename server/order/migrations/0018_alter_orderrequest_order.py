# Generated by Django 5.0.4 on 2024-05-08 11:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0017_orderrequest_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderrequest',
            name='order',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, related_name='request', to='order.order'),
        ),
    ]