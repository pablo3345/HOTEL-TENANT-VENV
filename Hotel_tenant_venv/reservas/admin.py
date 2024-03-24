from django.contrib import admin
from .models import Reserva, HuespedReserva

# Register your models here.

class adminReservas(admin.ModelAdmin):
    
    readonly_fields=("created", "updated")
    
    list_display=("id", "habitacion", "huesped", "estado", "cancelar","fecha_entrada", "fecha_salida",  "descuento_importe_noche", "descuento_total_calcularo", "aumento_total", "porcentaje_de_senia",
                  "total_senia", "created", "updated")
    
    


class adminHuesped(admin.ModelAdmin):
    
    readonly_fields=("created", "updated")
    
    list_display=("nombre", "apellido",  "created", "updated")
    
    
admin.site.register(Reserva, adminReservas)
admin.site.register(HuespedReserva, adminHuesped)




