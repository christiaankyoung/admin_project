# Generated by Django 2.1 on 2018-08-26 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('engagement_app', '0004_auto_20180825_2305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locationnames',
            name='engagement',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='locationnames', to='engagement_app.Engagement'),
        ),
    ]
