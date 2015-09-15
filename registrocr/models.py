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
	lst_perfiles = (('1', 'CONCEJO'), ('2', 'ALCALDIA'), ('3', 'ASAMBLEA'), ('4', 'GOBERNACION'))
	nombres = models.CharField(max_length = 40)
	apellidos = models.CharField(max_length = 40)
	perfil = models.CharField(max_length = 1, choices = lst_perfiles, default = '1' )
	

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

	def save(self, *args, **kwargs):
		c = Ciudadano()
		c.nombres = self.nombres
		c.apellidos = self.apellidos
		c.documento = self.documento
		c.direccion = self.direccion
		c.correo = self.correo
		c.ciudad = self.ciudad
		c.telefono = self.telefono
		super(Lider ,self).save(args, kwargs)
		c.lider = self
		c.save()

		

	def __unicode__(self):
		return self.get_full_name()

	def get_full_name(self):
		return u"%s %s" % ( self.nombres, self.apellidos)

	get_full_name.short_description = 'Nombre'

	def votantes(self):
		return "<a href='/admin/registrocr/ciudadano/?q=%d'>%d</a>" % ( self.documento , Ciudadano.objects.filter(lider = self).count()  )

	votantes.allow_tags = True
    

	

class Ciudadano(models.Model):

	nombres = models.CharField(max_length = 40)
	apellidos = models.CharField(max_length = 40)
	documento = models.BigIntegerField(unique=True)
	direccion = models.CharField(max_length = 50)
	correo =  models.EmailField(max_length=70,blank=True, null = True)
	ciudad = models.ForeignKey(Ciudad)
	fecha_cumpleanios = models.DateField( verbose_name = 'Fecha de cumpleaños (dd/mm/yyyy), si no se tiene al año de nacimiento ingrese el actual',  auto_now_add=True)
	telefono = models.BigIntegerField()
	lider = models.ForeignKey(Lider)
	colaborador = models.CharField(max_length = 60, null = True, blank = True)
	llamada = models.BooleanField(default = False, help_text='Indique si ya realizo el telemercadeo a este votante')
	candidatos =  models.ManyToManyField(Candidato, null = True, blank = True,)
	observaciones = models.CharField( max_length = 60, null = True, blank = True,)

	departamento = models.CharField(max_length = 60, null = True, blank = True, default= None, help_text="Este campo no es obligatorio será cargado directamente de la registraduria")
	municipio = models.CharField(max_length = 60, null = True, blank = True, default= None, help_text="Este campo no es obligatorio será cargado directamente de la registraduria")
	puesto = models.CharField(max_length = 100, null = True, default= None, blank = True, help_text="Este campo no es obligatorio será cargado directamente de la registraduria")
	direccion_puesto = models.CharField(max_length = 60, default= None, null = True, blank = True,help_text="Este campo no es obligatorio será cargado directamente de la registraduria")
	mesa = models.CharField(max_length = 3, default= None,null = True, blank = True, help_text="Este campo no es obligatorio será cargado directamente de la registraduria")


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
				self.departamento = None
				self.municipio = None
				self.puesto = None
				self.direccion_puesto = None
				self.mesa = None

		super(Ciudadano ,self).save(args, kwargs)

	@staticmethod
	def sincronize():
		import requests
		from bs4 import BeautifulSoup
		ciudadanos = Ciudadano.objects.filter(mesa__isnull = True)
		for c in ciudadanos:
			
			url = "http://www3.registraduria.gov.co/censo/_censoresultado.php?nCedula=%d" % c.documento
			
			req = requests.get(url)
			statusCode = req.status_code
			if statusCode == 200:
				try:
					html = BeautifulSoup(req.text)
					c.departamento = html.find_all('tr')[0].find_all('td')[1].getText()
					c.municipio = html.find_all('tr')[1].find_all('td')[1].getText()
					c.puesto = html.find_all('tr')[2].find_all('td')[1].getText()
					c.direccion_puesto = html.find_all('tr')[3].find_all('td')[1].getText()
					c.mesa = html.find_all('tr')[5].find_all('td')[1].getText()
				except:
					pass
				c.save()


	def __unicode__(self):
		return self.get_full_name()

	def get_full_name(self):
		return u"%s %s" % ( self.nombres, self.apellidos)

	get_full_name.short_description = 'Nombre'
	
