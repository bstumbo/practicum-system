# Generated by Django 3.0.3 on 2020-02-28 19:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gw_practicum', '0014_auto_20200228_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hours',
            name='practicum_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gw_practicum.PracticumPlan'),
        ),
    ]
