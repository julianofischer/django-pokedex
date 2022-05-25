# Generated by Django 4.0.4 on 2022-05-11 12:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('ataque', models.PositiveSmallIntegerField()),
                ('defesa', models.PositiveSmallIntegerField()),
                ('stamina', models.PositiveSmallIntegerField()),
                ('foto', models.ImageField(upload_to='media')),
                ('involucao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='evolucoes', to='pokemon.pokemon')),
            ],
        ),
    ]