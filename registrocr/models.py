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

	def votantes(self):
		return "<a href='/admin/registrocr/ciudadano/?q=%d'>%d</a>" % ( self.documento , Ciudadano.objects.filter(lider = self).count()  )

	votantes.allow_tags = True
    votantes.admin_order_field = "votantes"

	

class Ciudadano(models.Model):

	nombres = models.CharField(max_length = 40)
	apellidos = models.CharField(max_length = 40)
	documento = models.BigIntegerField(unique=True)
	direccion = models.CharField(max_length = 50)
	correo =  models.EmailField(max_length=70,blank=True, null = True)
	ciudad = models.ForeignKey(Ciudad)
	fecha_cumpleanios = models.DateField( verbose_name = 'Fecha de cumpleaños (dd/mm/yyyy), si no se tiene al año de nacimiento ingrese el actual')
	telefono = models.BigIntegerField()
	lider = models.ForeignKey(Lider)
	colaborador = models.CharField(max_length = 60, null = True, blank = True)
	#candidato =  models.ForeignKey(Candidato)
	departamento = models.CharField(max_length = 60, null = True, blank = True, editable = False)
	municipio = models.CharField(max_length = 60, null = True, blank = True, editable = False)
	puesto = models.CharField(max_length = 100, null = True, blank = True, editable = False)
	direccion_puesto = models.CharField(max_length = 60, null = True, blank = True, editable = False)
	mesa = models.CharField(max_length = 3, null = True, blank = True, editable = False)

	def save(self, *args, **kwargs):
		import requests
		from bs4 import BeautifulSoup
		url = "http://www3.registraduria.gov.co/censo/_censoresultado.php?nCedula=%d" % self.documento

		req = requests.get(url)
		statusCode = req.status_code
		if statusCode == 200:
			try:
				html = BeautifulSoup(req.text)
				self.departamento = html.find_all('tr')[0].find_all('td')[1].getText()
				self.municipio = html.find_all('tr')[1].find_all('td')[1].getText()
				self.puesto = html.find_all('tr')[2].find_all('td')[1].getText()
				self.direccion_puesto = html.find_all('tr')[3].find_all('td')[1].getText()
				self.mesa = html.find_all('tr')[5].find_all('td')[1].getText()
			except:
				pass

		super(Ciudadano ,self).save(args, kwargs)

	def __unicode__(self):
		return self.get_full_name()

	def get_full_name(self):
		return u"%s %s" % ( self.nombres, self.apellidos)

	get_full_name.short_description = 'Nombre'
	
