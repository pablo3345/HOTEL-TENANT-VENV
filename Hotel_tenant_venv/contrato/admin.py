
from django.contrib import admin
from .models import Huesped, Contrato

# Register your models here.


class adminHuesped(admin.ModelAdmin):
    
    readonly_fields=("created", "updated")
    
    list_display=("nombre_responsable", "apellido", "dni", "edad", "demas_huespedes", "patente_vehiculo", "modelo_vehiculo", "correo_electronico", "penalidad", "direccion", "localidad","codigo_postal", "pais", "created", "updated")
    
    search_fields=("nombre_responsable", "apellido")
    
    list_filter =("nombre_responsable", "apellido",)
    
    
    
    
class adminContrato(admin.ModelAdmin):
    readonly_fields=("created", "updated")
    list_display=("id", "habitacion", "huesped", "fecha_entrada", "fecha_salida", "importe_estadia", "importe_otros_gasto", "estado", "descuento_importe_noche", "descuento_total_calcularo", "aumento_total",  "total", "total_consumidos", "porcentaje_de_senia_reservas", "habitacion_reserva", "user")
    list_filter=("habitacion", "huesped")



admin.site.register(Huesped, adminHuesped)
admin.site.register(Contrato, adminContrato) 
    
    

