# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registrocr', '0004_auto_20150915_0643'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidato',
            name='numero_tarjeton',
        ),
        migrations.AlterField(
            model_name='candidato',
            name='perfil',
            field=models.CharField(default=b'1', max_length=1, choices=[(b'1', b'CONCEJO'), (b'2', b'ALCALDIA'), (b'3', b'ASAMBLEA'), (b'4', b'GOBERNACION')]),
        ),
        migrations.AlterField(
            model_name='ciudadano',
            name='candidatos',
            field=models.ManyToManyField(to='registrocr.Candidato', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='ciudadano',
            name='departamento',
            field=models.CharField(default=None, max_length=60, null=True, help_text=b'Este campo no es obligatorio ser\xc3\xa1 cargado directamente de la registraduria', blank=True),
        ),
        migrations.AlterField(
            model_name='ciudadano',
            name='direccion_puesto',
            field=models.CharField(default=None, max_length=60, null=True, help_text=b'Este campo no es obligatorio ser\xc3\xa1 cargado directamente de la registraduria', blank=True),
        ),
        migrations.AlterField(
            model_name='ciudadano',
            name='mesa',
            field=models.CharField(default=None, max_length=3, null=True, help_text=b'Este campo no es obligatorio ser\xc3\xa1 cargado directamente de la registraduria', blank=True),
        ),
        migrations.AlterField(
            model_name='ciudadano',
            name='municipio',
            field=models.CharField(default=None, max_length=60, null=True, help_text=b'Este campo no es obligatorio ser\xc3\xa1 cargado directamente de la registraduria', blank=True),
        ),
        migrations.AlterField(
            model_name='ciudadano',
            name='puesto',
            field=models.CharField(default=None, max_length=100, null=True, help_text=b'Este campo no es obligatorio ser\xc3\xa1 cargado directamente de la registraduria', blank=True),
        ),
    ]
