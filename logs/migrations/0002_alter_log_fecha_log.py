# Generated by Django 4.1 on 2022-11-29 16:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='fecha_log',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha'),
        ),
    ]
