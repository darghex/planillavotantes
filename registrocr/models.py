# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

lst_ciudades = ( ('1','ESPINAL'), ('2','CHICORAL'))

class Ciudad(models.Model):
	ciudad = models.CharField(max_length = 50)

	def __unicode__(self):
		return self.ciudad


class Candidato(models.Model):

	nombres = models.CharField(max_length = 40)
	apellidos = models.CharField(max_length = 40)
	perfil = models.CharField(max_length = 1, choices = (('1', 'CONCEJO'),), default = '1' )
	numero_tarjeton = models.SmallIntegerField()

	def __unicode__(self):
		return self.get_full_name()

	def get_full_name(self):
		return u"%s %s" % ( self.nombres, self.apellidos)


class Categoria(models.Model):
	descripcion = models.CharField(max_length = 50)

	def __unicode__(self):
		return self.descripcion

class Lider(models.Model):

	nombres = models.CharField(max_length = 40)
	apellidos = models.CharField(max_length = 40)
	documento = models.BigIntegerField(unique=True)
	direccion = models.CharField(max_length = 50)
	correo =  models.EmailField(max_length=70,blank=True, null = True)
	ciudad = models.ForeignKey(Ciudad)
	telefono = models.BigIntegerField(unique=True)
	grupo = models.ForeignKey(Categoria)
	

	def __unicode__(self):
		return self.get_full_name()

	def get_full_name(self):
		return u"%s %s" % ( self.nombres, self.apellidos)

	get_full_name.short_description = 'Nombre'

	

class Ciudadano(models.Model):

	nombres = models.CharField(max_length = 40)
	apellidos = models.CharField(max_length = 40)
	documento = models.BigIntegerField(unique=True)
	direccion = models.CharField(max_length = 50)
	correo =  models.EmailField(max_length=70,blank=True, null = True)
	ciudad = models.ForeignKey(Ciudad)
	fecha_cumpleanios = models.DateField( verbose_name = 'Fecha de cumpleaños (dd/mm/yyyy), si no se tiene al año de nacimiento ingrese el actual')
	telefono = models.BigIntegerField(unique=True)
	lider = models.ForeignKey(Lider)
	colaborador = models.CharField(max_length = 60, null = True, blank = True)
	#candidato =  models.ForeignKey(Candidato)

	def __unicode__(self):
		return self.get_full_name()

	def get_full_name(self):
		return u"%s %s" % ( self.nombres, self.apellidos)

	get_full_name.short_description = 'Nombre'
	