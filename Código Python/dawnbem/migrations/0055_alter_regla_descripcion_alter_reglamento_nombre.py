# Generated by Django 4.2.3 on 2023-08-10 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dawnbem', '0054_remove_equipo_inscripcion_equipo_inscripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regla',
            name='descripcion',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='reglamento',
            name='nombre',
            field=models.CharField(default=None, max_length=50),
        ),
    ]
