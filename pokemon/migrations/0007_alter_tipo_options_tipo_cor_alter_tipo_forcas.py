# Generated by Django 4.0.4 on 2022-05-25 11:26

import colorfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0006_alter_tipo_forcas_alter_tipo_fraquezas'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tipo',
            options={'ordering': ['nome'], 'verbose_name': 'Tipo', 'verbose_name_plural': 'Tipos'},
        ),
        migrations.AddField(
            model_name='tipo',
            name='cor',
            field=colorfield.fields.ColorField(default='#000000', image_field=None, max_length=18, samples=None),
        ),
        migrations.AlterField(
            model_name='tipo',
            name='forcas',
            field=models.ManyToManyField(blank=True, to='pokemon.tipo', verbose_name='Forças'),
        ),
    ]
