# Generated by Django 2.0.7 on 2018-08-17 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location_app', '0002_auto_20180817_1358'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainlocationinfo',
            name='balance',
            field=models.IntegerField(null=True),
        ),
    ]
