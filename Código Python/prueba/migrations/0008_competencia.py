# Generated by Django 4.2.3 on 2023-07-13 02:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prueba', '0007_alter_inscripcion_estado_inscripcion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Competencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('tipo_Mode_Juego', models.CharField(choices=[('Futbol', 'Futbol'), ('Baloncesto', 'Baloncesto'), ('Ecuavoly', 'Ecuavoly')], default='Futbol', max_length=50)),
                ('inscripcion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='competenciaList', to='prueba.inscripcion')),
            ],
        ),
    ]
