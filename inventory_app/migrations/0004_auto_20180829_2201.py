# Generated by Django 2.1 on 2018-08-30 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_app', '0003_auto_20180826_2142'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventoryclass',
            name='description',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='inventorytype',
            name='description',
            field=models.TextField(default='', null=True),
        ),
    ]
