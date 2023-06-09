# Generated by Django 4.1 on 2022-11-10 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departamentos', '0004_departamento_rut_jefe_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departamento',
            name='rut_jefe',
            field=models.CharField(blank=True, max_length=20, verbose_name='Rut Jefe'),
        ),
        migrations.AlterField(
            model_name='departamento',
            name='rut_jefe_subrogante',
            field=models.CharField(blank=True, max_length=20, verbose_name='Rut Jefe Subrogante'),
        ),
        migrations.AlterField(
            model_name='subdepartamento',
            name='rut_jefe',
            field=models.CharField(blank=True, max_length=20, verbose_name='Rut Jefe'),
        ),
        migrations.AlterField(
            model_name='subdepartamento',
            name='rut_jefe_subrogante',
            field=models.CharField(blank=True, max_length=20, verbose_name='Rut Jefe Subrogante'),
        ),
        migrations.AlterField(
            model_name='unidad',
            name='rut_jefe',
            field=models.CharField(blank=True, max_length=20, verbose_name='Rut Jefe'),
        ),
        migrations.AlterField(
            model_name='unidad',
            name='rut_jefe_subrogante',
            field=models.CharField(blank=True, max_length=20, verbose_name='Rut Jefe Subrogante'),
        ),
    ]
