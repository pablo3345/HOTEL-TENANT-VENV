from django.db import models
from habitacion.models import Habitacion
import datetime
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model



#from django.contrib import messages
#from django.shortcuts import redirect
#from contrato.models import Huesped, Contrato


User = get_user_model() # nos va a devolver el usuario que esta logeado, el usauario activo

 #Create your models here.
 
descuento_importeNoche = [(0, '0'),(5, '5'), (10, '10'), (15, '15'), (20, '20'), (25, '25'), (30, '30'),  (35, '35'),(40, '40'), (45, '45'), (50, '50'), (55, '55'), (60, '60'), (70, '70')] #es una tupla
 
descuento_importeTotal = [(0, '0'),(5, '5'), (10, '10'), (15, '15'), (20, '20'), (25, '25'), (30, '30'),  (35, '35'),(40, '40'), (45, '45'), (50, '50'), (55, '55'), (60, '60'), (70, '70')] #es una tupla

aumento_total = [(0, '0'),(4, '4'), (5, '5'), (10, '10'), (15, '15'), (20, '20'), (25, '25'), (30, '30'), (35, '35'), (40, '40'), (45, '45'), (50, '50')] #es una tupla

iva=[(0,'0'), (21, '21')]

class Huesped(models.Model):
     
    nombre_responsable =models.CharField(max_length=40)
    apellido =models.CharField(max_length=40)
    edad =models.IntegerField()
    dni= models.CharField(max_length=20)
    #-------------------------------------
    direccion =models.CharField(max_length=40)
    localidad =models.CharField(max_length=40)
    codigo_postal =models.CharField(max_length=40)
    pais =models.CharField(max_length=40)
    #----------------------------------------
    telefono= models.CharField(max_length=40, null= True, blank=True)
    #----------------------------------------
    demas_huespedes = models.CharField(max_length= 1500,  null= True, blank=True)
    patente_vehiculo= models.CharField(max_length=20,  null= True, blank=True)
    modelo_vehiculo= models.CharField(max_length=40,  null= True, blank=True)
    correo_electronico = models.EmailField(null=True, blank=True)
    penalidad = models.CharField(max_length=4, choices=(('SI', 'SI'), ('NO', 'NO')), default='NO')
    created = models.DateTimeField(auto_now_add=True)  # aca guardamos la fecha que se creo un servicio
    updated = models.DateTimeField(auto_now=True)  # aca guardamos cuando se actualiza
    
    def __str__(self):
        return f'{self.nombre_responsable}  {self.apellido} dni {self.dni}' # la f es de formato

    class Meta:
        db_table = "huesped"
        verbose_name = "Huesped"
        verbose_name_plural = "Huespedes"
        ordering = ['id']  # significa que se va a ordenar por id
        
   
    
    


#----volver atras---...
class Contrato(models.Model):
  
  
   
    
    habitacion = models.ForeignKey(Habitacion, on_delete= models.CASCADE)
    huesped = models.ForeignKey(Huesped, on_delete= models.CASCADE) #con default=1 en el select, me borra esa linea discontinua que aparece
    fecha_entrada= models.DateTimeField(auto_now=False)
    fecha_salida =models.DateTimeField(auto_now=False)
    importe_estadia = models.FloatField() # poner en un casillero el total del precio de la habitacion x noche
    importe_otros_gasto = models.FloatField(default=0.0)
   
    # late_chack_out = models.CharField(max_length=4, choices=(('SI', 'SI'), ('NO', 'NO')), default=1)
    total = models.FloatField(default=0) # le puse default cero para las senia de reservas
    estado = models.BooleanField()
    #---------------------------------------------
   
    #-------------------volver atras----------------------------------------------------------------------
    descuento_importe_noche= models.IntegerField( null= False, blank=False, choices=descuento_importeNoche, default= 1)
    descuento_total_calcularo=models.IntegerField(null= False, blank=False, choices=descuento_importeTotal, default=1)
    
    aumento_total=models.IntegerField(null= False, blank=False, choices=aumento_total, default=1)
    total_consumidos = models.FloatField(default=0.0)
    
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null = True)
    #---------------------------------------------------------------
    porcentaje_de_senia_reservas = models.FloatField(default=0) # agregue esto para modificar contrato
    #-------------------------------------------------------------
    created = models.DateTimeField(auto_now_add=True)  # aca guardamos la fecha que se creo un servicio
    updated = models.DateTimeField(auto_now=True)  # aca guardamos cuando se actualiza
    
    #-------------------------volver atras------------------reserva contratro---------------------
    habitacion_reserva = models.CharField(max_length=40,  null= True, blank=True)
    
    
    
    
    
    def __str__(self):
       # return f'{self.habitacion}  {self.huesped} {self.fecha_entrada} {self.fecha_salida}' # la f es de formato
        return f'{self.habitacion}  {self.huesped}' # la f es de formato
    
    
    class Meta:
        db_table = "contrato"
        verbose_name = "Contrato"
        verbose_name_plural = "Contratos"
        ordering = ['id']  # significa que se va a ordenar por id
        
        
        
        
    def calcularFechas(request, fecha_entra, fecha_sali, habitacions, importe_otros_gasto):
        habitacion = Habitacion.objects.get(id= habitacions)
        total =0
       
        
        fechaConvertida = datetime.datetime.strptime(fecha_entra, '%Y-%m-%dT%H:%M') # strptime lo convierto a objeto datetime, el segundo parametro le dice como interpretar la fecha, cual es la hora, el dia, el mes etc
        fechaConvertida2 = datetime.datetime.strptime(fecha_sali, '%Y-%m-%dT%H:%M')
        #---------------------esto lo saque por internet--------------------------
        
        #cambiarle la hora con replace a una fecha datetime
       
        
        #fechaConvertida2.replace(hour=10, minute=0)
       
       
        #fecha_Para_comparar2 = datetime.datetime.strptime("10:01:00", "%X").time()
        
        #---------------------------time delta-----------------------------------
        #...........poner un delta de fecha para que me calcule a partir de 5 dias por ejemplo. (tambien con datetime)..........
         
        #dia_delta = datetime.timedelta(hours=7)#timedelta es una instacia de datetime
        #fecha_mas_delta = fechaConvertida2 + dia_delta
        
        
        
        
        
      
        fecha_modificada = fechaConvertida2.replace(hour=10, minute=0) # con replace creo una variable nueva y a fechaConvertida2 le cambio la hota etc
       
       
       
        
        
       
       
       
       
        
         
       # diferencia = fechaConvertida2-fechaConvertida 
        diferencia = fecha_modificada-fechaConvertida 
       
        diferenciaConvertida= diferencia.days # agregue esto
     
       
       
      
        #print(" la diferencia de dia es ",diferencia.days)
       # print("la fecha de entrada es ", fechaConvertida, "la fecha de salida es ", fechaConvertida2)
        
        
          #--------------------------check out 10--------------------------
        if fechaConvertida2== fecha_modificada:
          #print("hora reemplazada", fecha_modificada)
       
          if fechaConvertida.hour <10 and diferencia.days >00:
            
            diferenciaConvertida = diferencia.days
            diferenciaConvertida = diferenciaConvertida #+1
           # print(diferenciaConvertida)
           
          
       
         
          elif fechaConvertida.hour >= 10 and fechaConvertida.minute>=1: #le agregue el = al 00
            
              diferenciaConvertida = diferencia.days
              diferenciaConvertida = diferenciaConvertida+1 #+2
             # print(diferenciaConvertida, "(10) debo sumarle uno")
             
          elif fechaConvertida.hour ==10 and fechaConvertida.minute ==00:
              diferenciaConvertida = diferencia.days
              diferenciaConvertida = diferenciaConvertida #+1
         
             # print("igual a 10 (10)", diferenciaConvertida)
              
          
             
        
          elif diferencia.days <1:
               diferenciaConvertida=1
              # print("menos de un dia (10)", diferenciaConvertida)
               
          elif fechaConvertida.hour >= 10: #le agregue el = al 00
              diferenciaConvertida = diferencia.days
              diferenciaConvertida = diferenciaConvertida+1 #+2
             # print(diferenciaConvertida, "(10) debo sumarle uno, para la hora 22")
              
          
         
          subtotal1 = float(habitacion.precio_por_noche) * float(diferenciaConvertida)
          total = subtotal1+ float(importe_otros_gasto)
          #print("el total es ", total)
          
          
       
       
     
            #---------------------late check out  --------------------
        elif fechaConvertida2.hour >=10 and fechaConvertida2.hour <18:
          
          
         
          fechaConvertida2=fecha_modificada
          
          #print("if perteneciente a late")
          if fecha_modificada.hour ==10 and fecha_modificada.minute ==0:
            fecha_modificada = fechaConvertida2.replace(hour=10, minute=0)
            fechaConvertida2= fecha_modificada
           # print("fecha_modificada =", fecha_modificada)
            if fechaConvertida.hour <10 and diferencia.days >00:
            
              diferenciaConvertida = diferencia.days
              diferenciaConvertida = diferenciaConvertida #+1
            #  print(diferenciaConvertida, "late")
           
          
       
         
            elif fechaConvertida.hour >= 10 and fechaConvertida.minute>=1: #le agregue el = al 00
              
            
              diferenciaConvertida = diferencia.days
              diferenciaConvertida = diferenciaConvertida+1 #+2
             # print(diferenciaConvertida, "(10) debo sumarle uno (late)")
             
            elif fechaConvertida.hour ==10 and fechaConvertida.minute ==00:
              diferenciaConvertida = diferencia.days
              diferenciaConvertida = diferenciaConvertida #+1
         
             # print("igual a 10 (10), (late)", diferenciaConvertida)
              
          
             
        
            elif diferencia.days <1:
               diferenciaConvertida=1
              # print("menos de un dia (10), (late)", diferenciaConvertida)
               
            elif fechaConvertida.hour >= 10: #le agregue el = al 00
              diferenciaConvertida = diferencia.days
              diferenciaConvertida = diferenciaConvertida+1 #+2
             # print(diferenciaConvertida, "(10) debo sumarle uno, para la hora 22 (late)")
              
          
        
          subtotal1 = float(habitacion.precio_por_noche) * float(diferenciaConvertida)
          total = subtotal1+ float(importe_otros_gasto)
          total = total + float(habitacion.check_out_lates)
         # print("el total es ", total)
       
          
            
        
     
     
       
       # print("el total de todo el alojamiento es ", total) 
            
        
        
       
        
        
        return total
      
      
    
    
    
    def calcularImporteEstadia(request, fecha_entra, fecha_sali, habitacions, importe_otros_gasto):
        habitacion = Habitacion.objects.get(id= habitacions)
        total =0
       
       
        
        fechaConvertida = datetime.datetime.strptime(fecha_entra, '%Y-%m-%dT%H:%M') # strptime lo convierto a objeto datetime, el segundo parametro le dice como interpretar la fecha, cual es la hora, el dia, el mes etc
        fechaConvertida2 = datetime.datetime.strptime(fecha_sali, '%Y-%m-%dT%H:%M')
        #---------------------esto lo saque por internet--------------------------
       
        #fecha_Para_comparar2 = datetime.datetime.strptime("10:01:00", "%X").time()
        
        #---------------------------time delta-----------------------------------
        #...........poner un delta de fecha para que me calcule a partir de 5 dias por ejemplo. (tambien con datetime)..........
         
        #dia_delta = datetime.timedelta(hours=7)#timedelta es una instacia de datetime
        #fecha_mas_delta = fechaConvertida2 + dia_delta
        fecha_modificada = fechaConvertida2.replace(hour=10, minute=0) # con replace creo una variable nueva y a fechaConvertida2 le cambio la hota etc
        diferencia = fecha_modificada-fechaConvertida 
       
        diferenciaConvertida= diferencia.days # agregue esto
       
       
         
        #diferencia = fechaConvertida2-fechaConvertida 
        
     
      
        #print(" la diferencia de dia es ",diferencia.days)
       # print("la fecha de entrada es ", fechaConvertida, "la fecha de salida es ", fechaConvertida2)
        
        
          #--------------------------check out 10--------------------------
        if fechaConvertida2.hour == 10 and fechaConvertida2.minute==0:
       
          if fechaConvertida.hour <10 and diferencia.days >00:
            
            diferenciaConvertida = diferencia.days
            diferenciaConvertida = diferenciaConvertida #+1
           # print(diferenciaConvertida)
          
       
         
          elif fechaConvertida.hour >= 10 and fechaConvertida.minute>=1: #le agregue el = al 00
            
              diferenciaConvertida = diferencia.days
              diferenciaConvertida = diferenciaConvertida+1 #+2
             # print(diferenciaConvertida, "(10) debo sumarle uno")
              
            
              
             
          elif fechaConvertida.hour ==10 and fechaConvertida.minute ==00:
              diferenciaConvertida = diferencia.days
              diferenciaConvertida = diferenciaConvertida #+1
         
             # print("igual a 10 (10)", diferenciaConvertida)
              
          
             
        
          elif diferencia.days <1:
               diferenciaConvertida=1
             #  print("menos de un dia (10)", diferenciaConvertida)
               
          elif fechaConvertida.hour >= 10: #le agregue el = al 00
              diferenciaConvertida = diferencia.days
              diferenciaConvertida = diferenciaConvertida+1 #+2
           #   print(diferenciaConvertida, "(10) debo sumarle uno, para la hora 22")
              
          
         
          subtotal1 = float(habitacion.precio_por_noche) * float(diferenciaConvertida)
          total = subtotal1+ float(importe_otros_gasto)
          #print("el total es  ", total)
          #--------le agregue esto----------------
         
         
     
            #---------------------late check out--------------------
            
        elif fechaConvertida2.hour >=10 and fechaConvertida2.hour <18:
          
          
         
          fechaConvertida2=fecha_modificada
          
        #  print("if perteneciente a late")
          if fecha_modificada.hour ==10 and fecha_modificada.minute ==0:
            fecha_modificada = fechaConvertida2.replace(hour=10, minute=0)
            fechaConvertida2= fecha_modificada
         #   print("fecha_modificada =", fecha_modificada)
            if fechaConvertida.hour <10 and diferencia.days >00:
            
              diferenciaConvertida = diferencia.days
              diferenciaConvertida = diferenciaConvertida #+1
             # print(diferenciaConvertida, "late")
           
          
       
         
            elif fechaConvertida.hour >= 10 and fechaConvertida.minute>=1: #le agregue el = al 00
              
            
              diferenciaConvertida = diferencia.days
              diferenciaConvertida = diferenciaConvertida+1 #+2
            #  print(diferenciaConvertida, "(10) debo sumarle uno (late)")
             
            elif fechaConvertida.hour ==10 and fechaConvertida.minute ==00:
              diferenciaConvertida = diferencia.days
              diferenciaConvertida = diferenciaConvertida #+1
         
            #  print("igual a 10 (10), (late)", diferenciaConvertida)
              
          
             
        
            elif diferencia.days <1:
               diferenciaConvertida=1
              # print("menos de un dia (10), (late)", diferenciaConvertida)
               
            elif fechaConvertida.hour >= 10: #le agregue el = al 00
              diferenciaConvertida = diferencia.days
              diferenciaConvertida = diferenciaConvertida+1 #+2
            #  print(diferenciaConvertida, "(10) debo sumarle uno, para la hora 22 (late)")
              
          
        
          subtotal2 = float(habitacion.precio_por_noche) * float(diferenciaConvertida)
       
          subtotal1 = subtotal2 + float(habitacion.check_out_lates)
         
       
          
            
        
            #if fechaConvertida2.hour <10 and fechaConvertida2.hour<17:
            # aca hacer un if menor de 10 y que el resultado me de cero y luego en la vista compararlo
             # y arriba en el if comparar con minutos
             
             
             
             #falta el agregarle el chek out late al importe
          
          
          
          
             
     
       
      # print("el total de todo el alojamiento es ", total)
        
        return subtotal1
      
      
      
      #-----------------------------noches pernotadas------------------------------
    def nochesDeEstadia(request, fecha_entra, fecha_sali, habitacions, importe_otros_gasto):
        habitacion = Habitacion.objects.get(id= habitacions)
        total =0
       
       
        
        fechaConvertida = datetime.datetime.strptime(fecha_entra, '%Y-%m-%dT%H:%M') # strptime lo convierto a objeto datetime, el segundo parametro le dice como interpretar la fecha, cual es la hora, el dia, el mes etc
        fechaConvertida2 = datetime.datetime.strptime(fecha_sali, '%Y-%m-%dT%H:%M')
        #---------------------esto lo saque por internet--------------------------
       
        #fecha_Para_comparar2 = datetime.datetime.strptime("10:01:00", "%X").time()
        
        #---------------------------time delta-----------------------------------
        #...........poner un delta de fecha para que me calcule a partir de 5 dias por ejemplo. (tambien con datetime)..........
         
        #dia_delta = datetime.timedelta(hours=7)#timedelta es una instacia de datetime
        #fecha_mas_delta = fechaConvertida2 + dia_delta
        fecha_modificada = fechaConvertida2.replace(hour=10, minute=0) # con replace creo una variable nueva y a fechaConvertida2 le cambio la hota etc
        diferencia = fecha_modificada-fechaConvertida 
       
        diferenciaConvertida= diferencia.days # agregue esto
       
       
         
        #diferencia = fechaConvertida2-fechaConvertida 
        
     
      
       # print(" la diferencia de dia es ",diferencia.days)
       # print("la fecha de entrada es ", fechaConvertida, "la fecha de salida es ", fechaConvertida2)
        
        
          #--------------------------check out 10--------------------------
        if fechaConvertida2.hour == 10 and fechaConvertida2.minute==0:
       
          if fechaConvertida.hour <10 and diferencia.days >00:
            
            diferenciaConvertida = diferencia.days
            diferenciaConvertida = diferenciaConvertida #+1
           # print(diferenciaConvertida)
          
       
         
          elif fechaConvertida.hour >= 10 and fechaConvertida.minute>=1: #le agregue el = al 00
            
              diferenciaConvertida = diferencia.days
              diferenciaConvertida = diferenciaConvertida+1 #+2
             # print(diferenciaConvertida, "(10) debo sumarle uno")
              
            
              
             
          elif fechaConvertida.hour ==10 and fechaConvertida.minute ==00:
              diferenciaConvertida = diferencia.days
              diferenciaConvertida = diferenciaConvertida #+1
         
            #  print("igual a 10 (10)", diferenciaConvertida)
              
          
             
        
          elif diferencia.days <1:
               diferenciaConvertida=1
             #  print("menos de un dia (10)", diferenciaConvertida)
               
          elif fechaConvertida.hour >= 10: #le agregue el = al 00
              diferenciaConvertida = diferencia.days
              diferenciaConvertida = diferenciaConvertida+1 #+2
             # print(diferenciaConvertida, "(10) debo sumarle uno, para la hora 22")
              
          
         
          subtotal1 = float(habitacion.precio_por_noche) * float(diferenciaConvertida)
          total = subtotal1+ float(importe_otros_gasto)
          #print("el total es  ", total)
          #--------le agregue esto----------------
         
         
     
            #---------------------late check out--------------------
            
        elif fechaConvertida2.hour >=10 and fechaConvertida2.hour <18:
          
          
         
          fechaConvertida2=fecha_modificada
          
        #  print("if perteneciente a late")
          if fecha_modificada.hour ==10 and fecha_modificada.minute ==0:
            fecha_modificada = fechaConvertida2.replace(hour=10, minute=0)
            fechaConvertida2= fecha_modificada
           # print("fecha_modificada =", fecha_modificada)
            if fechaConvertida.hour <10 and diferencia.days >00:
            
              diferenciaConvertida = diferencia.days
              diferenciaConvertida = diferenciaConvertida #+1
             # print(diferenciaConvertida, "late")
           
          
       
         
            elif fechaConvertida.hour >= 10 and fechaConvertida.minute>=1: #le agregue el = al 00
              
            
              diferenciaConvertida = diferencia.days
              diferenciaConvertida = diferenciaConvertida+1 #+2
             # print(diferenciaConvertida, "(10) debo sumarle uno (late)")
             
            elif fechaConvertida.hour ==10 and fechaConvertida.minute ==00:
              diferenciaConvertida = diferencia.days
              diferenciaConvertida = diferenciaConvertida #+1
         
             # print("igual a 10 (10), (late)", diferenciaConvertida)
              
          
             
        
            elif diferencia.days <1:
               diferenciaConvertida=1
            #   print("menos de un dia (10), (late)", diferenciaConvertida)
               
            elif fechaConvertida.hour >= 10: #le agregue el = al 00
              diferenciaConvertida = diferencia.days
              diferenciaConvertida = diferenciaConvertida+1 #+2
           #   print(diferenciaConvertida, "(10) debo sumarle uno, para la hora 22 (late)")
              
          
        
          subtotal2 = float(habitacion.precio_por_noche) * float(diferenciaConvertida)
       
          subtotal1 = subtotal2 + float(habitacion.check_out_lates)
         
       
          
            
        
            #if fechaConvertida2.hour <10 and fechaConvertida2.hour<17:
            # aca hacer un if menor de 10 y que el resultado me de cero y luego en la vista compararlo
             # y arriba en el if comparar con minutos
             
             
             
             #falta el agregarle el chek out late al importe
          
          
          
          
             
     
       
      #  print("el total de todo el alojamiento es ", total)
        
        return diferenciaConvertida
      
      
    # def habitacionesLibres(request):
      
    #   habitacionesLibres = list()
      
    #   habitaciones = Habitacion.objects.all()
      
    #   for habitacion in habitaciones:
    #     if habitacion.estado=="Null":
    #       habitacionesLibres.append(habitacion)
          
    #   return habitacionesLibres
      
      
      
    

      
   
      
      
      
 
      
      
    
      
      
      
    
        
       
         
           
             
    

    
             
       
             
    
             
             
            
             
             
       
             
    
             
             
            
             
             
       
        
    
   
  


   
        
        
       
         
           
             
    

    
             
       
             
    
             
             
            
             
             
       
             
    
             
             
