# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('registrocr', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ciudadano',
            name='documento',
            field=models.BigIntegerField(unique=True, validators=[django.core.validators.RegexValidator(regex=b'^\\d{8}$', message=b'Documento no es correcto', code=b'Invalid number')]),
        ),
        migrations.AlterField(
            model_name='lider',
            name='documento',
            field=models.BigIntegerField(unique=True, validators=[django.core.validators.RegexValidator(regex=b'^\\d{8}$', message=b'Documento no es correcto', code=b'Invalid number')]),
        ),
    ]
