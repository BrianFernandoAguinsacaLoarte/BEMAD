# Generated by Django 4.2.3 on 2023-07-13 03:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prueba', '0012_marcador_partido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marcador',
            name='punto_Marcador_Local',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='marcador',
            name='punto_Marcador_Visitante',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='temporada',
            name='duracion',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
