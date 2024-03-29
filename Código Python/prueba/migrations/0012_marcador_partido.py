# Generated by Django 4.2.3 on 2023-07-13 03:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prueba', '0011_asignacion_modalidad'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marcador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_Equipo', models.CharField(max_length=50)),
                ('punto_Marcador_Local', models.IntegerField()),
                ('punto_Marcador_Visitante', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Partido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('equipo_Local', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='equipoLocalList', to='prueba.equipoinscrito')),
                ('equipo_Visitante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='equipoVisitanteList', to='prueba.equipoinscrito')),
            ],
        ),
    ]
