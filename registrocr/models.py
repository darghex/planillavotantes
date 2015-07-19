# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

lst_ciudades = ( ('1','ESPINAL'), ('2','CHICORAL'))


class Candidato(models.Model):

	nombres = models.CharField(max_length = 40)
	apellidos = models.CharField(max_length = 40)
	perfil = models.CharField(max_length = 1, choices = (('1', 'CONCEJO'),), default = '1' )
	numero_tarjeton = models.SmallIntegerField()

	def __unicode__(self):
		return self.get_full_name()

	def get_full_name(self):
		return u"%s %s" % ( self.nombres, self.apellidos)


class Ciudadano(models.Model):

	nombres = models.CharField(max_length = 40)
	apellidos = models.CharField(max_length = 40)
	documento = models.IntegerField(unique=True, validators=[RegexValidator(regex='^\d{10}$', message='Documento no es correcto', code='Invalid number')])
	direccion = models.CharField(max_length = 50)
	correo =  models.EmailField(max_length=70,blank=True, null = True)
	ciudad = models.CharField(max_length = 1, choices = lst_ciudades )
	telefono = models.IntegerField(unique=True, validators=[RegexValidator(regex='^\d{10}$', message='Documento no es correcto', code='Invalid number')])
	fecha_cumpleanios = models.DateField( verbose_name = 'Fecha de cumpleaños')
	lider = models.ForeignKey(User, editable =  False)
	candidato =  models.ForeignKey(Candidato )

	def __unicode__(self):
		return self.get_full_name()

	def get_full_name(self):
		return u"%s %s" % ( self.nombres, self.apellidos)

	get_full_name.short_description = 'Nombre'

	def get_lider_full_name(self):
		return u"%s" % self.lider.get_full_name()

	get_lider_full_name.short_description = 'Lider'

