# Generated by Django 4.2.3 on 2023-08-12 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dawnbem', '0074_rename_equipo_sorteo_equipo_list'),
    ]

    operations = [
        migrations.AddField(
            model_name='inscripcion',
            name='EstadoInscripcion',
            field=models.CharField(blank=True, choices=[('Registrado', 'Registrado'), ('En Proceso', 'En Proceso'), ('Anulada', 'Anulada')], default='En Proceso', max_length=10, null=True),
        ),
    ]
