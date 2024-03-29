# Generated by Django 2.1 on 2018-09-05 22:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('location_app', '0008_auto_20180829_2201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainlocationinfo',
            name='type',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='mainlocationinfo', to='location_app.TypeLocation'),
        ),
        migrations.AlterField(
            model_name='subonelocationinfo',
            name='type',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='subonelocationinfo', to='location_app.TypeLocation'),
        ),
    ]
