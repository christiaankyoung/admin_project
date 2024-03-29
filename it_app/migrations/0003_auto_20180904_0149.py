# Generated by Django 2.1 on 2018-09-04 08:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('location_app', '0008_auto_20180829_2201'),
        ('it_app', '0002_auto_20180830_2209'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainLocationApplication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(default='', null=True)),
                ('application', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='mainlocationapplication', to='it_app.Application')),
                ('mainlocation', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='mainlocationapplication', to='location_app.MainLocation')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='mainlocationapplication',
            unique_together={('application', 'mainlocation')},
        ),
    ]
