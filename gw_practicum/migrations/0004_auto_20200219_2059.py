# Generated by Django 3.0.3 on 2020-02-19 20:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gw_practicum', '0003_auto_20200219_2042'),
    ]

    operations = [
        migrations.CreateModel(
            name='DegreeLevel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Major',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='preceptor',
            name='phone',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gwid', models.CharField(max_length=120)),
                ('degree', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gw_practicum.DegreeLevel')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gw_practicum.Department')),
                ('major', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gw_practicum.Major')),
                ('user_data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]