# Generated by Django 2.1 on 2018-09-02 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engagement_app', '0008_auto_20180829_2201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locationnames',
            name='mainlocation_name',
            field=models.CharField(blank=True, default='Main Location', max_length=56, null=True),
        ),
        migrations.AlterField(
            model_name='locationnames',
            name='subonelocation_name',
            field=models.CharField(blank=True, default='Sub One Location', max_length=56, null=True),
        ),
        migrations.AlterField(
            model_name='locationnames',
            name='subthreelocation_name',
            field=models.CharField(blank=True, default='Sub Three Location', max_length=56, null=True),
        ),
        migrations.AlterField(
            model_name='locationnames',
            name='subtwolocation_name',
            field=models.CharField(blank=True, default='Sub Two Location', max_length=56, null=True),
        ),
    ]
