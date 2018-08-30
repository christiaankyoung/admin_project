# Generated by Django 2.1 on 2018-08-30 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location_app', '0007_auto_20180819_1629'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainlocation',
            name='address',
            field=models.CharField(default='', max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='mainlocation',
            name='description',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='subonelocation',
            name='address',
            field=models.CharField(default='', max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='subonelocation',
            name='description',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='subtwolocation',
            name='address',
            field=models.CharField(default='', max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='subtwolocation',
            name='description',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='typelocation',
            name='description',
            field=models.TextField(default='', null=True),
        ),
    ]
