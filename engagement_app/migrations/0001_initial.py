# Generated by Django 2.0.7 on 2018-08-16 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Engagement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('partner', models.CharField(max_length=256)),
                ('location', models.CharField(max_length=256)),
            ],
        ),
    ]
