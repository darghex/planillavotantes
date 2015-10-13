from django.contrib import admin
from models import Ciudadano, Ciudad, Categoria, Lider, Candidato, Jurado


from import_export import resources


class LiderResource(resources.ModelResource):

    class Meta:
        model = Lider
        fields = ('nombres', 'apellidos', 'documento,', 'direccion', 'correo', 'ciudad__ciudad','telefono', 'grupo__descripcion', 'reunion', 'fecha_reunion')


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
            return queryset.exclude(puesto__isnull = True)
        if self.value() == 'n':
            return queryset.filter(puesto__isnull = True) 


class JuradoFilter(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = 'Es Jurado'

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'jurado'

    def lookups(self, request, model_admin):
        
        return (
            ('y', 'Si'),
            ('n', 'No'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'y':
            return queryset.filter( id__in = Jurado.objects.all())
        if self.value() == 'n':
            return queryset.exclude( id__in = Jurado.objects.all()) 

class FueraCiudadFilter(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = 'Fuera de la Ciudad'

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'otraciudad'

    def lookups(self, request, model_admin):
        
        return (
            ('y', 'Si'),
            ('n', 'No'),
        )

    def queryset(self, request, queryset):
        ciudad = u'ESPINAL'
        
        if self.value() == 'y':
            return queryset.exclude(municipio__icontains = ciudad).exclude(municipio__isnull = True)
        if self.value() == 'n':
            return queryset.filter(municipio__icontains  = ciudad,)

class JuradoInline(admin.TabularInline):
    model = Jurado
    verbose_name = "Es Jurado"
    verbose_name_plural = "Es Jurado"
    extra = 0
    readonly_fields = ('departamento', 'municipio','puesto','mesa')

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Ciudadano)
class CiudadanoAdmin(ImportExportActionModelAdmin):
    
    fieldsets = (( None, { 'fields': ( ('nombres', 'apellidos'), 'documento',('telefono', 'correo'),('direccion', 'ciudad'),('lider','colaborador'),'llamada','candidatos','observaciones') }),
        ('Informacion de votacion', { 'classes': ('collapse',),
                    'fields': ('departamento', 'municipio','puesto','direccion_puesto','mesa')
        }),
        )
    list_display = ('get_full_name', 'documento',  'telefono',  'lider', 'municipio' ,'puesto', 'mesa','llamada','es_jurado','rol')
    search_fields = ('nombres','apellidos','documento', 'lider__nombres', 'lider__apellidos', 'lider__documento')

    resource_class = CiudadanoResource
    list_filter = (RegistraduriaFilter,FueraCiudadFilter, JuradoFilter, 'lider__grupo__descripcion', 'rol','llamada')
    filter_horizontal = ('candidatos', )
    inlines = (JuradoInline,)
    readonly_fields = ('departamento', 'municipio','puesto','direccion_puesto','mesa')

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

    def asignar_punto(self, request, queryset):
        queryset.update(rol=1)    
    asignar_punto.short_description = "Asignar P. de Informacion (seleccionados)"
    
    def desasignar(self, request, queryset):
        queryset.update(rol=0)        
    desasignar.short_description = "Sin rol (Seleccionados)"

    actions = [ asignar_punto, desasignar ]

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
    list_display = ('get_full_name', 'documento', 'telefono',  'grupo','votantes', 'nulos','otra_ciudad', 'reunion')
    search_fields = ('nombres','apellidos','documento', 'grupo__descripcion', 'reunion',)
    resource_class = LiderResource
    list_filter = (VotantesFilter,)


@admin.register(Candidato)
class CandidatoAdmin(admin.ModelAdmin):
	list_display = ('get_full_name','perfil')


@admin.register(Ciudad)
class CiudadAdmin(admin.ModelAdmin):
	pass

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
	pass
