# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registrocr', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lider',
            options={'verbose_name_plural': 'Lideres'},
        ),
        migrations.RemoveField(
            model_name='candidato',
            name='numero_tarjeton',
        ),
        migrations.AddField(
            model_name='ciudadano',
            name='candidatos',
            field=models.ManyToManyField(to='registrocr.Candidato', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='ciudadano',
            name='departamento',
            field=models.CharField(default=None, max_length=60, null=True, help_text=b'Este campo no es obligatorio ser\xc3\xa1 cargado directamente de la registraduria', blank=True),
        ),
        migrations.AddField(
            model_name='ciudadano',
            name='direccion_puesto',
            field=models.CharField(default=None, max_length=60, null=True, help_text=b'Este campo no es obligatorio ser\xc3\xa1 cargado directamente de la registraduria', blank=True),
        ),
        migrations.AddField(
            model_name='ciudadano',
            name='llamada',
            field=models.BooleanField(default=False, help_text=b'Indique si ya realizo el telemercadeo a este votante'),
        ),
        migrations.AddField(
            model_name='ciudadano',
            name='mesa',
            field=models.CharField(default=None, max_length=3, null=True, help_text=b'Este campo no es obligatorio ser\xc3\xa1 cargado directamente de la registraduria', blank=True),
        ),
        migrations.AddField(
            model_name='ciudadano',
            name='municipio',
            field=models.CharField(default=None, max_length=60, null=True, help_text=b'Este campo no es obligatorio ser\xc3\xa1 cargado directamente de la registraduria', blank=True),
        ),
        migrations.AddField(
            model_name='ciudadano',
            name='observaciones',
            field=models.CharField(max_length=60, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='ciudadano',
            name='puesto',
            field=models.CharField(default=None, max_length=100, null=True, help_text=b'Este campo no es obligatorio ser\xc3\xa1 cargado directamente de la registraduria', blank=True),
        ),
        migrations.AddField(
            model_name='lider',
            name='fecha_reunion',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='lider',
            name='reunion',
            field=models.BooleanField(default=False, help_text=b'Indica si ya ha realizado reuni\xc3\xb3n'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='perfil',
            field=models.CharField(default=b'1', max_length=1, choices=[(b'1', b'CONCEJO'), (b'2', b'ALCALDIA'), (b'3', b'ASAMBLEA'), (b'4', b'GOBERNACION')]),
        ),
        migrations.AlterField(
            model_name='ciudadano',
            name='fecha_cumpleanios',
            field=models.DateField(auto_now_add=True, verbose_name=b'Fecha de cumplea\xc3\xb1os (dd/mm/yyyy), si no se tiene al a\xc3\xb1o de nacimiento ingrese el actual'),
        ),
    ]
