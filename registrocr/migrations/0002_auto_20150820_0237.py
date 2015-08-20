# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registrocr', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ciudadano',
            name='departamento',
            field=models.CharField(max_length=60, null=True, editable=False, blank=True),
        ),
        migrations.AddField(
            model_name='ciudadano',
            name='direccion_puesto',
            field=models.CharField(max_length=60, null=True, editable=False, blank=True),
        ),
        migrations.AddField(
            model_name='ciudadano',
            name='mesa',
            field=models.CharField(max_length=3, null=True, editable=False, blank=True),
        ),
        migrations.AddField(
            model_name='ciudadano',
            name='municipio',
            field=models.CharField(max_length=60, null=True, editable=False, blank=True),
        ),
        migrations.AddField(
            model_name='ciudadano',
            name='puesto',
            field=models.CharField(max_length=100, null=True, editable=False, blank=True),
        ),
    ]
