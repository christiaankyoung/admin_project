# Generated by Django 2.1 on 2018-08-26 06:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('engagement_app', '0003_auto_20180825_2303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locationnames',
            name='engagement',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='locationnames', to='engagement_app.Engagement', unique=True),
        ),
    ]
