from django.db import models
from habitacion.models import Habitacion


   

    

# Create your models here.

descuento_importeNoche = [(0, '0'),(5, '5'), (10, '10'), (15, '15'), (20, '20'), (25, '25'), (30, '30'),  (35, '35'),(40, '40'), (45, '45'), (50, '50'), (55, '55'), (60, '60'), (70, '70')] #es una tupla
 
descuento_importeTotal = [(0, '0'),(5, '5'), (10, '10'), (15, '15'), (20, '20'), (25, '25'), (30, '30'),  (35, '35'),(40, '40'), (45, '45'), (50, '50'), (55, '55'), (60, '60'), (70, '70')] #es una tupla

aumento_total = [(0, '0'),(4, '4'), (5, '5'), (10, '10'), (15, '15'), (20, '20'), (25, '25'), (30, '30'), (35, '35'), (40, '40'), (45, '45'), (50, '50')] #es una tupla

senia = [(0, '0'),(5, '5'), (10, '10'), (15, '15'), (20, '20'), (25, '25'), (30, '30'),  (35, '35'),(40, '40'), (45, '45'), (50, '50'), (55, '55'), (60, '60'), (70, '70')] #es una tupla
 


class HuespedReserva(models.Model):
     nombre = models.CharField(max_length=40)
     apellido= models.CharField(max_length=40)
     dni= models.CharField(max_length=40)
     telefono= models.CharField(max_length=40, null= True, blank=True)
     created = models.DateTimeField(auto_now_add=True)  # aca guardamos la fecha que se creo un servicio
     updated = models.DateTimeField(auto_now=True)  # aca guardamos cuando se actualiza
    
     
     def __str__(self):
        return f'{self.nombre}  {self.apellido} dni {self.dni}' # la f es de formato
    
     class Meta:
        db_table = "huespedReserva"
        verbose_name = "Huesped reserva"
        verbose_name_plural = "Huespedes reservas"
        ordering = ['id']  # significa que se va a ordenar por id
        
        
class Reserva(models.Model):
    habitacion = models.ForeignKey(Habitacion, on_delete= models.CASCADE)
    huesped = models.ForeignKey(HuespedReserva, on_delete= models.CASCADE) #con default=1 en el select, me borra esa linea discontinua que aparece
    fecha_entrada= models.DateTimeField(auto_now=False)
    fecha_salida =models.DateTimeField(auto_now=False)
    estado = models.BooleanField()
    
    cancelar = models.CharField(max_length=4, choices=(('NO', 'NO'), ('SI', 'SI')), default="NO")
    
    importe_estadia = models.FloatField() # poner en un casillero el total del precio de la habitacion x noche
    importe_otros_gasto = models.FloatField(default=0.0)
   # late_chack_out = models.CharField(max_length=4, choices=(('SI', 'SI'), ('NO', 'NO')), default=1)
    
    total = models.FloatField()
  
    #-------------------%--------------------------
    descuento_importe_noche= models.IntegerField( null= False, blank=False, choices=descuento_importeNoche, default= 1)
    descuento_total_calcularo=models.IntegerField(null= False, blank=False, choices=descuento_importeTotal, default=1)
    
    aumento_total=models.IntegerField(null= False, blank=False, choices=aumento_total, default=1)
    
    porcentaje_de_senia=models.IntegerField(null= False, blank=False, choices=senia, default=1)
    total_senia = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)  # aca guardamos la fecha que se creo un servicio
    updated = models.DateTimeField(auto_now=True)  # aca guardamos cuando se actualiza
    
    
    def __str__(self):
        return f'{self.habitacion}  {self.huesped} {self.fecha_entrada} {self.fecha_salida}' # la f es de formato
    
    
    class Meta:
        db_table = "reserva"
        verbose_name = "Reserva"
        verbose_name_plural = "Reservas"
        ordering = ['id'] # significa que se va a ordenar por id ----------volver atrassss----------------------