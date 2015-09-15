# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registrocr', '0002_auto_20150820_0237'),
    ]

    operations = [
        migrations.AddField(
            model_name='ciudadano',
            name='llamada',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='ciudadano',
            name='departamento',
            field=models.CharField(help_text=b'Este campo no es obligatorio ser\xc3\xa1 cargado directamente de la registraduria', max_length=60, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='ciudadano',
            name='direccion_puesto',
            field=models.CharField(help_text=b'Este campo no es obligatorio ser\xc3\xa1 cargado directamente de la registraduria', max_length=60, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='ciudadano',
            name='fecha_cumpleanios',
            field=models.DateField(auto_now_add=True, verbose_name=b'Fecha de cumplea\xc3\xb1os (dd/mm/yyyy), si no se tiene al a\xc3\xb1o de nacimiento ingrese el actual'),
        ),
        migrations.AlterField(
            model_name='ciudadano',
            name='mesa',
            field=models.CharField(help_text=b'Este campo no es obligatorio ser\xc3\xa1 cargado directamente de la registraduria', max_length=3, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='ciudadano',
            name='municipio',
            field=models.CharField(help_text=b'Este campo no es obligatorio ser\xc3\xa1 cargado directamente de la registraduria', max_length=60, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='ciudadano',
            name='puesto',
            field=models.CharField(help_text=b'Este campo no es obligatorio ser\xc3\xa1 cargado directamente de la registraduria', max_length=100, null=True, blank=True),
        ),
    ]
