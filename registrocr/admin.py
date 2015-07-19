from django.contrib import admin
from models import Ciudadano, Candidato

@admin.register(Ciudadano)
class CiudadanoAdmin(admin.ModelAdmin):
	list_display = ('get_full_name', 'documento', 'correo', 'telefono', 'fecha_cumpleanios', 'get_lider_full_name', 'candidato')
	search_fields = ('nombres','apellidos','documento')

	def save_model(self, request, obj, form, change):
		obj.lider = request.user
		obj.save()


	def get_queryset (self, request):
		if request.user.is_superuser:
			return Ciudadano.objects.all()
		return Ciudadano.objects.filter( lider = request.user)


@admin.register(Candidato)
class CandidatoAdmin(admin.ModelAdmin):
	list_display = ('get_full_name','perfil','numero_tarjeton')