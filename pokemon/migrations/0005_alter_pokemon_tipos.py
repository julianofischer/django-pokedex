# Generated by Django 4.0.4 on 2022-05-18 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0004_tipo_pokemon_tipos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='tipos',
            field=models.ManyToManyField(blank=True, to='pokemon.tipo'),
        ),
    ]