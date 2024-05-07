# Generated by Django 5.0.4 on 2024-05-05 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_remove_product_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='weight',
        ),
        migrations.AddField(
            model_name='product',
            name='info',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]