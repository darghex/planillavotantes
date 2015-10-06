# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registrocr', '0005_auto_20150915_0721'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lider',
            options={'verbose_name_plural': 'Lideres'},
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
    ]
