# Generated by Django 4.1 on 2022-11-23 15:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presupuesto', '0007_alter_presupuestodepartamento_id_presupuesto_categoria_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='presupuestocategoria',
            options={'ordering': ['-id']},
        ),
    ]
