# Generated by Django 4.2.3 on 2023-08-11 16:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dawnbem', '0064_rename_inscripcion_equipo_inscripcion_list'),
    ]

    operations = [
        migrations.RenameField(
            model_name='equipo',
            old_name='inscripcion_list',
            new_name='inscripcion',
        ),
    ]
