from django.contrib import admin
from .models import Cabañas
from .models import Promociones
from .models import Reservacion

# Register your models here.
class AdministrarModelo(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('clave', 'nombre', 'costoDia','numPersonas','numCamas',)
    search_fields = ('clave', 'nombre', 'costoDia', 'servicios')
    date_hierarchy = 'created'
    list_filter = ('costoDia','numPersonas')
    list_per_page=1
    
admin.site.register(Cabañas,AdministrarModelo)


class AdministrarPromociones(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('validez', 'nombre', 'promo')
    search_fields = ('nombre', 'promo')
    date_hierarchy = 'created'
    list_filter = ('validez','nombre')
    list_per_page=1

admin.site.register(Promociones,AdministrarPromociones)


class AdministrarReservacion(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


admin.site.register(Reservacion,AdministrarReservacion)