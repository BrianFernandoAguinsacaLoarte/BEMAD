# Generated by Django 4.2.3 on 2023-07-13 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prueba', '0005_estadoinscripcion_inscripcion_jugadorinscrito'),
    ]

    operations = [
        migrations.DeleteModel(
            name='EstadoInscripcion',
        ),
        migrations.RenameField(
            model_name='jugador',
            old_name='numero',
            new_name='numero_Camiseta',
        ),
        migrations.RemoveField(
            model_name='jugador',
            name='posicion',
        ),
        migrations.AddField(
            model_name='inscripcion',
            name='estado_Inscripcion',
            field=models.CharField(default='01', max_length=50),
            preserve_default=False,
        ),
    ]
