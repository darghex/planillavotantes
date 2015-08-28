from django.contrib import admin
from models import Ciudadano, Ciudad, Categoria, Lider


from import_export import resources


class LiderResource(resources.ModelResource):

    class Meta:
        model = Lider
        fields = ('nombres', 'apellidos', 'documento,', 'direccion', 'correo', 'ciudad__ciudad','telefono', 'grupo__descripcion', 'votantes')


class CiudadanoResource(resources.ModelResource):

    class Meta:
        model = Ciudadano
        fields = ('nombres', 'apellidos', 'documento,', 'direccion', 'correo', 'ciudad__ciudad','telefono', 'fecha_cumpleanios','lider__nombres', 'lider_apellidos', 'colaborador', 'departamento', 'municipio', 'puesto',
        'direccion_puesto', 'mesa')



from import_export.admin import ImportExportActionModelAdmin




class RegistraduriaFilter(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = 'Tiene puesto de votacion'

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'votante'

    def lookups(self, request, model_admin):
        
        return (
            ('y', 'Si'),
            ('n', 'No'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'y':
            return queryset.exclude(mesa__isnull = True)
        if self.value() == 'n':
            return queryset.filter(mesa__isnull = True) 



@admin.register(Ciudadano)
class CiudadanoAdmin(ImportExportActionModelAdmin):
	list_display = ('get_full_name', 'documento', 'correo', 'telefono', 'direccion', 'lider','puesto', 'mesa')
	search_fields = ('nombres','apellidos','documento', 'lider__nombres', 'lider__apellidos', 'lider__documento')
	resource_class = CiudadanoResource
	list_filter = (RegistraduriaFilter,)


	"""
	def save_model(self, request, obj, form, change):
		obj.lider = request.user
		obj.save()
	"""

	"""
	def get_queryset (self, request):
		if request.user.is_superuser:
			return Ciudadano.objects.all()
		return Ciudadano.objects.filter( lider = request.user)
	"""


class VotantesFilter(admin.SimpleListFilter):
    title = 'Tiene Votantes'

    parameter_name = 'votantes'

    def lookups(self, request, model_admin):
        
        return (
            ('y', 'Si'),
            ('n', 'No'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'y':
            return queryset.filter(ciudadano__isnull = False).distinct()
        if self.value() == 'n':
            return queryset.filter(ciudadano__isnull = True).distinct()


@admin.register(Lider)
class LiderAdmin(ImportExportActionModelAdmin):
    list_display = ('get_full_name', 'documento', 'correo', 'telefono', 'direccion', 'grupo','votantes')
    search_fields = ('nombres','apellidos','documento', 'grupo__descripcion')
    resource_class = LiderResource
    list_filter = (VotantesFilter,)

"""
@admin.register(Candidato)
class CandidatoAdmin(admin.ModelAdmin):
	list_display = ('get_full_name','perfil','numero_tarjeton')
"""

@admin.register(Ciudad)
class CiudadAdmin(admin.ModelAdmin):
	pass

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
	pass
