# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registrocr', '0003_auto_20150915_0549'),
    ]

    operations = [
        migrations.AddField(
            model_name='ciudadano',
            name='candidatos',
            field=models.ManyToManyField(to='registrocr.Candidato'),
        ),
        migrations.AddField(
            model_name='ciudadano',
            name='observaciones',
            field=models.CharField(max_length=60, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='ciudadano',
            name='llamada',
            field=models.BooleanField(default=False, help_text=b'Indique si ya realizo el telemercadeo a este votante'),
        ),
    ]
