# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
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
            name='Categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ciudad', models.CharField(max_length=50)),
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
                ('fecha_cumpleanios', models.DateField(verbose_name=b'Fecha de cumplea\xc3\xb1os (dd/mm/yyyy), si no se tiene al a\xc3\xb1o de nacimiento ingrese el actual')),
                ('telefono', models.BigIntegerField(unique=True, validators=[django.core.validators.RegexValidator(regex=b'^\\d{10}$', message=b'Telefono correcto', code=b'Invalid number')])),
                ('colaborador', models.CharField(max_length=60, null=True, blank=True)),
                ('ciudad', models.ForeignKey(to='registrocr.Ciudad')),
            ],
        ),
        migrations.CreateModel(
            name='Lider',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombres', models.CharField(max_length=40)),
                ('apellidos', models.CharField(max_length=40)),
                ('documento', models.BigIntegerField(unique=True, validators=[django.core.validators.RegexValidator(regex=b'^\\d{10}$', message=b'Documento no es correcto', code=b'Invalid number')])),
                ('direccion', models.CharField(max_length=50)),
                ('correo', models.EmailField(max_length=70, null=True, blank=True)),
                ('telefono', models.BigIntegerField(unique=True, validators=[django.core.validators.RegexValidator(regex=b'^\\d{10}$', message=b'Telefono correcto', code=b'Invalid number')])),
                ('ciudad', models.ForeignKey(to='registrocr.Ciudad')),
                ('grupo', models.ForeignKey(to='registrocr.Categoria')),
            ],
        ),
        migrations.AddField(
            model_name='ciudadano',
            name='lider',
            field=models.ForeignKey(to='registrocr.Lider'),
        ),
    ]
