# Generated by Django 3.0.3 on 2020-02-24 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gw_practicum', '0005_midpointevaluation_practicumdirector_practicumplan_preceptorfinalevaluation_studentselfevaluation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='preceptor',
            name='site',
        ),
    ]
