from django.contrib import admin
from .models import Proveedores, Insumos, Producto_al_publico, Agregar_productos

# Register your models here.

class adminProveedores(admin.ModelAdmin):
    
    readonly_fields=("created", "updated")
    
    list_display=("nombre_proveedor", "apellido", "direccion", "telefono", "mail", "nombre_empresa", "algun_otro_dato",  "created", "updated")
    
    
    
class adminInsumos(admin.ModelAdmin):
    readonly_fields=("created", "updated")
    
    list_display=("nombre_insumos", "marca_insumos", "precio", "medida", "proveedor", "algun_otro_dato", "disponibilidad",  "created", "updated")
    
    
class adminProducto(admin.ModelAdmin):
     readonly_fields=("created", "updated")
    
     list_display=("nombre_producto", "marca_producto", "precio_al_publico", "precio_de_costo", "medida", "proveedor", "disponibilidad" ,"algun_otro_dato",  "created", "updated", "eliminado")
     

class adminProductos_agregados(admin.ModelAdmin):
    # readonly_fields=("created")
    
     list_display=("id", "producto", "contrato", "cantidad", "total", "created")
    
    
    
    



admin.site.register(Proveedores, adminProveedores)
admin.site.register(Insumos, adminInsumos)
admin.site.register(Producto_al_publico, adminProducto)
admin.site.register(Agregar_productos, adminProductos_agregados)

