# Generated by Django 4.2.3 on 2023-08-11 16:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dawnbem', '0063_rename_estadoinscripcion_revisioninscripcion_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='equipo',
            old_name='inscripcion',
            new_name='inscripcion_list',
        ),
    ]
