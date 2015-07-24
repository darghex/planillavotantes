# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidato',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombres', models.CharField(max_length=40)),
                ('apellidos', models.CharField(max_length=40)),
                ('perfil', models.CharField(default=b'1', max_length=1, choices=[(b'1', b'CONCEJO')])),
                ('numero_tarjeton', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Ciudadano',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombres', models.CharField(max_length=40)),
                ('apellidos', models.CharField(max_length=40)),
                ('documento', models.BigIntegerField(unique=True, validators=[django.core.validators.RegexValidator(regex=b'^\\d{10}$', message=b'Documento no es correcto', code=b'Invalid number')])),
                ('direccion', models.CharField(max_length=50)),
                ('correo', models.EmailField(max_length=70, null=True, blank=True)),
                ('ciudad', models.CharField(max_length=1, choices=[(b'1', b'ESPINAL'), (b'2', b'CHICORAL')])),
                ('telefono', models.BigIntegerField(unique=True, validators=[django.core.validators.RegexValidator(regex=b'^\\d{10}$', message=b'Telefono es correcto', code=b'Invalid number')])),
                ('fecha_cumpleanios', models.DateField(verbose_name=b'Fecha de cumplea\xc3\xb1os (dd/mm/yyyy), si no se tiene al a\xc3\xb1o de nacimiento ingrese el actual')),
                ('candidato', models.ForeignKey(to='registrocr.Candidato')),
                ('lider', models.ForeignKey(editable=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
