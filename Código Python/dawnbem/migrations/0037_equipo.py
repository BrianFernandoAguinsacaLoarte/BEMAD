# Generated by Django 4.2.3 on 2023-07-30 17:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dawnbem', '0036_remove_registro_escogermodalidad_jugador_posicion_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('numero_Jugadores', models.PositiveIntegerField()),
                ('inscripcion', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='inscripcionList', to='dawnbem.inscripcion')),
            ],
        ),
    ]
