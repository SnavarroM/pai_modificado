# Generated by Django 4.1 on 2022-11-23 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cierreMensual', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cierremensualinsumo',
            name='denominacion',
            field=models.CharField(default='', max_length=255, verbose_name='Denominación'),
        ),
    ]
