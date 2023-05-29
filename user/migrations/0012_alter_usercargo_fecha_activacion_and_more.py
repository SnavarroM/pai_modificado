# Generated by Django 4.1 on 2022-09-22 20:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_alter_userprofile_id_perfil'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercargo',
            name='fecha_activacion',
            field=models.DateField(blank=True, verbose_name='Fecha Activación'),
        ),
        migrations.AlterField(
            model_name='usercargo',
            name='fecha_desactivacion',
            field=models.DateField(blank=True, verbose_name='Fecha Desactivación'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='id_perfil',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='user.perfil', verbose_name='Perfil'),
        ),
    ]
