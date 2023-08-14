# Generated by Django 4.2.3 on 2023-07-29 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dawnbem', '0023_alter_inscripcion_fecha_aprobacion_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CrearRol',
        ),
        migrations.AddField(
            model_name='registro',
            name='EleccionDeRol',
            field=models.CharField(choices=[('Jugador', 'Jugador'), ('Director Tecnico', 'Director Tecnico'), ('Arbitro', 'Arbitro')], default='Valor_Predeterminado', max_length=50),
        ),
    ]
