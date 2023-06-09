# Generated by Django 4.1 on 2022-08-25 13:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('departamentos', '0002_alter_departamento_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Formulario',
            fields=[
                ('id_formulario', models.AutoField(primary_key=True, serialize=False)),
                ('folio', models.CharField(max_length=50, unique=True, verbose_name='Folio')),
                ('fecha_creacion', models.DateField(verbose_name='Fecha Creación')),
                ('rut_solicitante', models.CharField(max_length=50, verbose_name='Rut Solicitante')),
                ('rut_jefe_aprobador', models.CharField(max_length=50, verbose_name='Rut Jefe Aprobador')),
                ('rut_admin_interna', models.CharField(max_length=50, verbose_name='Rut Administración Interna')),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('id_departamento', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='departamentos.departamento', verbose_name='Departamento')),
                ('id_sub_departamento', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='departamentos.subdepartamento', verbose_name='Sub Departamento')),
                ('id_unidad', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='departamentos.unidad', verbose_name='Unidad')),
            ],
        ),
    ]
