# Generated by Django 3.0.3 on 2020-02-27 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gw_practicum', '0009_hours'),
    ]

    operations = [
        migrations.AddField(
            model_name='practicumplan',
            name='total_hours',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=3),
        ),
    ]
