# Generated by Django 5.0.4 on 2024-05-03 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_alter_user_full_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='login',
            field=models.CharField(db_index=True, editable=False, max_length=128, unique=True),
        ),
    ]
