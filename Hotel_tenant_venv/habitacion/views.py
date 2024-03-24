from django.shortcuts import render, redirect, get_object_or_404
from habitacion.forms import FormsHabitacion
from django.contrib import messages
from .models import Habitacion
from contrato.models import Contrato
from django.contrib.auth.decorators import login_required

from shared.models import Client


from reservas.models import Reserva


# Create your views here.

def mostrarHabitacion(request):
    
    
    #codigo cantidad habitaciones comparar segun tenant----
    habitaciones = Habitacion.objects.filter(eliminado=False)
    total_habitacion = len(habitaciones)
    ultimaHabistacion = Habitacion.objects.last()
    cant_habi_tenant=request.tenant.cantidad_habitacion
   
   
    
  
 
    cliente = Client()
    
   
         
   
         
  
    
    
    habitacion = Habitacion()
    
   
    
   



    if request.method == 'POST': #si aprete el boton
       
       

        form = FormsHabitacion(request.POST)
              
        if form.is_valid():  # vamos a preguntar si los datos que se ingresaron son validos
              if cant_habi_tenant=="menos_de_10" and total_habitacion <9:
               form.save()
               messages.success(request, "La habitación se guardo correctamente")
          
              # print("cantidad:", cliente.cantidad_habitacion)
          
               return redirect("modificarHabitacion")
      
        
          
          
              elif cant_habi_tenant=="entre_diez_treinta"  and total_habitacion <=29:
                  
             
               
          
        # ultimaHabistacion.delete()
       
               form.save()
               messages.success(request, "La habitación se guardo correctamente")
       
               return redirect("modificarHabitacion")
     
              elif cant_habi_tenant=="mas_30" and total_habitacion>=0:
         
               form.save()
               messages.success(request, "La habitación se guardo correctamente")
              
          
               return redirect("modificarHabitacion")
       
              else:
               messages.error(request, "cantidad de habitaciones no permitidas")
             
           
               return redirect("Habitacion")
         
          
           

        else:
            messages.error(request, "La habitacion no se ha guardado...")
          



    else:

        form = FormsHabitacion()  # si no es un post le decimos que nos vuelva a renderizar el formulario
                

    return render(request, 'habitacion/habitacion.html', {'forms': form})


def actualizarHabitacion(request):
    
    lista=list()
    habitaciones = Habitacion.objects.all()
    
    for hab in habitaciones:
        if hab.eliminado == False:
            lista.append(hab)
            



    return render(request, 'habitacion/modificarHabitacion.html', {'habitaciones': lista})





def tabla_modificar(request, id_habitacion):

    habitacion = get_object_or_404(Habitacion, id=id_habitacion)

    if request.method == "POST":
                       #------CAMPOS DEL FORMULARIO.---------------
       

        nombre = request.POST.get("nombre_numero")
        piso = request.POST.get("piso")
        capacidad = request.POST.get("capacidad")
        precio_por_noche = request.POST.get("precio_por_noche")
        camita_bebe = request.POST.get("camita_bebe")
        #esta_limpia = request.POST.get("esta_limpia")
        posee_heladera = request.POST.get("posee_heladera")
        posee_aire_acondicionado = request.POST.get("posee_aire_acondicionado")
        posee_calefaccion = request.POST.get("posee_calefaccion")
        posee_ventana = request.POST.get("posee_ventana")
        posee_cama_matrimonial = request.POST.get("posee_cama_matrimonial")
        posee_televisor = request.POST.get("posee_televisor")
        posee_wifi = request.POST.get("posee_wifi")
        posee_jacuzzi = request.POST.get("jacuzzi")#lo agregue nuevo
        posee_microondas =request.POST.get("posee_microondas")#lo agregue nuevo
        check_out_late =request.POST.get("check_out_lates")#lo agregue nuevo
        otro_dato = request.POST.get("otro_dato")#lo agregue nuevo

        #-----------------CAMPOS DEL MODELO--------------------------------------------

        habitacion.nombre_numero = nombre
        habitacion.piso=piso
        habitacion.capacidad = capacidad
        habitacion.precio_por_noche = precio_por_noche
        habitacion.camita_bebe = camita_bebe
       # habitacion.esta_limpia = esta_limpia
        habitacion.posee_heladera = posee_heladera
        habitacion.posee_aire_acondicionado = posee_aire_acondicionado
        habitacion.posee_calefaccion = posee_calefaccion
        habitacion.posee_ventana = posee_ventana
        habitacion.posee_cama_matrimonial = posee_cama_matrimonial
        habitacion.posee_televisor = posee_televisor
        habitacion.posee_wifi = posee_wifi
        habitacion.jacuzzi=posee_jacuzzi
        habitacion.posee_microondas=posee_microondas
        habitacion.check_out_lates=check_out_late
        habitacion.otro_dato=otro_dato
       
        
        #....................................le agregue esto antes no estaba-----------------
       
       

        try:
            habitacion.save()
          
            messages.success(request, "La habitacion se actualizo correctamente...")

        except:

            messages.error(request, "La habitacion no se actualizo...")




        return redirect('modificarHabitacion')

    else:
        form = FormsHabitacion(instance=habitacion)

    return render(request, 'habitacion/modificar_tabla.html', {'form': form})




def eliminarHabitacion(request, id_habitacion):
    
    
    habitacion = get_object_or_404(Habitacion, id=id_habitacion)
    #eliminar_y_Poner_Null(request, id_habitacion)
    
    try:
        habitacion.delete()
       
        messages.success(request, "La habitacion se elimino correctamente...")
        
    except:
        messages.error(request, "La habitacion no se elimino...")
        
    return redirect('modificarHabitacion')


def habilitarPost_time(request, id_habitacion):
    habitacion = get_object_or_404(Habitacion, id=id_habitacion)
    contrato = Contrato.objects.all()
     
    False_variable = False
    
    if habitacion.estado=="ocupada":
        habitacion.estado="Null"
        habitacion.save()
        
        #-------------le greguego esto------------------------
            
        for contr in contrato:
                 
            if contr.habitacion== habitacion:
                contr.estado= False_variable
                contr.save()
    return redirect('Panel')
    
    
    
def eliminar_ocultar_habitacion(request, id_habitacion):
    
    #poner habitacion  ,eliminado true, ocupada y contrato = false
    
    #---------volver atras-------------------- -------------- ----------------   ---- -------------------
    
    reserva = Reserva.objects.all()
    
    habitacion = get_object_or_404(Habitacion, id=id_habitacion)
    
    contrato = Contrato.objects.all()
    
    if request.method =="POST":
        
        try:
            habitacion.estado="ocupada"
            habitacion.eliminado=True
            habitacion.save()
            
            for contra in contrato:
                
                if contra.habitacion == habitacion:
                    contra.estado=False
                    contra.save()
                    
            for reser in reserva:
                
                if reser.habitacion == habitacion:
                    reser.estado=False
                    reser.save()
            
            messages.success(request, "La habitación se elimino correctamente...")
           
            
        except:
         
            
            messages.error(request, "La habitación no se elimino...")
             
             
        return redirect('modificarHabitacion')     
         
    
    

    
'''def filtrar_por_cantidad(request):
    
  
   
   
     habitaciones = Habitacion.objects.filter(eliminado=False)
     total_habitacion = len(habitaciones)
     ultimaHabistacion = Habitacion.objects.last()
     cant_habi_tenant=request.tenant.cantidad_habitacion
   
     
  

    
     if cant_habi_tenant=="menos_de_10" and total_habitacion <9:
          form.save()
          messages.success(request, "La habitación se guardo correctamente")
          
         # print("cantidad:", cliente.cantidad_habitacion)
          
          return redirect("paginaPrincipal")
      
        
          
          
     elif cant_habi_tenant=="entre_diez_treinta" and  total_habitacion >0 and total_habitacion <=30:
          
        # ultimaHabistacion.delete()
       
         form.save()
         messages.success(request, "La habitación se guardo correctamente")
       
         return redirect("paginaPrincipal")
     
     elif cant_habi_tenant=="mas_30" and total_habitacion>30:
         
           form.save()
           messages.success(request, "La habitación se guardo correctamente")
          
           return redirect("paginaPrincipal")
       
     else:
             messages.error(request, "cantidad de habitaciones no permitidas")
           
             return redirect("paginaPrincipal")'''
         
          
      

        
    
    
        
    
   
    
    













