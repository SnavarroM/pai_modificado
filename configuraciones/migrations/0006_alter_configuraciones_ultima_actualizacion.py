# Generated by Django 4.1 on 2022-11-24 13:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('configuraciones', '0005_alter_configuraciones_ultima_actualizacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configuraciones',
            name='ultima_actualizacion',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Última Actualización'),
        ),
    ]
