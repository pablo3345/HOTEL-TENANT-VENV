from django.db import models
from contrato.models import Contrato
from django.db.models import F,Sum, FloatField  # para calcular el total de una orden de pedido



    

   

# Create your models here.

class Proveedores(models.Model):
    nombre_proveedor= models.CharField(max_length=40)
    apellido =models.CharField(max_length=40)
    direccion =models.CharField(max_length=40)
    telefono =models.CharField(max_length=40)
    mail =models.EmailField(null=True, blank=True)
    nombre_empresa =  models.CharField(max_length=40)
    algun_otro_dato = models.CharField(max_length=40, null = True, blank= True)
    created = models.DateTimeField(auto_now_add=True)  # aca guardamos la fecha que se creo un servicio
    updated = models.DateTimeField(auto_now=True)  # aca guardamos cuando se actualiza
    
    def __str__(self):
        return f'{self.nombre_proveedor}  {self.apellido} {self.nombre_empresa}' # la f es de formato
    
    class Meta:
        db_table = "proveedores"
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"
        ordering = ['id']  # significa que se va a ordenar por id
        
        
class Insumos(models.Model):
    
    nombre_insumos= models.CharField(max_length=40)
    marca_insumos = models.CharField(max_length=40)
    precio= models.FloatField()
    medida = models.FloatField()
    proveedor = models.ForeignKey(Proveedores, on_delete= models.CASCADE)
    algun_otro_dato = models.CharField(max_length=40, null = True, blank= True)
    disponibilidad = models.BooleanField(choices=((True, 'SI'), (False, 'NO')), default=1)
    created = models.DateTimeField(auto_now_add=True)  # aca guardamos la fecha que se creo un servicio
    updated = models.DateTimeField(auto_now=True)  # aca guardamos cuando se actualiza
    
    def __str__(self):
        return f'{self.nombre_insumos}  {self.marca_insumos}' 
    
    class Meta:
        db_table = "insumos"
        verbose_name = "Insumo"
        verbose_name_plural = "Insumos"
        ordering = ['id']  # significa que se va a ordenar por id
        
        
        
class Producto_al_publico(models.Model):
        
        
        nombre_producto= models.CharField(max_length=40)
        marca_producto = models.CharField(max_length=40)
        precio_al_publico = models.FloatField()
        precio_de_costo = models.FloatField()
        medida = models.FloatField()
        proveedor = models.ForeignKey(Proveedores, on_delete= models.CASCADE)
        disponibilidad = models.BooleanField(choices=((True, 'SI'), (False, 'NO')), default=1)
        #precio_promocion = models.FloatField(default = 0.0)
        algun_otro_dato = models.CharField(max_length=40, null = True, blank= True)
        created = models.DateTimeField(auto_now_add=True)  # aca guardamos la fecha que se creo un servicio
        updated = models.DateTimeField(auto_now=True)  # aca guardamos cuando se actualiza
        #--------------------------------------------
        eliminado = models.BooleanField(default=False)
        
        def __str__(self):
         return f'{self.nombre_producto} precio actualizado {self.precio_al_publico}' 
     
       
     
        class Meta:
         db_table = "producto_al_publico"
         verbose_name = "Producto al publico"
         verbose_name_plural = "Productos al publico"
         ordering = ['id']  # significa que se va a ordenar por id
        
        
        
  #-----------ACA PONER EL MODELO AGREGAR PRODUCTOS CONSUMIDOS----------      
    
    
        
class Agregar_productos(models.Model):
    
    
   
    
   
    
   # producto = models.ForeignKey(Producto_al_publico, on_delete= models.CASCADE, default=1)
    producto = models.ForeignKey(Producto_al_publico, on_delete= models.CASCADE, default=1)
    contrato = models.ForeignKey(Contrato, on_delete= models.CASCADE, default=1)
    cantidad = models.IntegerField()
    total = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    
   
   
    
    
    def __str__(self):
         return f'{self.producto}  {self.contrato}  {self.cantidad}'
     
    class Meta:
         db_table = "agregar_productos"
         verbose_name = "Agregar Producto"
         verbose_name_plural = "Agregar Productos"
        # ordering = ['id']  # significa que se va a ordenar por id
