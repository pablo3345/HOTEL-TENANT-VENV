#import MySQLdb
from django.shortcuts import render, redirect, get_object_or_404 #,render_to_response
from contrato.formsContrtato import FormContrato 
from contrato.formsHuesped import FormHuesped
from contrato.formsProductos_agregados import FormsProductos_agregados
from django.contrib import messages
from contrato.models import Huesped, Contrato
import datetime
from habitacion.models import Habitacion
#from panel_de_admin.views import mostrarPanel
from django.views.generic import View
from .utilitario import render_to_pdf
from django.http import HttpResponse
from productos.models import Agregar_productos
from productos.models import Producto_al_publico
from django.db.models import F,Sum, FloatField  # para calcular el total de una orden de pedido
from django.db import connection
from django.urls import reverse
from django.http import HttpResponseRedirect

#import json


from reservas.models import HuespedReserva, Reserva



#--------------------------------volver---atras--------------------------------------------------


# Create your views here.

def mostrarContrato(request):
     form = FormHuesped()
     form2 = FormContrato()
   
  
   
     #-------para mostrar el ultimo huesped en el html----------
     ultimoHuesped = Huesped.objects.all()
     #--------------todo sobre el select reserva------------------
   #  Reservas = Reserva.objects.all()
     #id = request.GET["hues"]
    # print("el id del select es vvContrato ", id)
     
     
     
     #-----------------------------------------------------------
     ultimo = list()
     ultimoHues = list()
     
     for ult in ultimoHuesped:
          if ult.nombre_responsable != None:
               ultimo.append(ult)
               ultimoHues= ultimo[-1]
               
         
    #----------------------------------------------------------
     
     
     if request.method =='POST':
         
          formHuesped =FormHuesped(request.POST)
         
          if formHuesped.is_valid():
              
              formHuesped.save()
              messages.success(request, "El huesped se guardo correctamente...")
              
          else:
              messages.error(request, "El huesped no se guardo...")
              
          return redirect('Contrato')
        
        
          
        
          
     
     else:
          formHuesped=FormHuesped()
       
          #---agrego esto para mandar el huesped reserva ahuesped contrato
          
          
        
         
    
     return render(request, "contrato/contrato.html", {'formHuesped': form, 'formContrato': form2, 'ultimoHuesped':ultimoHues})
 
 
 
def modificarHuesped(request):
     #formHuesped = FormHuesped()
     huespedes = Huesped.objects.all()
     
     return render(request, "contrato/modificarHuesped.html",{'huespedes': huespedes})
     
  



def modificarTablaHuesped(request, id_huesped):
     
     formHuesped = FormHuesped()
     huesped =  get_object_or_404(Huesped, id=id_huesped)
     
     nombre_resp = request.POST.get("nombre_responsable")
     apelli = request.POST.get("apellido")
     edadd = request.POST.get("edad")
     dnii = request.POST.get("dni")
     demas_huespe = request.POST.get("demas_huespedes")
     patente_vehicu = request.POST.get("patente_vehiculo")
     modelo_vehicu = request.POST.get("modelo_vehiculo")
     correo_electro =request.POST.get("correo_electronico")
     #----------------------------------------------------------
     direccion= request.POST.get("direccion")
     localidad = request.POST.get("localidad")
     codigo_postal =  request.POST.get("codigo_postal")
     pais= request.POST.get("pais")
     telefono= request.POST.get("telefono")
     #------------------------------------------------
    # penalidad = request.POST.get("penalidad")
     
     if request.method =='POST':
          
          huesped.nombre_responsable= nombre_resp
          huesped.apellido = apelli
          huesped.edad = edadd
          huesped.dni = dnii
          huesped.demas_huespedes = demas_huespe
          huesped.patente_vehiculo= patente_vehicu
          huesped.modelo_vehiculo= modelo_vehicu
          huesped.correo_electronico= correo_electro
          huesped.penalidad= huesped.penalidad
          #---------------------------------------
          huesped.direccion= direccion
          huesped.localidad= localidad
          huesped.codigo_postal= codigo_postal
          huesped.pais=pais
          huesped.telefono= telefono
          
         
          
          try:
          
            huesped.save()
            messages.success(request, "El huesped se actualizo correctamente...")
          
            
       
        
          except:
               messages.error(request, "El huesped no se actualizo...")
               
          return redirect('modificarHuesped')
     
     
     else:
          formHues = FormHuesped(instance=huesped)
        

          
          
     return render(request, "contrato/modificar_tablaHuesped.html", {'formHues': formHues, 'penalidad': penalidad})



def eliminarHuesped(request, id_huesped):
     
     huesped = get_object_or_404(Huesped, id=id_huesped)
    
     
     ponerNullHabitacion_cuandoBorroUnHuesped_en_Contrato(request, id_huesped)
     
     try:
          huesped.delete()
         
          
          messages.success(request, "El huesped se elimino correctamente...")
         
          
     except:
          messages.error(request, "El huesped no se elimino...")
          
    
          
          
     return redirect('modificarHuesped')


          
     
     #---------------------------------VISTA CONTRATO--------------------------------------
     
     

         
   
     #-------------------------------------volver atras----------------------------------------------------------------------
def guardarContrato(request):
     form = FormHuesped()
     form2 = FormContrato()
     contrato = Contrato()
     
     true_variable = True
     
     reservas2 = Reserva.objects.all()
     contratos2 = Contrato.objects.all()
     
     
     
     ultimoHuespedd = Huesped.objects.all()
      
     ultimos = list()
     ultimoHues = list()
     
     for ult in ultimoHuespedd:
          if ult.nombre_responsable != None:
               ultimos.append(ult)
               ultimoHues= ultimos[-1]
               
     
     
     
    # habitacion = Habitacion.objects.get(id= id_habitacion)
    
    
    
     
     # si en el formulario no obtengo los datos con form(request.POST), no voy a preguntar si el forn is_valid()
     
     
     if request.method == "POST":
         # habitacion=models.Habitacion.objects.get(habitacion)
          habitacions = request.POST.get("habitacion")
          huespeds =request.POST.get("huesped")
          fecha_entra = request.POST.get("fecha_entrada")
          fecha_sali = request.POST.get("fecha_salida")
          importe_estad= request.POST.get("importe_estadia")
          importe_otros_gast= request.POST.get("importe_otros_gasto")
          totals= request.POST.get("total")
          late_check_out = request.POST.get("late_chack_out")
          
          descuento_porNoche= request.POST.get("descuento_importe_noche")
          descuento_total_importe= request.POST.get("descuento_total_calcularo")
          aumento_Total= request.POST.get("aumento_total")
          
          #----------------------------------------
          porcentaje_senia= request.POST.get("total")
          
          #-----------------------volver atrass------------------------------
          
       
          porcentaje_senia_reserva= request.POST.get("porcentaje_de_senia_reservas")
          
         #---volver atras----------------------------- --- --- -------------------------------------------
         
           
          
          habitacion_reservas= request.POST.get("habitacion_reserva")
          
         # total_enviar_desdeReserva_a_contrato= request.POST.get("total_enviar_desdeReserva_a_contrato")
          
          
          
          
          
        
          
        
        
          
     #.........................cambiar formato calendario.....................
          fechaConvertida = datetime.datetime.strptime(fecha_entra, '%Y-%m-%dT%H:%M') # strptime lo convierto a objeto datetime, el segundo parametro le dice como interpretar la fecha, cual es la hora, el dia, el mes etc
     
          fechaFormateada = fechaConvertida.strftime('%Y-%m-%dT%H:%M') # strftime para darle el formato que quiero
       
        
          fechaConvertida2 = datetime.datetime.strptime(fecha_sali, '%Y-%m-%dT%H:%M')
          fechaFormateada2 = fechaConvertida2.strftime('%Y-%m-%dT%H:%M') 
          
          #habitacion = Habitacion.objects.get(id= habitacions)
          #huesped = Huesped.objects.get(id=huespeds)
          habitacion = get_object_or_404(Habitacion, id=habitacions)
          huesped = get_object_or_404(Huesped, id=huespeds)
          
          #-------------------------id contrato para ponerle True----------------------
          id_contrato = contrato.id
          
          contrato.habitacion =habitacion 
           
          
          
        
          
        
         
          
          #-------fuera del horario----------
          if fechaConvertida2.hour <10 or fechaConvertida2.hour>=18:
                messages.error(request, "El horario no corresponde")
                return redirect('Contrato')
          #-------------para comparar si la fecha entrada es mayor a la fecha salida-----------
          
          elif fechaConvertida >= fechaConvertida2:
                messages.error(request, "La entrada es mayor o igual a la salida")
                return redirect('Contrato')
           
         
                 
           
           
          elif habitacion_reservas == "":
               
               pass
          else:
                if habitacion_reservas != contrato.habitacion.nombre_numero:
                      messages.error(request, "No se guardo... porque la habitación Reserva no coincide con la de contrato")
                      print("total contrato", float(contrato.total))
                      return redirect("Contrato")
                 
                 
         
               
               
          
           
           
         
          
        #---------------------------hago esto para cuando los años de entrada y salida no coinciden-------------------------------
          '''fechaSalidaEntero = int(fechaConvertida2.strftime('%y'))
          fechaEntradaEntero = int(fechaConvertida.strftime('%y'))
          
       
          
          if fechaEntradaEntero > fechaSalidaEntero:
                messages.error(request, "Los años no corresponden")
               # print("fecha entrada año", fechaEntradaEntero)
               # print("fecha salida año", fechaSalidaEntero)
                return redirect('Contrato')'''
          
          
          
          
       #-----------volver atras modifique todo el---------------------------------------------------------
          
          
        
         
               
          
          total =calcularTotal(request, fecha_entra, fecha_sali, habitacions, importe_otros_gast)
          
          importeEstadia =calcularImporteEstadia(request, fecha_entra, fecha_sali, habitacions, importe_otros_gast)
          
          diferenciaConvertida = contrato.nochesDeEstadia(fecha_entra, fecha_sali, habitacions, importe_otros_gast)
          
          
        
           #---------------para sacar la promocion de descuento-------------- pr volver------
         # total_estadia_con_descuento_Late =descuento_delTotal_Promocion_menosLate(request, fecha_entra, fecha_sali, habitacions, importe_otros_gast)
          #total_estadia_con_descuento_diez =descuento_delTotal_Promocion_chekOut_diez(request, fecha_entra, fecha_sali, habitacions, importe_otros_gast)
           #para volver atras--------------...........----------------------
          
          if int(descuento_porNoche) != 0 and int(descuento_total_importe) != 0:
               
               messages.error(request, "ingreso porcentajes en opciones no permitidas")
               return redirect('Contrato')
          
           #----------------agregue esto por que el casillero habitacion esta vacio 
         
          
         # elif  int(descuento_porNoche) != 0 and int(aumento_Total) != 0:
             #   messages.error(request, "ingreso porcentajes en varias opciones")
             #   return redirect('Contrato')
         # elif int(descuento_total_importe) != 0 and int(aumento_Total) != 0:
             #  messages.error(request,"ingreso porcentajes en varias opciones")
              # return redirect('Contrato')
          
          elif int(descuento_total_importe) != 0 and int(aumento_Total) != 0 and int(descuento_porNoche) != 0:
                messages.error(request,"ingreso porcentajes en opciones no permitidas")
                return redirect('Contrato')
           
           
           
           
           
           
           
           
        
          
          
        
         
       
              
         
          if int(descuento_porNoche) != 0 and int(aumento_Total) ==0:
              
               
             
             
               if fechaConvertida2.hour==10 and fechaConvertida2.minute==0:
                     total_estadia_con_descuento_diez =descuento_delTotal_Promocion_chekOut_diez(request, fecha_entra, fecha_sali, habitacions, importe_otros_gast)
                     contrato.importe_estadia= total_estadia_con_descuento_diez
                     contrato.total = total_estadia_con_descuento_diez + float(importe_otros_gast)  # - float(porcentaje_senia)  agregue el total de la seña reserva
                     
                     descuento = contrato.total * float(porcentaje_senia_reserva)/100
                     
                     contrato.total = contrato.total - float(descuento)
                     
                     contrato.porcentaje_de_senia_reservas= float(porcentaje_senia_reserva)
                     #------------------------volver atrasssss------------------------------------------
                   #  contrato.porcentaje_de_senia_reservas= float(porcentaje_senia)
                     
                     messages.success(request, "agrego descuento al precio de la habitacion por cada noche")
                    
                    
                    
               else:
                    if fechaConvertida2.hour >=10 and fechaConvertida2.hour <18:
                          total_estadia_con_descuento_Late =descuento_delTotal_Promocion_menosLate(request, fecha_entra, fecha_sali, habitacions, importe_otros_gast)
                          contrato.importe_estadia= total_estadia_con_descuento_Late
                          contrato.total= total_estadia_con_descuento_Late + float(importe_otros_gast) # - float(porcentaje_senia)  agregue el total de la seña reserva
                          
                          descuento = contrato.total * float(porcentaje_senia_reserva)/100
                          contrato.total = contrato.total - float(descuento)
                          
                          contrato.porcentaje_de_senia_reservas= float(porcentaje_senia_reserva)
                         # contrato.porcentaje_de_senia_reservas= float(porcentaje_senia)
                          
                          messages.success(request, "agrego descuento al precio de la habitacion por cada noche")
                          #print("el porcentaje de senia es ", float(porcentaje_senia))
                         
                    
                    
          
                     
                     
        
                  
          elif int(aumento_Total) != 0 and  int(descuento_porNoche) == 0 and int(descuento_total_importe)== 0: # esto lo agregue a lo ultimo de la noche
                 contrato.importe_estadia= importeEstadia
                
                 aumento_total = total* float(aumento_Total) /100
                 aumento_total2 = aumento_total
                 contrato.total= total + aumento_total2 #- float(porcentaje_senia)  agregue el total de la seña reserva
                 
                 descuento = contrato.total *float(porcentaje_senia_reserva)/100
                 
                 contrato.total = contrato.total - float(descuento)
                 
                # contrato.porcentaje_de_senia_reservas= float(porcentaje_senia)
                 contrato.porcentaje_de_senia_reservas= float(porcentaje_senia_reserva)
                 messages.success(request, "agrego un aumento al total del importe")
          
          
          elif  int(descuento_total_importe) !=0  and int(aumento_Total) ==0: # esto lo agregue ahor para volver atras-----
                 contrato.importe_estadia= importeEstadia
                
                 descuentoTotal = total* float(descuento_total_importe) /100
                 descuentoTotal2 = descuentoTotal 
                 
                # -----------volver atras--------------------
                 #contrato.porcentaje_de_senia_reservas= float(porcentaje_senia_reserva)
               
                 contrato.total= total - descuentoTotal2 #- float(porcentaje_senia)  agregue el total de la seña reserva
             
                 descuento = contrato.total *float(porcentaje_senia_reserva)/100
                 
                 contrato.total = contrato.total - float(descuento)
               
               
                 messages.success(request, "agrego descuento al total")
                 
         #---------------------------APRETANDO DOS OPCIONES------------------------------- 
         
          elif int(descuento_porNoche) != 0 and int(aumento_Total) != 0:
               contrato.habitacion =habitacion 
               
             #  contrato.huesped = ultimoHues # cambie huesped por esto
               contrato.huesped = huesped # cambie el ultimoHues por esto
               contrato.fecha_entrada= fechaFormateada
               contrato.fecha_salida = fechaFormateada2
          
          #-------------------agregue los descuentos ---------------------
          
               contrato.descuento_importe_noche=descuento_porNoche
               contrato.descuento_total_calcularo=descuento_total_importe
               contrato.aumento_total= aumento_Total
          
         #----------------------------------------------------------- 
       
               contrato.importe_otros_gasto = importe_otros_gast
        
               contrato.estado=true_variable
               
               
              # contrato.porcentaje_de_senia_reservas= float(porcentaje_senia)
              
               contrato.porcentaje_de_senia_reservas= float(porcentaje_senia_reserva)
       
        
         
             
             #---------------------------para volver atras-------------------
               if fechaConvertida2.hour==10 and fechaConvertida2.minute==0:
                     total_estadia_con_descuento_diez =descuento_delTotal_Promocion_chekOut_diez(request, fecha_entra, fecha_sali, habitacions, importe_otros_gast)
                     contrato.importe_estadia= total_estadia_con_descuento_diez
                     contrato.total = total_estadia_con_descuento_diez + float(importe_otros_gast) 
                     
                     
                   
                     
                     messages.success(request, "aplico un descuento por cada noche y un aumento sobre el total")
                     
               #-------------aumento-----------    
                     total= contrato.total
                     total2 = total *float(aumento_Total)/100
                     total3 = total +total2
                     
                     contrato.total = total3 #-float(porcentaje_senia)  agregue el total de la seña reserva
                      
                     descuento15 = contrato.total * float(porcentaje_senia_reserva) /100 
                      
                     contrato.total = contrato.total - float(descuento15)
                     contrato.save()
                   
                    
               else:
                    if fechaConvertida2.hour >=10 and fechaConvertida2.hour <18:
                          total_estadia_con_descuento_Late =descuento_delTotal_Promocion_menosLate(request, fecha_entra, fecha_sali, habitacions, importe_otros_gast)
                          contrato.importe_estadia= total_estadia_con_descuento_Late
                          contrato.total= total_estadia_con_descuento_Late + float(importe_otros_gast) 
                          
                         
                          
                          messages.success(request, "aplico un descuento por cada noche y un aumento sobre el total")
                          
                        
                 
          #---------------------aumento-------------------------------
                  
                      
                    total= contrato.total
                    total2 = total *float(aumento_Total)/100
                    total3 = total +total2
                    
       
                     
                    contrato.total = total3 #- float(porcentaje_senia)  agregue el total de la seña reserva
                    
                    
                    descuento16 = contrato.total * float(porcentaje_senia_reserva) /100 
                      
                    contrato.total = contrato.total - float(descuento16)
                      
                    contrato.save()
                    
                    
          elif  int(descuento_total_importe) !=0  and int(aumento_Total) != 0:
                 contrato.habitacion =habitacion 
          
                 contrato.huesped = huesped
                 contrato.fecha_entrada= fechaFormateada
                 contrato.fecha_salida = fechaFormateada2
          
          #-------------------agregue los descuentos ---------------------
          
                 contrato.descuento_importe_noche=descuento_porNoche
                 contrato.descuento_total_calcularo=descuento_total_importe
                 contrato.aumento_total= aumento_Total
          
         #----------------------------------------------------------- 
       
                 contrato.importe_otros_gasto = importe_otros_gast
        
                 contrato.estado=true_variable
       
                
                 contrato.importe_estadia= importeEstadia
                
                 descuentoTotal = total* float(descuento_total_importe) /100
                 descuentoTotal2 = descuentoTotal
                  
               
                 contrato.total= total - descuentoTotal2
                 
                 contrato.porcentaje_de_senia_reservas= float(porcentaje_senia_reserva)
                 
                 contrato.save()
               
                # messages.success(request, "agrego descuento al total importe")
                 #----------------------------------------
                 
                 total= contrato.importe_estadia
                      
                 estadia_mas_otros_gastos = float(contrato.importe_estadia)+ float(contrato.importe_otros_gasto)
                      
                 descuento =estadia_mas_otros_gastos*float(descuento_total_importe)/100
                      
                      
                 tota2 = estadia_mas_otros_gastos- descuento
                      
                 tota2 = tota2 + tota2 *float(aumento_Total)/100
                          
                     
                      
                 contrato.total = tota2 #- float(porcentaje_senia)  agregue el total de la seña reserva
                 
                 
                 descuento19 = contrato.total * float(porcentaje_senia_reserva) /100 
                      
                 contrato.total = contrato.total - float(descuento19)
                 
                 
                # contrato.porcentaje_de_senia_reservas= float(porcentaje_senia)
                 
                 messages.success(request, "agrego descuento al total importe, y luego un aumento al total")
                      
                 contrato.save()
                 
                 
          #        #---------agregar el iva del 21 porciento--------------------------------------
          # if  int(aumento_iva) !=0 and  int(descuento_total_importe) ==0  and int(aumento_Total)==0:
             
                
          #         aumento_total_iva = float(importeEstadia)* float(aumento_iva) /100
          #         aumento_total_iva2 = aumento_total_iva
          #         contrato.importe_estadia= float(importeEstadia) + aumento_total_iva2
                 
                 
          #         contrato.total= float(contrato.importe_estadia) + float(importe_otros_gast)
             
          #         messages.success(request, "agrego el iva al importe estadia")
                 
          #         contrato.save()
               
                   
               
                   
                     
                 
         
                
               
               
          
               
               
          else:
               
               
               contrato.importe_estadia= importeEstadia
               contrato.total= total - total*float(porcentaje_senia_reserva)/100 # agregue el total de la seña reserva
               
               #------------------volver atras---------------------------
             
               
          
         
              
                         
               
              
     
          
          contrato.habitacion =habitacion # obtuve la habitacion mediante el id
          contrato.huesped = huesped
          #contrato.huesped = ultimoHues
          contrato.fecha_entrada= fechaFormateada
          contrato.fecha_salida = fechaFormateada2
          
          #-------------------agregue los descuentos ---------------------
          
          contrato.descuento_importe_noche=descuento_porNoche
          contrato.descuento_total_calcularo=descuento_total_importe
          contrato.aumento_total= aumento_Total
          
         #----------------------------------------------------------- 
       
          contrato.importe_otros_gasto = importe_otros_gast
        
          contrato.estado=true_variable
          
          
          #------------------aguegue esto para ver el total en pantalla---------
          total_Para_ver = contrato.total
          
          #-----------------------------------------------------------
          usuario= request.user #necesito meter tambien el usuario
           
          contrato.user= usuario
          
          
      #---------------agregue el iva -----------------------------
          contrato.porcentaje_de_senia_reservas= float(porcentaje_senia_reserva)
       
        
          
          
       
        
         
          
               
          
          
         
          try:
          
           
        
         
           ponerOcupada_ultimaHabitacion(request, habitacions)
           ponerTrue_alUltimoContrato(request, habitacions)
          
           
          
           contrato.save()
           
          
    
     #------------------------------------------------------------------
           
          
           
          
       
               
           
           
          
        
           messages.success(request, "El contrato se guardo correctamente...")
          
          
               
            
           
           
          except:
               messages.error(request, "El contrato no se guardo...")
               
               #----------para probar--------------
              # ponerFalse_alUltimoContrato(request, habitacions)
               ponerLIbre_ultimaHabitacion(request, habitacions)
               
               
          return redirect("modificarContrato")
               
               
        
             
                    
      
             
          
     else:
         form2 = FormContrato()
     
     
     
     return render(request, "contrato/contrato.html", {'formHuesped': form, 'formContrato': form2, 'total': total, 'importe_de_otros_gastos':importe_otros_gast, 'importe_estadia':importeEstadia, 'diferenciaConvertida':diferenciaConvertida, 'descuento':descuento_porNoche, 'descuento_total': descuento_total_importe, 'aumento':aumento_Total, 'total_Para_ver':total_Para_ver})
     
     
   
               
              
             
def modificarContrato(request):
          
     contratos = Contrato.objects.all()
     true = True
     contratos_true = list()
     
     for contrato in contratos:
          if contrato.estado== true:
               contratos_true.append(contrato)
     
     return render(request, "contrato/modificarContrato.html",{'contratos': contratos_true})  



def modificarTablaContrato(request, id_contrato):
       #contrato = Contrato()
     formContrato = FormContrato()
     
     contrato = get_object_or_404(Contrato, id=id_contrato)
     
     habitacion_para_form = contrato.habitacion
     
    
     
    
     
     
     #.....................................ahora obtengo el huesped y el contrato mediante el id........................
   
     
     if request.method == "POST":
          #contrato = get_object_or_404(Contrato, id=id_contrato)
          variable_true = True
        
          habitacions = contrato.habitacion.id
          
          #---------------------------------
          huespeds =request.POST.get("huesped")# id
          #--------------------------------------------------------
          
          #huesped = Huesped.objects.get(id= huespeds)
          huesped = get_object_or_404(Huesped, id=huespeds)# cambie esto a ultimo momento
          
          
          descuento_porNoche= request.POST.get("descuento_importe_noche")
          descuento_total_importe= request.POST.get("descuento_total_calcularo")
          aumento_Total= request.POST.get("aumento_total")
          
          
          
          #----------------------------volver atras------------------------------------------
          porcentaje_senia_reserva= request.POST.get("porcentaje_de_senia_reservas")
          
          true_variable = True
          
          
     
         # fecha_entra = request.POST.get("fecha_entrada")
          fecha_sali = request.POST.get("fecha_salida")
          fecha_entra = request.POST.get("fecha_entrada")
         # importe_estad= request.POST.get("importe_estadia")
          importe_otros_gast= request.POST.get("importe_otros_gasto")
         # late_check_out = request.POST.get("late_chack_out")
          #totals= request.POST.get("total")
         # habitacion = Habitacion.objects.get(id= habitacions)
         # huesped = Huesped.objects.get(id=huespeds)
          id_habitacion = contrato.habitacion.id
          habitacion = get_object_or_404(Habitacion, id=id_habitacion)
          
          #---------------------para volver atras------------
          
        
          fechaConvertida = datetime.datetime.strptime(fecha_entra, '%Y-%m-%dT%H:%M')
     
          fechaConvertida2 = datetime.datetime.strptime(fecha_sali, '%Y-%m-%dT%H:%M')
          fechaFormateada2 = fechaConvertida2.strftime('%Y-%m-%dT%H:%M') 
          
          fechaFormateada = fechaConvertida.strftime('%Y-%m-%dT%H:%M') 
          
          
          #--------------------años que no coinciden-------------------
          #fechaSalidaEntero = int(fechaConvertida2.strftime('%y'))
          #fechaEntradaEntero = int(fechaConvertida.strftime('%y'))
          
          
             #-------fuera del horario----volver atras------
          if fechaConvertida2.hour <10 or fechaConvertida2.hour>=18:
                messages.error(request, "El horario no corresponde")
                return redirect('Contrato')
           
           
             #---------------------------hago esto para cuando los años de entrada y salida no coinciden-------------------------------
        
          #elif fechaEntradaEntero > fechaSalidaEntero:
               # messages.error(request, "Los años no corresponden")
                  
               # print("fecha entrada año", fechaEntradaEntero)
              #  print("fecha salida año", fechaSalidaEntero)
          
               # return redirect('Contrato')
          
           #-------------para comparar si la fecha entrada es mayor a la fecha salida-----------
          
          elif fechaConvertida >= fechaConvertida2:
                messages.error(request, "La entrada es mayor o igual a la salida")
                return redirect('Contrato')
           
          
           
          
          
         
          
           
           
           
           
          else:
                #paraAnular_habitacionAnterior_Actualizar(request, contrato)
               total =calcularTotal(request, fecha_entra, fecha_sali, habitacions, importe_otros_gast)
          
               importeEstadia =calcularImporteEstadia(request, fecha_entra, fecha_sali, habitacions, importe_otros_gast)
          
               diferenciaConvertida = contrato.nochesDeEstadia(fecha_entra, fecha_sali, habitacions, importe_otros_gast)
          
          
               if int(descuento_porNoche) != 0 and int(descuento_total_importe) != 0:
               
                messages.error(request, "ingreso porcentajes en opciones no permitidas")
                return redirect('Contrato')
          
         # elif  int(descuento_porNoche) != 0 and int(aumento_Total) != 0:
             #   messages.error(request, "ingreso porcentajes en varias opciones")
             #   return redirect('Contrato')
         # elif int(descuento_total_importe) != 0 and int(aumento_Total) != 0:
             #  messages.error(request,"ingreso porcentajes en varias opciones")
              # return redirect('Contrato')
          
               elif int(descuento_total_importe) != 0 and int(aumento_Total) != 0 and int(descuento_porNoche) != 0:
                 messages.error(request,"ingreso porcentajes en opciones no permitidas")
                 return redirect('Contrato')
          
               
               if int(descuento_porNoche) != 0 and int(aumento_Total) ==0:
               
               
             #-------volver---atras--------------------------------------------------
             
                if fechaConvertida2.hour==10 and fechaConvertida2.minute==0:
                     total_estadia_con_descuento_diez =descuento_delTotal_Promocion_chekOut_diez_actualizar_tabla(request, fecha_entra, fecha_sali, habitacions, importe_otros_gast)
                     contrato.importe_estadia= total_estadia_con_descuento_diez
                    # contrato.total = total_estadia_con_descuento_diez + float(importe_otros_gast)
                    
                    
                     suma= total_estadia_con_descuento_diez + float(importe_otros_gast)
                     descuento2= suma *float(porcentaje_senia_reserva)/100
                     contrato.total = suma - descuento2
                     
                     
                     #-------volver---atras---------------------------------------------
                     messages.success(request, "agrego descuento al precio de la habitacion por cada noche")
                    
                    
                else:
                    if fechaConvertida2.hour >=10 and fechaConvertida2.hour <18:
                          total_estadia_con_descuento_Late =descuento_delTotal_Promocion_menosLate_actualizarTabla(request, fecha_entra, fecha_sali, habitacions, importe_otros_gast)
                          contrato.importe_estadia= total_estadia_con_descuento_Late
                         # contrato.total= total_estadia_con_descuento_Late + float(importe_otros_gast)
                          
                          suma2= total_estadia_con_descuento_Late + float(importe_otros_gast)
                          descuento3= suma2 *float(porcentaje_senia_reserva)/100
                          contrato.total = suma2 - descuento3
                     
                          
                          
                          #------volver---atras-------------------------------
                          
                          
                          messages.success(request, "agrego descuento al precio de la habitacion por cada noche")
                        
                         
                    
                   
          
                     
                     
        
                  
               elif int(aumento_Total) != 0 and  int(descuento_porNoche) == 0 and int(descuento_total_importe)== 0: # esto lo agregue a lo ultimo de la noche
                 contrato.importe_estadia= importeEstadia
                
                 aumento_total = total* float(aumento_Total) /100
                 aumento_total2 = aumento_total
                 
                 #-----------------volver atras----- ------------------------------volve------------  ---------
                 
                 contrato.total= total + aumento_total2
                 
                 descuento2 = float(contrato.total) *float(porcentaje_senia_reserva)/100
                 
                 contrato.total = float(contrato.total) -descuento2
             
                 messages.success(request, "agrego un aumento al total del importe")
          
          #-------volver atras-------------------------------------------------- ----- ---------
               elif  int(descuento_total_importe) !=0  and int(aumento_Total) ==0: # esto lo agregue ahor para volver atras-----
                 contrato.importe_estadia= importeEstadia
                
                 descuentoTotal = total* float(descuento_total_importe) /100
                 descuentoTotal2 = descuentoTotal
                  
               
                 contrato.total= total - descuentoTotal2
                 
                 
                 descuento2= float(contrato.total)  *float(porcentaje_senia_reserva)/100
                 
                 contrato.total= float(contrato.total)- descuento2
                 
               
               
                 messages.success(request, "agrego descuento al total")
                 
         #---------------------------APRETANDO DOS OPCIONES------------------------------- 
         
               elif int(descuento_porNoche) != 0 and int(aumento_Total) != 0:
                contrato.habitacion =habitacion 
          
                contrato.huesped = huesped
                contrato.fecha_entrada= fechaFormateada
                contrato.fecha_salida = fechaFormateada2
          
          #-------------------agregue los descuentos ---------------------
          
                contrato.descuento_importe_noche=descuento_porNoche
                contrato.descuento_total_calcularo=descuento_total_importe
                contrato.aumento_total= aumento_Total
          
         #-----------------------------para------------------------------ 
       
                contrato.importe_otros_gasto = importe_otros_gast
        
                contrato.estado=true_variable
       
        
         
               
             #---------------------------para volver atras-------------------
                if fechaConvertida2.hour==10 and fechaConvertida2.minute==0:
                     total_estadia_con_descuento_diez =descuento_delTotal_Promocion_chekOut_diez_actualizar_tabla(request, fecha_entra, fecha_sali, habitacions, importe_otros_gast)
                     contrato.importe_estadia= total_estadia_con_descuento_diez
                     contrato.total = total_estadia_con_descuento_diez + float(importe_otros_gast)
                     messages.success(request, "aplico un descuento por cada noche y un aumento sobre el total")
                     
               #-------------aumento-----------    
                     total= contrato.total
                     total2 = total *float(aumento_Total)/100
                     total3 = total +total2
                     
                     descuento2 = total3*float(porcentaje_senia_reserva)/100
                     
                     contrato.total = total3 -descuento2
                      
                     contrato.save()
                   
                    
                else:
                    if fechaConvertida2.hour >=10 and fechaConvertida2.hour <18:
                          total_estadia_con_descuento_Late =descuento_delTotal_Promocion_menosLate_actualizarTabla(request, fecha_entra, fecha_sali, habitacions, importe_otros_gast)
                          contrato.importe_estadia= total_estadia_con_descuento_Late
                          contrato.total= total_estadia_con_descuento_Late + float(importe_otros_gast)
                          messages.success(request, "aplico un descuento por cada noche y un aumento sobre el total")
                          
                        
                 
          #---------------------aumento-------------------------------
                  
                      
                    total= contrato.total
                    total2 = total *float(aumento_Total)/100
                    total3 = total +total2
                    
       
                    descuento2 = total3 *float(porcentaje_senia_reserva)/100
                   # contrato.total = total3
                    contrato.total = total3 - descuento2
                    contrato.save()
                    
                    
               elif  int(descuento_total_importe) !=0  and int(aumento_Total) != 0:
                 contrato.habitacion =habitacion 
          
                 contrato.huesped = huesped
                 contrato.fecha_entrada= fechaFormateada
                 contrato.fecha_salida = fechaFormateada2
          
          #-------------------agregue los descuentos ---------------------
          
                 contrato.descuento_importe_noche=descuento_porNoche
                 contrato.descuento_total_calcularo=descuento_total_importe
                 contrato.aumento_total= aumento_Total
          
         #----------------------------------------------------------- 
       
                 contrato.importe_otros_gasto = importe_otros_gast
        
                 contrato.estado=true_variable
       
                
                 contrato.importe_estadia= importeEstadia
                
                 descuentoTotal = total* float(descuento_total_importe) /100
                 descuentoTotal2 = descuentoTotal
                  
               
                 contrato.total= total - descuentoTotal2
               
                 
                 contrato.save()
               
                # messages.success(request, "agrego descuento al total importe")
                 #----------------------------------------
                 
                 total= contrato.importe_estadia
                      
                 estadia_mas_otros_gastos = float(contrato.importe_estadia)+ float(contrato.importe_otros_gasto)
                      
                 descuento =estadia_mas_otros_gastos*float(descuento_total_importe)/100
                      
                      
                 tota2 = estadia_mas_otros_gastos- descuento
                      
                 tota2 = tota2 + tota2 *float(aumento_Total)/100
                          
                 descuento_senia = tota2 * float(porcentaje_senia_reserva)/100
                      
                 #contrato.total = tota2 
                 contrato.total = tota2 - descuento_senia
                 
                 messages.success(request, "agrego descuento al total importe, y luego un aumento al total")
                      
                 contrato.save()
                   
                     
                 
         
                
               
               
          
             
               
               else:
               
               
                contrato.importe_estadia= importeEstadia
                
                
                #contrato.total= total
                descuento_senia =  total *float(porcentaje_senia_reserva) / 100
             
                
                contrato.total = total-descuento_senia
             
               
          
         
              
                         
               
              
               
               
               
               #------------------------------------------------------------------------
              
               id_habitacion = contrato.habitacion.id
               habitacion = get_object_or_404(Habitacion, id=id_habitacion)
              # importe_otros_gast= contrato.importe_otros_gasto
               late_check_out = habitacion.check_out_lates
               #importe_estadia = float(contrato.importe_estadia)+ float(late_check_out)
              # total = float(importe_estadia)+ float(importe_otros_gast)
               total =calcularTotal(request, fecha_entra, fecha_sali, habitacions, importe_otros_gast)
          
               importeEstadia =calcularImporteEstadia(request, fecha_entra, fecha_sali, habitacions, importe_otros_gast)
               
               
                #---------------------volver atras y desbloquera lo de abajo---------------------
               contrato.habitacion =habitacion # obtuve la habitacion mediante el id
          
               contrato.huesped = huesped
               contrato.fecha_entrada= fechaFormateada
               contrato.fecha_salida = fechaFormateada2
               
            
          
                #-------------------agregue los descuentos ---------------------
          
               contrato.descuento_importe_noche=descuento_porNoche
               contrato.descuento_total_calcularo=descuento_total_importe
               contrato.aumento_total= aumento_Total
          
         #----------------------------------------------------------- 
       
               contrato.importe_otros_gasto = importe_otros_gast
        
               contrato.estado=true_variable
               
               #-------guardo el usuario-----------------------
               usuario = request.user
               contrato.user=usuario
               #----------------------------------------------------
               
               """ contrato.total=total
          
               contrato.fecha_salida = fechaFormateada2
               contrato.fecha_entrada=fechaFormateada
               contrato.importe_estadia= importeEstadia
               contrato.importe_otros_gasto= importe_otros_gast
               #---------------agregue el huesped-----------------
               contrato.huesped=huesped
               
                #-------------------agregue los descuentos ---------------------
          
               contrato.descuento_importe_noche=descuento_porNoche
               contrato.descuento_total_calcularo=descuento_total_importe
               contrato.aumento_total= aumento_Total
           """
               #----------------------------------------------------------- 
               
           
               
              
               
               try:
                contrato.save()
                #habitacionOcupada(request, habitacions)#acabo de copiar esto de abajo
        
              
                messages.success(request, "El contrato se actualizo correctamente...")
               
                return redirect('modificarContrato')
               
               
               except:
                messages.error(request, "El contrato no se actualizo...")
                return redirect('modificarContrato')
            
              
               
          
     
     
     else:
          
          
          contrato.fecha_salida=  str(contrato.fecha_salida)
          contrato.fecha_entrada=  str(contrato.fecha_entrada)
          formContrato = FormContrato(instance=contrato)
          
     
     
     
     
     return render(request, "contrato/modificarTablaContrato.html", {'formContrato': formContrato, 'contrato':contrato, 'habitacion_para_form': habitacion_para_form})


    

def eliminarContrato(request, id_contrato):
     
    contrato = get_object_or_404(Contrato, id=id_contrato)
    nombre = Contrato.habitacion
    
   
   
    #ponerFalse_cuando_elimino(request, id_contrato)
    
    #----------------------agrego esto antes no estaba----------------------------------
    id_habitacion = contrato.habitacion.id
    habitacion = get_object_or_404(Habitacion, id=id_habitacion)
    habitacion.estado="Null"
    habitacion.save()
    
  
    
   
 
  
    
    try:
         contrato.delete()
        
        
         
     
       
         messages.success(request, "El contrato se elimino correctamente...")
         
         
    except:
         messages.error(request, "El contrato no se elimino...")
         
   
         
    return redirect('modificarContrato')





def calcularTotal(request, fecha_entra, fecha_sali, habitacions, importe_otros_gasto):
          contrato = Contrato()
          #total =0
         
     
     
         
          total = contrato.calcularFechas(fecha_entra, fecha_sali, habitacions, importe_otros_gasto)
          
    
     
          return total
     
     
def calcularImporteEstadia(request, fecha_entra, fecha_sali, habitacions, importe_otros_gasto):
          
          contrato = Contrato()
          #total =0
         
     
     
         
          importeEstadia = contrato.calcularImporteEstadia(fecha_entra, fecha_sali, habitacions, importe_otros_gasto)
          
    
     
          return importeEstadia
     
     
     
     
def habitacionOcupada(request, habitacions):
     
    # habitacion=Habitacion()
     
     if request.method == 'POST':
          
          # habitacion = Habitacion.objects.get(id= habitacions)
           habitacion = get_object_or_404(Habitacion, id=habitacions)
           habitacion.estado="ocupada"
           
           habitacion.save()
     
     

# def  ponerNull_elimino(request, id_contrato):
#      # esta funcion es para cuando elimino un contrato la habitacion me aparezca Null o sea lista para alquilar
#       contrato = Contrato.objects.get(id= id_contrato)
      
#       id = contrato.habitacion.id
      
#       if request.method == 'GET':
#             habitacion = Habitacion.objects.get(id= id)
#             habitacion.estado="Null"
#             habitacion.save()
            
def habilitar_ocupadas(request, id_habitacion):
     
     contrato = Contrato.objects.all()
     
     False_variable = False
     
     if request.method == 'GET':
           # habitacion = Habitacion.objects.get(id= id_habitacion)
            habitacion = get_object_or_404(Habitacion, id=id_habitacion)

            habitacion.estado="Null"
            habitacion.save()
            
            
            #-------------le greguego esto------------------------
            
            for contr in contrato:
                 
                 if contr.habitacion== habitacion:
                      contr.estado= False_variable
                      contr.save()
            return redirect('Panel')
       
       
       
 
        
      
def ponerFalse_cuando_elimino(request, id_contrato):
     # contrato = Contrato.objects.get(id= id_contrato)
      contrato = get_object_or_404(Contrato, id=id_contrato)
     
      id = contrato.habitacion.id
      habitacion = Habitacion.objects.get(id= id)
     
      #------le agrego esto---------------------
     
     
    
   
      #False_variable=False
     
     
      #contrato.estado= False_variable
     # #-------le agreegue esto-----------
      #contrato.habitacion.estado = "Null"
      # #-----------------------------------
      #contrato.save()
     
      #habitacion.estado="Null"
      #habitacion.save()
    
      return redirect('Panel')
 
 
def ponerTrue_alUltimoContrato(request, habitacions):
     contrato=Contrato()
    # habitacion = Habitacion.objects.get(id = habitacions)
     habitacion = get_object_or_404(Habitacion, id=habitacions)
    
     variableTrue = True
     variableFalse = False
     
     contratos = Contrato.objects.filter(habitacion=habitacion)
     ultimo=list()
     
    # habitacion = Habitacion.objects.get(id=habitacions)
     habitacion = get_object_or_404(Habitacion, id=habitacions)
    
          
    
     
     for contra in contratos:
          if contra.importe_estadia >0:
               ultimo.append(contra)
              #print("contratos de habitaciones", contratos)
              # print("ultimo contrarto", ultimo[-1])
               if ultimo[-1] == contra.habitacion:
                    contra.estado=variableTrue
                   
                    contra.save()
                    
               else:
                    contra.estado=variableFalse
                  
                    contra.save()
                   
                    
    
def ponerOcupada_ultimaHabitacion(request, habitacions):
     # habitacion = Habitacion.objects.get(id=habitacions)
      habitacion = get_object_or_404(Habitacion, id=habitacions)
      
      habitacion.estado="ocupada"
      habitacion.save()
      
      
def lateCheckout(request, id_contrato):
     formContrato=FormContrato()
     
     #----------------------------para volver atras--------------------------------
     contrato = get_object_or_404(Contrato, id=id_contrato)
     
     habitacion_para_form = contrato.habitacion
     
    
     
    
     
     
     #.....................................ahora obtengo el huesped y el contrato mediante el id........................
   
     
     if request.method == "POST":
          #contrato = get_object_or_404(Contrato, id=id_contrato)
          variable_true = True
        
          habitacions = contrato.habitacion.id
          
          #---------------------------------
          huespeds =request.POST.get("huesped")# id
          #--------------------------------------------------------
          
          #huesped = Huesped.objects.get(id= huespeds)
          huesped = get_object_or_404(Huesped, id=huespeds)# cambie esto a ultimo momento
          
          
          descuento_porNoche= request.POST.get("descuento_importe_noche")
          descuento_total_importe= request.POST.get("descuento_total_calcularo")
          aumento_Total= request.POST.get("aumento_total")
          
          
          
          #-------------------------------------------------------------
          
          true_variable = True
          
          
     
         # fecha_entra = request.POST.get("fecha_entrada")
          fecha_sali = request.POST.get("fecha_salida")
          fecha_entra = request.POST.get("fecha_entrada")
         # importe_estad= request.POST.get("importe_estadia")
          importe_otros_gast= request.POST.get("importe_otros_gasto")
         # late_check_out = request.POST.get("late_chack_out")
          #totals= request.POST.get("total")
         # habitacion = Habitacion.objects.get(id= habitacions)
         # huesped = Huesped.objects.get(id=huespeds)
          id_habitacion = contrato.habitacion.id
          habitacion = get_object_or_404(Habitacion, id=id_habitacion)
          
          #---------------------para volver atras------------
          
        
          fechaConvertida = datetime.datetime.strptime(fecha_entra, '%Y-%m-%dT%H:%M')
     
          fechaConvertida2 = datetime.datetime.strptime(fecha_sali, '%Y-%m-%dT%H:%M')
          fechaFormateada2 = fechaConvertida2.strftime('%Y-%m-%dT%H:%M') 
          
          fechaFormateada = fechaConvertida.strftime('%Y-%m-%dT%H:%M') 
          
             #-------fuera del horario----volver atras------
             
          hora= fechaFormateada = fechaConvertida.strftime('%Y-%m-%dT%H:%M') 
          min= fechaFormateada = fechaConvertida.strftime('%Y-%m-%dT%H:%M') 
            
             
             
             #-------------------------------------
          
           
          if fechaConvertida2.hour <10 or fechaConvertida2.hour>=18:
                messages.error(request, "El horario no corresponde")
                return redirect('modificarContrato')
          
          
          elif  fechaConvertida2.hour ==10 and fechaConvertida2.minute==0 and fechaConvertida2.second==0:
               messages.error(request, "El horario no corresponde al late check out")
               return redirect('modificarContrato')
          
          elif fechaConvertida2.day != contrato.fecha_salida.day:
               messages.error(request, "El dia no corresponde al late check out")
               return redirect('modificarContrato')
          
          
        
          
         
          
           
           
           
           
          else:
                #paraAnular_habitacionAnterior_Actualizar(request, contrato)
               total =calcularTotal(request, fecha_entra, fecha_sali, habitacions, importe_otros_gast)
          
               importeEstadia =calcularImporteEstadia(request, fecha_entra, fecha_sali, habitacions, importe_otros_gast)
          
               diferenciaConvertida = contrato.nochesDeEstadia(fecha_entra, fecha_sali, habitacions, importe_otros_gast)
          
          
     #           if int(descuento_porNoche) != 0 and int(descuento_total_importe) != 0:
               
     #            messages.error(request, "ingreso porcentajes en varias opciones")
     #            return redirect('Contrato')
          
     #     # elif  int(descuento_porNoche) != 0 and int(aumento_Total) != 0:
     #         #   messages.error(request, "ingreso porcentajes en varias opciones")
     #         #   return redirect('Contrato')
     #     # elif int(descuento_total_importe) != 0 and int(aumento_Total) != 0:
     #         #  messages.error(request,"ingreso porcentajes en varias opciones")
     #          # return redirect('Contrato')
          
     #           elif int(descuento_total_importe) != 0 and int(aumento_Total) != 0 and int(descuento_porNoche) != 0:
     #             messages.error(request,"ingreso porcentajes en varias opciones")
     #             return redirect('Contrato')
          
               
               if int(descuento_porNoche) != 0 and int(aumento_Total) ==0:
               # messages.success(request, "agrego descuento al precio de la habitacion por cada noche")
               
             
             
                if fechaConvertida2.hour==10 and fechaConvertida2.minute==0:
                     total_estadia_con_descuento_diez =descuento_delTotal_Promocion_chekOut_diez_actualizar_tabla(request, fecha_entra, fecha_sali, habitacions, importe_otros_gast)
                     contrato.importe_estadia= total_estadia_con_descuento_diez
                     contrato.total = total_estadia_con_descuento_diez + float(importe_otros_gast)
                    
          
                    
                    
                else:
                    if fechaConvertida2.hour >=10 and fechaConvertida2.hour <18:
                          total_estadia_con_descuento_Late =descuento_delTotal_Promocion_menosLate_actualizarTabla(request, fecha_entra, fecha_sali, habitacions, importe_otros_gast)
                          contrato.importe_estadia= total_estadia_con_descuento_Late
                          contrato.total= total_estadia_con_descuento_Late + float(importe_otros_gast)
                        
                         
                    
                   
          
                     
                     
        
                  
               elif int(aumento_Total) != 0 and  int(descuento_porNoche) == 0 and int(descuento_total_importe)== 0: # esto lo agregue a lo ultimo de la noche
                 contrato.importe_estadia= importeEstadia
                
                 aumento_total = total* float(aumento_Total) /100
                 aumento_total2 = aumento_total
                 contrato.total= total + aumento_total2
             
                 #messages.success(request, "agrego un aumento al total del importe")
          
          
               elif  int(descuento_total_importe) !=0  and int(aumento_Total) ==0: # esto lo agregue ahor para volver atras-----
                 contrato.importe_estadia= importeEstadia
                
                 descuentoTotal = total* float(descuento_total_importe) /100
                 descuentoTotal2 = descuentoTotal
                  
               
                 contrato.total= total - descuentoTotal2
                 
               
               
                # messages.success(request, "agrego descuento al total")
                 
         #---------------------------APRETANDO DOS OPCIONES------------------------------- 
         
               elif int(descuento_porNoche) != 0 and int(aumento_Total) != 0:
                contrato.habitacion =habitacion 
          
                contrato.huesped = huesped
                contrato.fecha_entrada= fechaFormateada
                contrato.fecha_salida = fechaFormateada2
          
          #-------------------agregue los descuentos ---------------------
          
                contrato.descuento_importe_noche=descuento_porNoche
                contrato.descuento_total_calcularo=descuento_total_importe
                contrato.aumento_total= aumento_Total
          
         #-----------------------------para------------------------------ 
       
                contrato.importe_otros_gasto = importe_otros_gast
        
                contrato.estado=true_variable
       
        
         
               # messages.success(request, "aplico un descuento por cada noche y un aumento sobre el total")
             #---------------------------para volver atras-------------------
                if fechaConvertida2.hour==10 and fechaConvertida2.minute==0:
                     total_estadia_con_descuento_diez =descuento_delTotal_Promocion_chekOut_diez_actualizar_tabla(request, fecha_entra, fecha_sali, habitacions, importe_otros_gast)
                     contrato.importe_estadia= total_estadia_con_descuento_diez
                     contrato.total = total_estadia_con_descuento_diez + float(importe_otros_gast)
                     
               #-------------aumento-----------    
                     total= contrato.total
                     total2 = total *float(aumento_Total)/100
                     total3 = total +total2
                     
                     contrato.total = total3
                      
                     contrato.save()
                   
                    
                else:
                    if fechaConvertida2.hour >=10 and fechaConvertida2.hour <18:
                          total_estadia_con_descuento_Late =descuento_delTotal_Promocion_menosLate_actualizarTabla(request, fecha_entra, fecha_sali, habitacions, importe_otros_gast)
                          contrato.importe_estadia= total_estadia_con_descuento_Late
                          contrato.total= total_estadia_con_descuento_Late + float(importe_otros_gast)
                          
                        
                 
          #---------------------aumento-------------------------------
                  
                      
                    total= contrato.total
                    total2 = total *float(aumento_Total)/100
                    total3 = total +total2
                    
       
                     
                    contrato.total = total3
                      
                    contrato.save()
                    
                    
               elif  int(descuento_total_importe) !=0  and int(aumento_Total) != 0:
                 contrato.habitacion =habitacion 
          
                 contrato.huesped = huesped
                 contrato.fecha_entrada= fechaFormateada
                 contrato.fecha_salida = fechaFormateada2
          
          #-------------------agregue los descuentos ---------------------
          
                 contrato.descuento_importe_noche=descuento_porNoche
                 contrato.descuento_total_calcularo=descuento_total_importe
                 contrato.aumento_total= aumento_Total
          
         #----------------------------------------------------------- 
       
                 contrato.importe_otros_gasto = importe_otros_gast
        
                 contrato.estado=true_variable
       
                
                 contrato.importe_estadia= importeEstadia
                
                 descuentoTotal = total* float(descuento_total_importe) /100
                 descuentoTotal2 = descuentoTotal
                  
               
                 contrato.total= total - descuentoTotal2
                 
                 contrato.save()
               
                # messages.success(request, "agrego descuento al total importe")
                 #----------------------------------------
                 
                 total= contrato.importe_estadia
                      
                 estadia_mas_otros_gastos = float(contrato.importe_estadia)+ float(contrato.importe_otros_gasto)
                      
                 descuento =estadia_mas_otros_gastos*float(descuento_total_importe)/100
                      
                      
                 tota2 = estadia_mas_otros_gastos- descuento
                      
                 tota2 = tota2 + tota2 *float(aumento_Total)/100
                          
                     
                      
                 contrato.total = tota2
                 
                # messages.success(request, "agrego descuento al total importe, y luego un aumento al total")
                      
                 contrato.save()
                   
                     
                 
         
                
               
               
          
               
               
               else:
               
               
                contrato.importe_estadia= importeEstadia
                contrato.total= total
                contrato.fecha_salida = str(contrato.fecha_salida) 
                contrato.fecha_entrada = str(contrato.fecha_entrada)
                contrato.huesped
                contrato.aumento_total
                contrato.descuento_importe_noche
                contrato.aumento_total
                formContrato=FormContrato(instance=contrato)
             
               
          
         
              
                         
               
              
               
               
               
               #------------------------------------------------------------------------
              
               id_habitacion = contrato.habitacion.id
               habitacion = get_object_or_404(Habitacion, id=id_habitacion)
              # importe_otros_gast= contrato.importe_otros_gasto
               late_check_out = habitacion.check_out_lates
               #importe_estadia = float(contrato.importe_estadia)+ float(late_check_out)
              # total = float(importe_estadia)+ float(importe_otros_gast)
               total =calcularTotal(request, fecha_entra, fecha_sali, habitacions, importe_otros_gast)
          
               importeEstadia =calcularImporteEstadia(request, fecha_entra, fecha_sali, habitacions, importe_otros_gast)
               
               
                #---------------------volver atras y desbloquera lo de abajo---------------------
               contrato.habitacion =habitacion # obtuve la habitacion mediante el id
          
               contrato.huesped = huesped
               contrato.fecha_entrada= fechaFormateada
               contrato.fecha_salida = fechaFormateada2
               
            
          
                #-------------------agregue los descuentos ---------------------
          
               contrato.descuento_importe_noche=descuento_porNoche
               contrato.descuento_total_calcularo=descuento_total_importe
               contrato.aumento_total= aumento_Total
          
         #----------------------------------------------------------- 
       
               contrato.importe_otros_gasto = importe_otros_gast
        
               contrato.estado=true_variable
               
               #------guardar el usuario----------------------------------
               usuario2 = request.user
               contrato.user = usuario2
       
               
               """ contrato.total=total
          
               contrato.fecha_salida = fechaFormateada2
               contrato.fecha_entrada=fechaFormateada
               contrato.importe_estadia= importeEstadia
               contrato.importe_otros_gasto= importe_otros_gast
               #---------------agregue el huesped-----------------
               contrato.huesped=huesped
               
                #-------------------agregue los descuentos ---------------------
          
               contrato.descuento_importe_noche=descuento_porNoche
               contrato.descuento_total_calcularo=descuento_total_importe
               contrato.aumento_total= aumento_Total
           """
               #----------------------------------------------------------- 
               
               #-----------------S--para volver atras-----------------------
               
              
               
               try:
                contrato.save()
                #habitacionOcupada(request, habitacions)#acabo de copiar esto de abajo
        
              
                messages.success(request, "El late check out se agrego correctamente...")
               
                return redirect('modificarContrato')
               
               
               except:
                messages.error(request, "El late check out no se agrego...")
                return redirect('modificarContrato')
            
              
               
          
     
     
     else:
          
          
          contrato.fecha_salida=  str(contrato.fecha_salida)
          contrato.fecha_entrada=  str(contrato.fecha_entrada)
          formContrato = FormContrato(instance=contrato)
          
     
     
     
     
     return render(request, "contrato/late_check.html", {'contrato': contrato, 'formContrato': formContrato})

    
     
     
     
    
     
     
    
     
     
  
def contratosTotales(request):
     
     contratos = Contrato.objects.all()  
     
     return render(request, 'contrato/tablaContratos_totales.html', {'contratos':contratos})   




class generar_reporter_huespedes(View):
     
   
   
     
     def get(self, request, *args, **kwargs): # **kwargs es un diccionario de argumentos por si les paso
         
          id=self.kwargs.get("id") # lo reconoce como id a los dos nombres, pongo id_huesped y no funciona
       
          huespedes = Huesped.objects.all()
          huesped = get_object_or_404(Huesped, id=id)
          fecha = huesped.created
          
          template_name= "contrato/reporter_huesped.html"
          
          data={'cantidad': huespedes.count(), # a count() es solo un ejemplo no lo voy a usar
                'huespedes': huespedes,
                'huesped': huesped,
                'fecha': fecha
                
              
             
              
                
                } # count es para saber la cantidad de objetos que tiene el modelo huesped
          
          pdf = render_to_pdf(template_name, data) # aca le mando el template y el contenido(contexto, diccionario) a la funcion de utulitario donde me convierte el template a pdf
          
          return HttpResponse(pdf, content_type= 'application/pdf' )
     
     
     
def cambiar_total(request, id_contrato):
     
     contrato = get_object_or_404(Contrato, id=id_contrato)
   
     data={
          'habitacion': contrato.habitacion,
          'huesped': contrato.huesped,
          'fecha_entrada': contrato.fecha_entrada,
          'fecha_salida': contrato.fecha_salida,
          'total_anterior': contrato.total
          
     }
     
     if request.method == "POST":
          total_cambiado = request.POST.get("cambiar_total")
          contrato.total= total_cambiado
          #---------guardar el usuario----------------------
          usuario3= request.user
          contrato.user= usuario3
          
          try:
           contrato.save()
           messages.success(request, "El total se actualizo correctamente...")
           
          except:
               messages.error(request, "El total no se actualizo...")
          return redirect('modificarContrato')
     
     
    # return render(request, "contrato/cambiar_total.html", {'data': data})





def descuento_delTotal_Promocion_menosLate(request, fecha_entra, fecha_sali, habitacions, importe_otros_gast):
          contrato= Contrato()
          
          
     
          habitacions = request.POST.get("habitacion")
          
          habitacion = get_object_or_404(Habitacion, id=habitacions)
          
         # habitacion = Habitacion.objects.get(id = habitacions)
        
          fecha_entra = request.POST.get("fecha_entrada")
          fecha_sali = request.POST.get("fecha_salida")
         
          importe_otros_gast= request.POST.get("importe_otros_gasto")
          
          descuento= request.POST.get("descuento_importe_noche")
          # descuento= request.POST.get("descuento")
        
         
     
          importeEstadia =calcularImporteEstadia(request, fecha_entra, fecha_sali, habitacions, importe_otros_gast)
          diferenciaConvertida = contrato.nochesDeEstadia(fecha_entra, fecha_sali, habitacions, importe_otros_gast)
          
         
          
          retas1 = importeEstadia 
          
          resta2 = retas1- float(habitacion.check_out_lates)
          
          resta3 = resta2 / diferenciaConvertida
          
          #..................aca tengo el precio por noche de la habitacion-----------
          
          total1 = resta3 * int(descuento) /100
          #..................................................
          total2 = diferenciaConvertida*total1
          
          #----------------------------------------------
          
          total_con_descuento = importeEstadia - total2
          
          #------------le agrego el late check aut---------------------
          
          
          
          
          
          
          return total_con_descuento # este seria el importe de estadia NO  el total

          

def descuento_delTotal_Promocion_chekOut_diez(request, fecha_entra, fecha_sali, habitacions, importe_otros_gast):
          contrato= Contrato()
          
         
          
     
          habitacions = request.POST.get("habitacion")
          
         # habitacion = Habitacion.objects.get(id = habitacions)
          habitacion = get_object_or_404(Habitacion, id=habitacions)
        
          fecha_entra = request.POST.get("fecha_entrada")
          fecha_sali = request.POST.get("fecha_salida")
         
          importe_otros_gast= request.POST.get("importe_otros_gasto")
          
          #descuento= request.POST.get("descuento")
          descuento= request.POST.get("descuento_importe_noche")
          
        

     
          importeEstadia =calcularImporteEstadia(request, fecha_entra, fecha_sali, habitacions, importe_otros_gast)
          diferenciaConvertida = contrato.nochesDeEstadia(fecha_entra, fecha_sali, habitacions, importe_otros_gast)
          
        
          
          retas1 = importeEstadia 
          
          resta2 = retas1
          
          resta3 = resta2 / diferenciaConvertida
          
          #..................aca tengo el precio por noche de la habitacion-----------
          #para volver-------------------------------------
          
          total1 = resta3 * int(descuento) /100
          #..................................................
          total2 = diferenciaConvertida*total1
          
          #----------------------------------------------
          
          total_con_descuento = importeEstadia - total2
          
          
          
          return total_con_descuento # este seria el importe de estadia NO  el total

          
          
#----------para volver atras -------------PARA DESCUENTO POR NOCHE EN ACTUALIZAR TABLA-------------------
def descuento_delTotal_Promocion_menosLate_actualizarTabla(request, fecha_entra, fecha_sali, habitacions, importe_otros_gast):
          contrato= Contrato()
          
          
     
          #habitacions = request.POST.get("habitacion")
          
          habitacion = get_object_or_404(Habitacion, id=habitacions)
          
         # habitacion = Habitacion.objects.get(id = habitacions)
        
          fecha_entra = request.POST.get("fecha_entrada")
          fecha_sali = request.POST.get("fecha_salida")
         
          importe_otros_gast= request.POST.get("importe_otros_gasto")
          
          descuento= request.POST.get("descuento_importe_noche")
          # descuento= request.POST.get("descuento")
        
         
     
          importeEstadia =calcularImporteEstadia(request, fecha_entra, fecha_sali, habitacions, importe_otros_gast)
          diferenciaConvertida = contrato.nochesDeEstadia(fecha_entra, fecha_sali, habitacions, importe_otros_gast)
          
         
          
          retas1 = importeEstadia 
          
          resta2 = retas1- float(habitacion.check_out_lates)
          
          resta3 = resta2 / diferenciaConvertida
          
          #..................aca tengo el precio por noche de la habitacion-----------
          
          total1 = resta3 * int(descuento) /100
          #..................................................
          total2 = diferenciaConvertida*total1
          
          #----------------------------------------------
          
          total_con_descuento = importeEstadia - total2
          
          #------------le agrego el late check aut---------------------
          
          
          
          
          
          
          return total_con_descuento # este seria el importe de estadia NO  el total



def descuento_delTotal_Promocion_chekOut_diez_actualizar_tabla(request, fecha_entra, fecha_sali, habitacions, importe_otros_gast):
          contrato= Contrato()
          
         
          
     
         #habitacions = request.POST.get("habitacion")
          
         # habitacion = Habitacion.objects.get(id = habitacions)
          habitacion = get_object_or_404(Habitacion, id=habitacions)
        
          fecha_entra = request.POST.get("fecha_entrada")
          fecha_sali = request.POST.get("fecha_salida")
         
          importe_otros_gast= request.POST.get("importe_otros_gasto")
          
          #descuento= request.POST.get("descuento")
          descuento= request.POST.get("descuento_importe_noche")
          
        

     
          importeEstadia =calcularImporteEstadia(request, fecha_entra, fecha_sali, habitacions, importe_otros_gast)
          diferenciaConvertida = contrato.nochesDeEstadia(fecha_entra, fecha_sali, habitacions, importe_otros_gast)
          
        
          
          retas1 = importeEstadia 
          
          resta2 = retas1
          
          resta3 = resta2 / diferenciaConvertida
          
          #..................aca tengo el precio por noche de la habitacion-----------
          #para volver-------------------------------------
          
          total1 = resta3 * int(descuento) /100
          #..................................................
          total2 = diferenciaConvertida*total1
          
          #----------------------------------------------
          
          total_con_descuento = importeEstadia - total2
          
          
          
          return total_con_descuento # este seria el importe de estadia NO  el total

          
def ponerNullHabitacion_cuandoBorroUnHuesped_en_Contrato(request, id_huesped):
     
     huesped = get_object_or_404(Huesped, id=id_huesped)
     
     contratos = Contrato.objects.all()
     
     for con in contratos:
          if con.huesped== huesped and con.estado==True:
               id_habitacion = con.habitacion.id
               habitacion = get_object_or_404(Habitacion, id=id_habitacion)
               habitacion.estado="Null"
               habitacion.save()
               
               '''id_contrato = con.id
               contrato = get_object_or_404(Contrato, id=id_habitacion)
               contrato.estado=False
               contrato.save'''
               
          #else:
               
              # habitacion.estado="ocupada"
              # habitacion.save()
               
               
          
     
     '''huesped = get_object_or_404(Huesped, id=id_huesped)
     
     contrato = Contrato.objects.all()
     
     contratoHuesped = Contrato.objects.filter(huesped=huesped)
     
     for hues in contratoHuesped:
       if hues.habitacion.nombre_numero != None:
            id_habitacion = hues.habitacion.id
            habitacion = get_object_or_404(Habitacion, id=id_habitacion)
            habitacion.estado="Null"
            habitacion.save()'''
          
      
          
def penalidad(request, id_huesped):
       
        huesped = get_object_or_404(Huesped, id=id_huesped)
       # apellido = huesped.apellido
        
       
        if request.method == "GET": 
         huesped.penalidad = "SI"
         huesped.save()
         messages.success(request, "Se le agrego penalidad al huesped")
         
         return redirect('modificarHuesped')
       
               
     
def quitar_penalidad(request, id_huesped):
     
      huesped = get_object_or_404(Huesped, id=id_huesped)
       # apellido = huesped.apellido
        
       
      if request.method == "GET": 
         huesped.penalidad = "NO"
         huesped.save()
         messages.success(request, "Se le quito la penalizacion al huesped")
         
         return redirect('modificarHuesped')
       
   
       
    
def agregar_Producto(request, id_contrato):
     
  
    
     
     formProductos_agregados = FormsProductos_agregados()
     
    
   
    # contrato_id= request.POST.get("contrato")
     contrato = get_object_or_404(Contrato, id=id_contrato)
     
     huespedContrato = contrato.huesped
     
     agregar_Producto=Agregar_productos()
     
     
     
     
     lista2=list()
     
     lista=list()
     
     
     total_para_html=0
     
    
     
    
     
     
     
     
     productosAgregados_totales = Agregar_productos.objects.filter(contrato=contrato)
     
  
    
               
   
         
     
   
    
 #---------------------------volver atras ----------------------------------------------------------------
     
      # Listenig.objects.filter(id=1).update(value=90.0)
     
     if request.method=="POST":
            producto_id= request.POST.get("producto")
           
            cantidad= request.POST.get("cantidad")
            
          
            
            #----------------------------------------------------------------
            producto = get_object_or_404(Producto_al_publico, id=producto_id)
            
           
            
           
            total=0
          
            
           
            #----------------------------------------------------------------
            agregar_Producto.producto= producto
            agregar_Producto.contrato = contrato
            agregar_Producto.cantidad= cantidad
            
            agregar_Producto.total = float(cantidad)* float(producto.precio_al_publico)
          
            
            
            
            agregar_Producto.save()
            
            
             #........................guardar el usuario------------------------
            usuario4 = request.user
            contrato.user=usuario4
            contrato.save()
                #-------------------------------------------------------
            
            messages.success(request, "Se guardo correctamente...")
            
           
                
                 
         
           # return redirect(to=f'http://127.0.0.1:8000/contrato/AgregarProductos/{int(id_contrato)}')
            reverse("AgregarProductos", args=[id_contrato])

        
        
          
     
          
          
                      
                    
                      
            
     for agre in Agregar_productos.objects.raw('SELECT * FROM agregar_productos WHERE contrato_id = %s', [int(id_contrato)]):
                lista.append(agre.total)
               # print(lista)
                total= sum(lista)
               # print("el total es ", total)
                total_para_html= total
                
                #----------------------------------------------
               
               
                id_agregar = agre.id
                
               # Agregar_productos.objects.filter(contrato=contrato).update(total=33)
               # Agregar_productos.objects.update(total=33)
       
     #---------------------------------------------agregue esto------------------------
                contrato.total_consumidos= total_para_html
                
               
                
                contrato.save()
              
              
    
                    
                    
     return render(request, "contrato/tabla_agregarProductos.html", {'formProductos_agregados':formProductos_agregados, 'huespedContrato':huespedContrato, 'productosAgregados':productosAgregados_totales, 'total_para_html':total_para_html})
     
     
'''def my_custom_sql(precio_al_publics, cantidad, id_contrato): # esta conexion para hacer las consultas sql, lo saque de la pagina de django oficial donde dice raw, en español es (Realización de consultas SQL sin formato), entre a un link de la pagina raw
    with connection.cursor() as cursor:
      #  cursor.execute("UPDATE bar SET foo = 1 WHERE baz = %s", [self.baz])
       # cursor.execute("SELECT foo FROM bar WHERE baz = %s", [self.baz])
         # cursor.execute("UPDATE agregar_productos SET total= SUM(%s * %s) WHERE contrato_id =%s", [precio_al_public, cantidad, id_contrato])
          cursor.execute("SELECT SUM(%s * %s) FROM agregar_productos WHERE contrato_id = %s", [precio_al_publics, cantidad,  id_contrato])
       
       
          row = cursor.fetchone()

          return row'''
   


def eliminarAgregar(request, id_agregar):
     agregar = get_object_or_404(Agregar_productos, id=id_agregar)
     id_contrato= agregar.contrato.id
     contrato = get_object_or_404(Contrato, id=id_contrato)
     
     totalCon = contrato.total_consumidos
     
    # total_para_html= agregar.total
     productosAgregados_totales = Agregar_productos.objects.filter(contrato=contrato)
     
     #-----------------------------------------------
     lista= list()
    
     ultimo=0
     
     
     try:
          agregar.delete()
        
          
          
          #--------------guardar el usuario---------------------------
          
          usuario5= request.user
          contrato.user= usuario5
          contrato.save()
          
          #-----------------------------------------------------------
          
          messages.success(request, "El producto se elimino correctamente...")
         # Contrato.objects.update(total_consumidos=0)
          
          for agre in productosAgregados_totales:
               
               lista.append(agre.total)
               #ultimo = lista[-1]
               total=sum(lista)
             
             
               agre.contrato.total_consumidos =   float(agre.contrato.total_consumidos) - float(agre.total)
              
              # agre.contrato.total_consumidos =total
              # contrato.save() #agregue esto al lo ultimo xq al eliminar un producto no se me refleja el cambio en el total contrato
             
             
          
           
               
              
          
     except:
           messages.error(request, "El producto no se elimino")
           
     if len(lista) ==0:
               contrato.total_consumidos =0
               contrato.save()
              # print("llego hasta aca")
                    
           
           
     #return redirect(to=f'http://127.0.0.1:8000/contrato/AgregarProductos/{int(id_contrato)}')
     return HttpResponseRedirect(reverse("AgregarProductos", args=[id_contrato]))
    



#-----pongo estas dos funciones para si no me guarda el contrato ponga false i libre el contrato y la habitacion-----

def ponerLIbre_ultimaHabitacion(request, habitacions):
     # habitacion = Habitacion.objects.get(id=habitacions)
      habitacion = get_object_or_404(Habitacion, id=habitacions)
      
      habitacion.estado="Null"
      habitacion.save()
      
      
      
      
'''def ponerFalse_alUltimoContrato(request, habitacions):
     contrato=Contrato()
    # habitacion = Habitacion.objects.get(id = habitacions)
     habitacion = get_object_or_404(Habitacion, id=habitacions)
    
     variableTrue = True
     variableFalse = False
     
     contratos = Contrato.objects.filter(habitacion=habitacion)
     ultimo=list()
     
    # habitacion = Habitacion.objects.get(id=habitacions)
     habitacion = get_object_or_404(Habitacion, id=habitacions)
    
          
    
     
     for contra in contratos:
          if contra.importe_estadia >0:
               ultimo.append(contra)
              #print("contratos de habitaciones", contratos)
              # print("ultimo contrarto", ultimo[-1])
               if ultimo[-1] == contra.habitacion:
                    contra.estado=variableFalse
                   
                    contra.save()
                    
               else:
                    contra.estado=variableTrue
                  
                    contra.save()'''
                   
        
#-------------------------RECIBIR DATOS DE RESERVA PARA GUARDAR EN CONTRATO--------------------
'''class obtenerReserva(View):
   def get( **kwargs): # **kwargs es un diccionario de argumentos por si les paso
         
     nombre=kwargs.get("nombre_responsa2") # lo reconoce como id a los dos nombres, pongo id_huesped y no funciona
       
     
    
 
     form2=FormHuesped()
     form1=FormContrato()     
     huesped = Huesped()
     contrato=Contrato()
   
   
     
     
   
     huesped.nombre_responsable=nombre
        
    
        
         
  
     
      
   
      
    
     form2 = FormHuesped(instance=huesped)
     form1 = FormContrato(instance=contrato)
          
   
    
     return render("contrato/contrato.html", {'formHuesped': form2, 'formContrato': form1})'''


'''def reserva_mostrarDatos(request):
     form= FormHuesped()
     form2=FormContrato()
     
     if request.GET["hues"]:# hacemos un if que controle si viene informacion del formulario
    
      huespedReserva= request.GET["hues"]
     
     
      print(huespedReserva)
      print("hola mundo")
      print("hola", huespedReserva)
      
      return redirect("Contrato")
     
    
     
     return render(request, "contrato/contrato.html", {'formHuesped': form, 'formContrato': form2})'''
     
     
def recibir_id_reserva(request, id_reservas):
     
    #----------------------Reserva-------------------------------------------------
   
    # print("el id es ", id_reservas)
     
     reserva =  get_object_or_404(Reserva, id=id_reservas)
     id_huesped = reserva.huesped.id
     huesped_reserva =  get_object_or_404(HuespedReserva, id=id_huesped)
     
     
     reserva =  get_object_or_404(Reserva, id=id_reservas)
     
     huesped=Huesped()
     contrato=Contrato()
     
     form2 = FormHuesped()
     form1 = FormContrato()
     
    
     
     
     
     
     #--------------huesped reserva----------------------------------
     
     nombre= huesped_reserva.nombre
     apellido=huesped_reserva.apellido
     dni= huesped_reserva.dni
     telefono= huesped_reserva.telefono
      
     huesped.nombre_responsable= nombre
     huesped.apellido= apellido
     huesped.dni= dni
     huesped.telefono=telefono
     
      #------------------------------------------------------------------------------------------
    
               
          
     
    
     
     if request.method=="GET":
          
       
   
       form2 = FormHuesped(instance=huesped)
       return redirect("Contrato")
   
      # return HttpResponseRedirect(reverse("recibir_id", args=[id_reservas]))
     
    
    # mostrarContrato_reservas(request, id_reservas)
     
     return render(request, "contrato/contrato.html", {'formHuesped': form2, 'formContrato': form1})




#------------------------traje guardar huesped y guardar contrato para reservas-----------------



def mostrarContrato_reservas(request, id_reservas):
     form = FormHuesped()
     form2 = FormContrato()
     huesped=Huesped()
     contrato=Contrato()
     reserva =  get_object_or_404(Reserva, id=id_reservas)
     
     habitacion_template= reserva.habitacion
   
     
     huespedesReservas = HuespedReserva.objects.all()
     ultimoHuesped = Huesped.objects.all()
     
     ultimo = list()
     ultimoHues = list()
     
     
     for ult in ultimoHuesped:
          if ult.nombre_responsable != None:
               ultimo.append(ult)
               ultimoHues= ultimo[-1]
               
     #------------------comparar Habitaciones------------------------
     
    
               
      #---------------------------------------------------------- 
    # reserva =  get_object_or_404(Reserva, id=id_reservas)
     id_huesped = reserva.huesped.id
     huesped_reserva =  get_object_or_404(HuespedReserva, id=id_huesped)
     nombre= huesped_reserva.nombre
     apellido=huesped_reserva.apellido
     dni= huesped_reserva.dni
     telefono= huesped_reserva.telefono
      
     huesped.nombre_responsable= nombre
     huesped.apellido= apellido
     huesped.dni= dni
     huesped.telefono=telefono
     
     total_senias= reserva.total_senia
     
   #---------------------------porcentaje reserva seña----- -------------------
     #contrato.total = reserva.total_senia
     contrato.total =total_senias
     
     
     contrato.fecha_entrada= str(reserva.fecha_entrada)
     contrato.fecha_salida= str(reserva.fecha_salida)
     contrato.importe_otros_gasto= reserva.importe_otros_gasto
     contrato.descuento_importe_noche= reserva.descuento_importe_noche
     contrato.descuento_total_calcularo= reserva.descuento_total_calcularo
     contrato.aumento_total = reserva.aumento_total
     
     contrato.porcentaje_de_senia_reservas = reserva.porcentaje_de_senia
     
    # contrato.total_enviar_desdeReserva_a_contrato= reserva.total
    
    
    
    
    
     
     
     
     
     
    
     
     contrato.habitacion_reserva = habitacion_template.nombre_numero
    
      
     porcentaje_senia = reserva.porcentaje_de_senia
     #-------para mostrar el ultimo huesped en el html----------
     ultimoHuesped = Huesped.objects.all()
     
     huespedesReservas = HuespedReserva.objects.all()
     
     
     
     
     
       
      
    
     
     
   
     
     if request.method =='POST':
        
         
        
         
          formHuesped =FormHuesped(request.POST)
         
          if formHuesped.is_valid():
              
              formHuesped.save()
              
              messages.success(request, "El huesped se guardo correctamente...")
              
             # return redirect("Contrato") 
         
             
            
              return HttpResponseRedirect(reverse("huesped_Reserva", args=[id_reservas]))
              
           
              
          else:
              messages.error(request, "El huesped no se guardo...")
              
        
         
        
        
          
        
          
     
     else:
             #----------------------------------------------------------
     
                            
      
                
        
          
          
       form=FormHuesped(instance=huesped)
       form2=FormContrato(instance=contrato)
        #------------------------------------------------------------------------------------------
      
         
       
       
       
   
          #---agrego esto para mandar el huesped reserva ahuesped contrato
        
          
          
    # pasarDarosAContrato(request, id_reservas)  
         
    
     return render(request, "contrato/contrato.html", {'formHuesped': form, 'formContrato': form2, 'ultimoHuesped':ultimoHues, 'huespedeReser':huespedesReservas, 'habitacion_template':habitacion_template})
 
 
def  pasarDarosAContrato(request, id_reservas):
     
     form2 = FormContrato()
     
     
     
    # print("pasaje")
     reserva =  get_object_or_404(Reserva, id=id_reservas)
     contrato=Contrato()
     
     contrato.habitacion= reserva.habitacion
      #contrato.fecha_entrada= str(reserva.fecha_entrada)
      #contrato.fecha_salida= str(reserva.fecha_salida)
     contrato.fecha_entrada= str(reserva.fecha_entrada)
     contrato.fecha_salida= str(reserva.fecha_salida)
     contrato.importe_otros_gasto= reserva.importe_otros_gasto
     contrato.descuento_importe_noche= reserva.descuento_importe_noche
     contrato.descuento_total_calcularo= reserva.descuento_total_calcularo
     contrato.aumento_total = reserva.aumento_total
     
     #------------------------volver atrasss-------------------------
    # contrato.total_enviar_desdeReserva_a_contrato= reserva.total
    
    
    
    
     
     
     
     form2=FormContrato(instance=contrato)
     
     return render(request, "contrato/contrato.html", {'formContrato': form2})
     
     
'''def pasar_select(request):
     form = FormHuesped()
     form2 = FormContrato()
     id = request.GET["hues"]
     Reservas = Reserva.objects.all()
     
     
     print("el id del select es vv ", id)
     
     return render(request, "contrato/contrato.html", {'formHuesped': form, 'formContrato': form2, 'Reservas':Reservas})'''

   
def no_coinciden_los_totales(request, id_reserva, id_contrato, porcentaje_senia):
     
      reserva =  get_object_or_404(Reserva, id=id_reserva)
      
      contrato =  get_object_or_404(Contrato, id=id_contrato)
      
      if reserva.total != contrato.total + float(porcentaje_senia):
           
           messages.error(request, "Los resultados de contrato y reserva no coinciden")
           
           return redirect("Contrato")
           
     
     
def habilitar_habitaciones_tabla_contrato(request, id_habitacion):
     
     contrato = Contrato.objects.all()
     
     False_variable = False
     
     if request.method == 'GET':
           # habitacion = Habitacion.objects.get(id= id_habitacion)
            habitacion = get_object_or_404(Habitacion, id=id_habitacion)

            habitacion.estado="Null"
            habitacion.save()
            
            
            #-------------le greguego esto------------------------
            
            for contr in contrato:
                 
                 if contr.habitacion== habitacion:
                      contr.estado= False_variable
                      contr.save()
            return redirect('modificarContrato')
       
       
       

