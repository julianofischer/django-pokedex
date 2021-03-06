# Generated by Django 4.0.4 on 2022-05-25 12:40

import colorfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0007_alter_tipo_options_tipo_cor_alter_tipo_forcas'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tipo',
            name='fraquezas',
        ),
        migrations.AlterField(
            model_name='tipo',
            name='cor',
            field=colorfield.fields.ColorField(default='#FFFFFF', image_field=None, max_length=18, samples=None),
        ),
        migrations.AlterField(
            model_name='tipo',
            name='forcas',
            field=models.ManyToManyField(blank=True, related_name='fraquezas', to='pokemon.tipo', verbose_name='Forças'),
        ),
    ]
