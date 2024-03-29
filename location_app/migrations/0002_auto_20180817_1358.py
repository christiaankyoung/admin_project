# Generated by Django 2.0.7 on 2018-08-17 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainLocationInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mainlocation', models.ForeignKey(blank=True, on_delete='Cascade', related_name='mainlocationinfo', to='location_app.MainLocation')),
                ('type', models.ForeignKey(blank=True, on_delete='Cascade', related_name='mainlocationinfotype', to='location_app.TypeLocation')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='mainlocationinfo',
            unique_together={('type', 'mainlocation')},
        ),
    ]
