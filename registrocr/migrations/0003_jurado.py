# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registrocr', '0002_auto_20151013_1534'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jurado',
            fields=[
                ('id', models.OneToOneField(primary_key=True, db_column=b'id', serialize=False, to='registrocr.Ciudadano')),
                ('departamento', models.CharField(default=None, max_length=60, null=True, help_text=b'Este campo no es obligatorio ser\xc3\xa1 cargado directamente de la registraduria', blank=True)),
                ('municipio', models.CharField(default=None, max_length=60, null=True, help_text=b'Este campo no es obligatorio ser\xc3\xa1 cargado directamente de la registraduria', blank=True)),
                ('puesto', models.CharField(default=None, max_length=100, null=True, help_text=b'Este campo no es obligatorio ser\xc3\xa1 cargado directamente de la registraduria', blank=True)),
                ('mesa', models.CharField(default=None, max_length=3, null=True, help_text=b'Este campo no es obligatorio ser\xc3\xa1 cargado directamente de la registraduria', blank=True)),
            ],
        ),
    ]
