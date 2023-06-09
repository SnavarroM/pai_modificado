# Generated by Django 4.1 on 2022-09-26 14:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('departamentos', '0002_alter_departamento_options_and_more'),
        ('user', '0021_alter_usercargo_id_cargo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdepartamento',
            name='id_unidad',
            field=models.ForeignKey(default=0, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='usuario_unidad', to='departamentos.unidad', verbose_name='Unidad'),
        ),
    ]
