# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

class FILTER(object):
	ALL = 0
	NULLS = 1
	EMPTY = 2

lst_ciudades = ( ('1','ESPINAL'), ('2','CHICORAL'))
lst_rol = ( ('0',''),('1','P. INF'), )

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
	reunion = models.BooleanField(default = False, help_text = 'Indica si ya ha realizado reunión')
	fecha_reunion = models.DateField(null = True, blank = True)

	class Meta:
		verbose_name_plural = "Lideres"

	def save(self, *args, **kwargs):
		try:
			c = Ciudadano.objects.get( documento = self.documento )
		except Ciudadano.DoesNotExist:
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


	def nulos(self):
		return "<a href='/admin/registrocr/ciudadano/?q=%d&votante=n'>%d</a>" % ( self.documento , Ciudadano.objects.filter(municipio__isnull = True, lider = self).count()  )

	nulos.allow_tags = True


	def otra_ciudad(self, ciudad = 'ESPINAL'):
		
		return "<a href='/admin/registrocr/ciudadano/?q=%d&otraciudad=y'>%d</a>" % ( self.documento , Ciudadano.objects.filter(lider = self).exclude(municipio__icontains = ciudad).exclude(municipio__isnull = True).count()  )

	otra_ciudad.allow_tags = True

    

	

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
	llamada = models.BooleanField(default = False, verbose_name='Call',help_text='Indique si ya realizo el telemercadeo a este votante')
	candidatos =  models.ManyToManyField(Candidato, null = True, blank = True,)
	observaciones = models.CharField( max_length = 60, null = True, blank = True,)

	departamento = models.CharField(max_length = 60, null = True, blank = True, default= None, help_text="Este campo no es obligatorio será cargado directamente de la registraduria")
	municipio = models.CharField(max_length = 60, null = True, blank = True, default= None, help_text="Este campo no es obligatorio será cargado directamente de la registraduria")
	puesto = models.CharField(max_length = 100, null = True, default= None, blank = True, help_text="Este campo no es obligatorio será cargado directamente de la registraduria")
	direccion_puesto = models.CharField(max_length = 60, default= None, null = True, blank = True,help_text="Este campo no es obligatorio será cargado directamente de la registraduria")
	mesa = models.CharField(max_length = 3, default= None,null = True, blank = True, help_text="Este campo no es obligatorio será cargado directamente de la registraduria")
	rol = models.CharField(max_length = 1, choices = lst_rol, default = '0' )

	
	def save(self, *args, **kwargs):
		import requests
		from bs4 import BeautifulSoup
		url = "http://www3.registraduria.gov.co/censo/_censoresultado.php?nCedula=%d" % self.documento

		req = requests.get(url)
		statusCode = req.status_code
		if statusCode == 200:
			html = BeautifulSoup(req.text)
			try:
				self.departamento = html.find_all('tr')[0].find_all('td')[1].getText().strip()
			except:
				self.departamento = None
			try:
				self.municipio = html.find_all('tr')[1].find_all('td')[1].getText().strip()
			except:
				self.municipio = None

			try:
				self.puesto = html.find_all('tr')[2].find_all('td')[1].getText().strip()
			except:
				self.puesto = None

			try:
				self.direccion_puesto = html.find_all('tr')[3].find_all('td')[1].getText().strip()
			except:
				self.direccion_puesto = None

			try:
				self.mesa = html.find_all('tr')[5].find_all('td')[1].getText().strip()
			except:
				self.mesa = None

		
		super(Ciudadano ,self).save(args, kwargs)

		url ="http://190.60.255.25:81/Registraduria/vista/jurados_files/consultar_jurados.php?cedula=%d" % self.documento
		req = requests.get(url)
		statusCode = req.status_code
			
		if statusCode == 200:
			html = BeautifulSoup(req.text)
			j = None
			try:
				html = html.find_all('table')[1]
			except:
				return
			try:
				j = Jurado.objects.get(id = self)
			except Jurado.DoesNotExist:
				j = Jurado()

			j.id = self
			j.departamento = html.find_all('tr')[0].find_all('td')[1].getText().strip() 
			j.municipio = html.find_all('tr')[1].find_all('td')[1].getText().strip() 
			j.puesto = html.find_all('tr')[2].find_all('td')[1].getText().strip() 
			j.mesa = html.find_all('tr')[3].find_all('td')[1].getText().strip() 
			j.save()



	@staticmethod
	def sincronize(filter = FILTER.NULLS):
		
		import requests
		from bs4 import BeautifulSoup
		if filter == FILTER.NULLS:
			ciudadanos = Ciudadano.objects.filter(mesa__isnull = True)
		elif filter == FILTER.EMPTY:
			ciudadanos = Ciudadano.objects.filter(mesa = '')
		elif filter == FILTER.ALL:
			ciudadanos = Ciudadano.objects.filter()


		for c in ciudadanos:
			
			url = "http://www3.registraduria.gov.co/censo/_censoresultado.php?nCedula=%d" % c.documento
			
			req = requests.get(url)
			statusCode = req.status_code
			if statusCode == 200:
				html = BeautifulSoup(req.text)
				try:
					c.departamento = html.find_all('tr')[0].find_all('td')[1].getText()
				except:
					pass
				try:
					c.municipio = html.find_all('tr')[1].find_all('td')[1].getText()
				except:
					pass
				try:
					c.puesto = html.find_all('tr')[2].find_all('td')[1].getText()
				except:
					pass
				try:
					c.direccion_puesto = html.find_all('tr')[3].find_all('td')[1].getText()
				except:
					pass
				try:
					c.mesa = html.find_all('tr')[5].find_all('td')[1].getText()
				except:
					pass
				c.save()

			url ="http://190.60.255.25:81/Registraduria/vista/jurados_files/consultar_jurados.php?cedula=%d" % c.documento
			req = requests.get(url)
			statusCode = req.status_code
			
			if statusCode == 200:
				html = BeautifulSoup(req.text)
				j = None
				try:
					html = html.find_all('table')[1]
				except:
					continue
				try:
					j = Jurado.objects.get(id = c)
				except Jurado.DoesNotExist:
					j = Jurado()

				j.id = c
				j.departamento = html.find_all('tr')[0].find_all('td')[1].getText().strip() 
				j.municipio = html.find_all('tr')[1].find_all('td')[1].getText().strip() 
				j.puesto = html.find_all('tr')[2].find_all('td')[1].getText().strip() 
				j.mesa = html.find_all('tr')[3].find_all('td')[1].getText().strip() 
				j.save()

				




	def __unicode__(self):
		return self.get_full_name()

	def get_full_name(self):
		return u"%s %s" % ( self.nombres, self.apellidos)

	get_full_name.short_description = 'Nombre'

	def es_jurado(self):
		return Jurado.objects.filter(id = self.id).exists()
	es_jurado.boolean = True
	es_jurado.short_description = 'Jur.'



class Jurado(models.Model):
	id = models.OneToOneField(Ciudadano, primary_key=True, db_column='id')
	departamento = models.CharField(max_length = 60, null = True, blank = True, default= None, help_text="Este campo no es obligatorio será cargado directamente de la registraduria")
	municipio = models.CharField(max_length = 60, null = True, blank = True, default= None, help_text="Este campo no es obligatorio será cargado directamente de la registraduria")
	puesto = models.CharField(max_length = 100, null = True, default= None, blank = True, help_text="Este campo no es obligatorio será cargado directamente de la registraduria")
	mesa = models.CharField(max_length = 3, default= None,null = True, blank = True, help_text="Este campo no es obligatorio será cargado directamente de la registraduria")

	
