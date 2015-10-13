# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registrocr', '0003_jurado'),
    ]

    operations = [
        migrations.AddField(
            model_name='ciudadano',
            name='rol',
            field=models.CharField(default=b'0', max_length=1, choices=[(b'0', b''), (b'1', b'PUESTO INF.')]),
        ),
    ]
