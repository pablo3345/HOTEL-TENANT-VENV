from django.shortcuts import render, redirect, get_object_or_404
from reservas.forms import FormHuesped_reserva, FormReserva
from contrato.formsHuesped import FormHuesped
from reservas.models import HuespedReserva
from django.contrib import messages
import datetime
from habitacion.models import Habitacion
from contrato.models import Contrato, Huesped
from reservas.models import Reserva
from contrato.formsContrtato import FormContrato
from django.views.generic import View
from django.http import HttpResponse





#-------------------------------------------------

from django.http import HttpResponseRedirect
from django.urls import reverse
       
from django.http import JsonResponse       

import json

# Create your views here.


def mostrar_reserva(request):
     
    
    
    
 
    FormReservas = FormReserva()
     #-------para mostrar el huesped reserva en el formulario reserva----
    ultimoHuesped = HuespedReserva.objects.all()
      
    ultimo = list()
    ultimoHues = list()
     
    for ult in ultimoHuesped:
          if ult.nombre != None:
               ultimo.append(ult)
               ultimoHues= ultimo[-1]
               
    #----------------------------------------------------------
    if request.method =='POST':
         
     formHuesped_reservas =FormHuesped_reserva(request.POST)
         
     if formHuesped_reservas.is_valid():
              
               formHuesped_reservas.save()
               messages.success(request, "El huesped de reserva se guardo correctamente...")
              
     else:
              messages.error(request, "El huesped no se guardo...")
              
     return redirect('mostrar_reservas')
     
    else:
          formHuesped_reservas=FormHuesped_reserva()
          
          #------------agregue esto----------
        
       
        
          
          
     
    
    return render(request, "reservas/reservas.html", {'FormReservas': FormReservas, 'FormHuesped_reservas':formHuesped_reservas, 'ultimoHuesped':ultimoHues})





def guardarReserva(request):
      
     formHuesped_reservas = FormHuesped_reserva()
     formReservas = FormReserva()
     contrato = Contrato()
     
     true_variable = True
     
     reserva=Reserva()
     
     
      #---volver---atras--------------------------------------------------------------------
     
     ultimoHuesped = HuespedReserva.objects.all()
      
     ultimo = list()
     ultimoHues = list()
     
     for ult in ultimoHuesped:
          if ult.nombre != None:
               ultimo.append(ult)
               ultimoHues= ultimo[-1]
               
     
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
          
          
          porcentaje_de_senia= request.POST.get("porcentaje_de_senia")
          
          # -----json eliminar-------------------------------------------
        
          
     #.........................cambiar formato calendario.....................
          fechaConvertida = datetime.datetime.strptime(fecha_entra, '%Y-%m-%dT%H:%M') # strptime lo convierto a objeto datetime, el segundo parametro le dice como interpretar la fecha, cual es la hora, el dia, el mes etc
     
          fechaFormateada = fechaConvertida.strftime('%Y-%m-%dT%H:%M') # strftime para darle el formato que quiero
       
        
          fechaConvertida2 = datetime.datetime.strptime(fecha_sali, '%Y-%m-%dT%H:%M')
          fechaFormateada2 = fechaConvertida2.strftime('%Y-%m-%dT%H:%M') 
          
          #habitacion = Habitacion.objects.get(id= habitacions)
          #huesped = Huesped.objects.get(id=huespeds)
          habitacion = get_object_or_404(Habitacion, id=habitacions)
          huesped = get_object_or_404(HuespedReserva, id=huespeds)
          
          #-------------------------id contrato para ponerle True----------------------
          id_contrato = contrato.id
          
          #--------------------------cuando no tengo huesped----------------------
         
          '''try:
               reserva.huesped = ultimoHues
               
          except:
                messages.error(request, "La reserva no se guardo, puede ser que no haya ingresado el huesped")
                return redirect("mostrar_reservas")'''
          #-----------------------------------------------------------   
          
          #-------fuera del horario----------
          if fechaConvertida2.hour <10 or fechaConvertida2.hour>=18:
                messages.error(request, "El horario no corresponde")
                return redirect('mostrar_reservas')
            #-------------para comparar si la fecha entrada es mayor a la fecha salida-----------
          
          elif fechaConvertida >= fechaConvertida2:
                messages.error(request, "La entrada es mayor o igual a la salida")
                return redirect('mostrar_reservas')
          
          
         
          
        #---------------------------hago esto para cuando los años de entrada y salida no coinciden---
          
        
          
          
          total =calcularTotal(request, fecha_entra, fecha_sali, habitacions, importe_otros_gast)
          
          importeEstadia =contrato.calcularImporteEstadia(fecha_entra, fecha_sali, habitacions, importe_otros_gast)
          
          diferenciaConvertida = contrato.nochesDeEstadia(fecha_entra, fecha_sali, habitacions, importe_otros_gast)
          
        
           #---------------para sacar la promocion de descuento-------------- pr volver------
         # total_estadia_con_descuento_Late =descuento_delTotal_Promocion_menosLate(request, fecha_entra, fecha_sali, habitacions, importe_otros_gast)
          #total_estadia_con_descuento_diez =descuento_delTotal_Promocion_chekOut_diez(request, fecha_entra, fecha_sali, habitacions, importe_otros_gast)
           #para volver atras--------------...........----------------------
          
          if int(descuento_porNoche) != 0 and int(descuento_total_importe) != 0:
               
               messages.error(request, "ingreso porcentajes en opciones no permitidas")
               return redirect("mostrar_reservas")
          
         # elif  int(descuento_porNoche) != 0 and int(aumento_Total) != 0:
             #   messages.error(request, "ingreso porcentajes en varias opciones")
             #   return redirect('Contrato')
         # elif int(descuento_total_importe) != 0 and int(aumento_Total) != 0:
             #  messages.error(request,"ingreso porcentajes en varias opciones")
              # return redirect('Contrato')
          
          elif int(descuento_total_importe) != 0 and int(aumento_Total) != 0 and int(descuento_porNoche) != 0 and int(porcentaje_de_senia) !=0:
                messages.error(request,"ingreso porcentajes en opciones no permitidas")
                return redirect('mostrar_reservas')
          
          
          
              
         
          if int(descuento_porNoche) != 0 and int(aumento_Total) ==0 and int(porcentaje_de_senia) ==0:
               messages.success(request, "agrego descuento al precio de la habitacion por cada noche")
               
          
               
             
             
               if fechaConvertida2.hour==10 and fechaConvertida2.minute==0:
                     total_estadia_con_descuento_diez =descuento_delTotal_Promocion_chekOut_diez(request, fecha_entra, fecha_sali, habitacions, importe_otros_gast)
                     reserva.importe_estadia= total_estadia_con_descuento_diez
                     reserva.total = total_estadia_con_descuento_diez + float(importe_otros_gast)
                     #-------------le agregue esto-------------------
                     reserva.total_senia=0
                    #----------------------------------------------------
                     reserva.fecha_entrada= fechaFormateada
                     reserva.fecha_salida = fechaFormateada2
                     reserva.estado=true_variable
                     reserva.porcentaje_de_senia=0
                     reserva.descuento_importe_noche=descuento_porNoche
                     reserva.descuento_total_calcularo=descuento_total_importe
                     reserva.aumento_total= aumento_Total
                     
                     reserva.habitacion=habitacion
                     
                     reserva.importe_otros_gasto= importe_otros_gast
                     
                     reserva.huesped=huesped
                   
                   
                     
                     reserva.save()
                     return redirect("ModificarReservas")
                    
                    
               else:
                    if fechaConvertida2.hour >=10 and fechaConvertida2.hour <18:
                          total_estadia_con_descuento_Late =descuento_delTotal_Promocion_menosLate(request, fecha_entra, fecha_sali, habitacions, importe_otros_gast)
                          reserva.importe_estadia= total_estadia_con_descuento_Late
                          reserva.total= total_estadia_con_descuento_Late + float(importe_otros_gast)
                          #------le agregue esto-----------------------
                          reserva.total_senia=0
                          
                          reserva.fecha_entrada= fechaFormateada
                          reserva.fecha_salida = fechaFormateada2
                          reserva.estado=true_variable
                          reserva.porcentaje_de_senia=0
                          reserva.descuento_importe_noche=descuento_porNoche
                          reserva.descuento_total_calcularo=descuento_total_importe
                          reserva.aumento_total= aumento_Total
                          
                          reserva.importe_otros_gasto= importe_otros_gast
                          
                          
                          reserva.habitacion=habitacion
                          reserva.huesped=huesped
                          
                          
                          reserva.save()
                          return redirect("ModificarReservas")
                        
                         
                    
                    
          
                     
                     
        
                  
          elif int(aumento_Total) != 0 and  int(descuento_porNoche) == 0 and int(descuento_total_importe)== 0 and int(porcentaje_de_senia) ==0:# esto lo agregue a lo ultimo de la noche
                 reserva.habitacion =habitacion 
          
                 reserva.huesped = huesped
                 reserva.fecha_entrada= fechaFormateada
                 reserva.fecha_salida = fechaFormateada2
                 reserva.estado=true_variable
                 reserva.porcentaje_de_senia=0
                 reserva.total_senia=0
          
          #-------------------agregue los descuentos ---------------------
          
                 reserva.descuento_importe_noche=descuento_porNoche
                 reserva.descuento_total_calcularo=descuento_total_importe
                 reserva.aumento_total= aumento_Total
                 #-------------------------------------------------------
                 reserva.importe_estadia= importeEstadia
                 
                 reserva.importe_otros_gasto= importe_otros_gast
                
                 aumento_total = total* float(aumento_Total) /100
                 aumento_total2 = aumento_total
                 reserva.total= total + aumento_total2
                 #--------------------le agrego esto-------------------------
                 reserva.save()
             
                 messages.success(request, "agrego un aumento al total del importe")
                 return redirect("ModificarReservas")
             #-----para volver atras..............................
          
          
          elif  int(descuento_total_importe) !=0  and int(aumento_Total) ==0 and int(porcentaje_de_senia)==0: # esto lo agregue ahor para volver atras-----
                 reserva.importe_estadia= importeEstadia
                
                 descuentoTotal = total* float(descuento_total_importe) /100
                 descuentoTotal2 = descuentoTotal
                  
               
                 reserva.total= total - descuentoTotal2
                 
                 
                 
                 #----------------------------------------------
                 
                 reserva.habitacion =habitacion 
          
                 reserva.huesped = huesped
                 
                 
                 reserva.fecha_entrada= fechaFormateada
                 reserva.fecha_salida = fechaFormateada2
                 reserva.estado= true_variable
                 reserva.porcentaje_de_senia =0
                 reserva.total_senia=0
                 reserva.descuento_importe_noche=descuento_porNoche
                 reserva.descuento_total_calcularo=descuento_total_importe
                 reserva.aumento_total= aumento_Total
                 
                 reserva.importe_otros_gasto= importe_otros_gast
                 
                 reserva.save()
                 
               
               
                 messages.success(request, "agrego descuento al total")
                 return redirect("ModificarReservas")
                 
         #---------------------------APRETANDO DOS OPCIONES------------------------------- 
         
          elif int(descuento_porNoche) != 0 and int(aumento_Total) != 0 and int(porcentaje_de_senia)==0:
               reserva.habitacion =habitacion 
          
               reserva.huesped = huesped
               reserva.fecha_entrada= fechaFormateada
               reserva.fecha_salida = fechaFormateada2
          
          #-------------------agregue los descuentos ---------------------
          
               reserva.descuento_importe_noche=descuento_porNoche
               reserva.descuento_total_calcularo=descuento_total_importe
               reserva.aumento_total= aumento_Total
          
         #----------------------------------------------------------- 
       
               reserva.importe_otros_gasto = importe_otros_gast
        
               reserva.estado=true_variable
               
               reserva.porcentaje_de_senia=0
       
        
         
               messages.success(request, "aplico un descuento por cada noche y un aumento sobre el total")
             #---------------------------para volver atras-------------------
               if fechaConvertida2.hour==10 and fechaConvertida2.minute==0:
                     total_estadia_con_descuento_diez =descuento_delTotal_Promocion_chekOut_diez(request, fecha_entra, fecha_sali, habitacions, importe_otros_gast)
                     reserva.importe_estadia= total_estadia_con_descuento_diez
                     reserva.total = total_estadia_con_descuento_diez + float(importe_otros_gast)
                     
               #-------------aumento-----------    
                     total= reserva.total
                     total2 = total *float(aumento_Total)/100
                     total3 = total +total2
                     
                     reserva.total = total3
                     
                     reserva.total_senia=0
                      
                     reserva.save()
                     return redirect("ModificarReservas")
                     
                     
                   
                    
               else:
                    if fechaConvertida2.hour >=10 and fechaConvertida2.hour <18:
                          total_estadia_con_descuento_Late =descuento_delTotal_Promocion_menosLate(request, fecha_entra, fecha_sali, habitacions, importe_otros_gast)
                          reserva.importe_estadia= total_estadia_con_descuento_Late
                          reserva.total= total_estadia_con_descuento_Late + float(importe_otros_gast)
                          
                        
                 
          #---------------------aumento-------------------------------
                  
                      
                    total= reserva.total
                    total2 = total *float(aumento_Total)/100
                    total3 = total +total2
                    
       
                     
                    reserva.total = total3
                    
                    reserva.total_senia=0
                      
                    reserva.save()
                    return redirect("ModificarReservas")
                    
                    
          elif  int(descuento_total_importe) !=0  and int(aumento_Total) != 0 and int(porcentaje_de_senia) ==0:
                 reserva.habitacion =habitacion 
          
                 reserva.huesped = huesped
                 reserva.fecha_entrada= fechaFormateada
                 reserva.fecha_salida = fechaFormateada2
          
          #-------------------agregue los descuentos ---------------------
          
                 reserva.descuento_importe_noche=descuento_porNoche
                 reserva.descuento_total_calcularo=descuento_total_importe
                 reserva.aumento_total= aumento_Total
          
         #----------------------------------------------------------- 
       
                 reserva.importe_otros_gasto = importe_otros_gast
        
                 reserva.estado=true_variable
       
                
                 reserva.importe_estadia= importeEstadia
                
                 descuentoTotal = total* float(descuento_total_importe) /100
                 descuentoTotal2 = descuentoTotal
                  
               
                 reserva.total= total - descuentoTotal2
                 
                 #-------le agregue estado y total seña---------------------------
                 reserva.estado= true_variable
                 reserva.total_senia=0
                 #-----------------------------------------------
                 
                 reserva.save()
               
                # messages.success(request, "agrego descuento al total importe")
                 #----------------------------------------
                 
                 total= reserva.importe_estadia
                      
                 #estadia_mas_otros_gastos = float(contrato.importe_estadia)+ float(contrato.importe_otros_gasto)
                 estadia_mas_otros_gastos = float(reserva.importe_estadia)+ float(importe_otros_gast)
                      
                 descuento =estadia_mas_otros_gastos*float(descuento_total_importe)/100
                      
                      
                 tota2 = estadia_mas_otros_gastos- descuento
                      
                 tota2 = tota2 + tota2 *float(aumento_Total)/100
                 
                 reserva.porcentaje_de_senia=0
                          
                     
                      
                 reserva.total = tota2
                 
                 messages.success(request, "agrego descuento al total importe, y luego un aumento al total")
                      
                 reserva.save()
                 return redirect("ModificarReservas")
                   
                     
           #----------------------el total con la seña---------------------------- 
           # ----------------para volver atras.......................... 
           
               
               
          elif  int(porcentaje_de_senia) !=0 and  int(descuento_porNoche) == 0 and int(descuento_total_importe) == 0 and int(aumento_Total)==0:
                
                 reserva.habitacion =habitacion 
          
                 reserva.huesped = huesped
                 reserva.fecha_entrada= fechaFormateada
                 reserva.fecha_salida = fechaFormateada2
          
         
                 reserva.descuento_importe_noche=descuento_porNoche
                 reserva.descuento_total_calcularo=descuento_total_importe
                 reserva.aumento_total= aumento_Total
                 reserva.porcentaje_de_senia= porcentaje_de_senia
          
         #----------------------------------------------------------- 
       
                 reserva.importe_otros_gasto = importe_otros_gast
        
                 reserva.estado=true_variable
       
        
                 reserva.importe_estadia= importeEstadia
                
                 aumento_senia = total* float(porcentaje_de_senia) /100
                 aumento_total2 = aumento_senia
                 reserva.total_senia=  aumento_total2
                 
                 reserva.total= total
                 
                
                 
                 reserva.save()
             
                 messages.success(request, "calculó el porcentaje de la reserva")
                 
                 #return redirect('mostrar_reservas')
                 return redirect("ModificarReservas")
                 
          elif  int(porcentaje_de_senia) !=0 and  int(descuento_porNoche) != 0 and int(descuento_total_importe) == 0  and int(aumento_Total) == 0:
                
                 if fechaConvertida2.hour==10 and fechaConvertida2.minute==0:
                     total_estadia_con_descuento_diez =descuento_delTotal_Promocion_chekOut_diez(request, fecha_entra, fecha_sali, habitacions, importe_otros_gast)
                     reserva.importe_estadia= total_estadia_con_descuento_diez
                     reserva.total = total_estadia_con_descuento_diez + float(importe_otros_gast)
                     
               #-------------aumento-----------    
                     reserva.importe_otros_gasto = float(importe_otros_gast)
        
                     reserva.estado=true_variable
       
        
                    # reserva.importe_estadia= importeEstadia
                
                     aumento_senia = float(reserva.total)* float(porcentaje_de_senia) /100
                     aumento_total2 = aumento_senia
                     reserva.total_senia=  aumento_total2
                 
                    # reserva.total= float(reserva.importe_estadia) +importe_otros_gast
                     
                     reserva.fecha_entrada= fechaFormateada
                     reserva.fecha_salida = fechaFormateada2
                     
                     reserva.descuento_importe_noche=descuento_porNoche
                     reserva.descuento_total_calcularo=descuento_total_importe
                     reserva.aumento_total= aumento_Total
                     
                     reserva.porcentaje_de_senia= porcentaje_de_senia
                     
                     #-------------------agregue esto porque me generaba error en estas opciones-----
                     reserva.habitacion = habitacion
                     
                     reserva.huesped= huesped
                 
                
                 
                     reserva.save()
             
                     messages.success(request, "calculó el porcentaje de la reserva, mas el descuento de habitacion por noche")
                     
                     return redirect("ModificarReservas")
                   
                    
                 else:
                    if fechaConvertida2.hour >=10 and fechaConvertida2.hour <18:
                          total_estadia_con_descuento_Late =descuento_delTotal_Promocion_menosLate(request, fecha_entra, fecha_sali, habitacions, importe_otros_gast)
                          reserva.importe_estadia= total_estadia_con_descuento_Late
                          reserva.total= total_estadia_con_descuento_Late + float(importe_otros_gast)
                          
                        
                 
          #---------------------aumento-------------------------------
                  
                      
                          reserva.importe_otros_gasto = importe_otros_gast
        
                          reserva.estado=true_variable
       
        
                         # reserva.importe_estadia= importeEstadia
                
                          aumento_senia = float(reserva.total) * float(porcentaje_de_senia) /100
                          aumento_total2 = aumento_senia
                          reserva.total_senia=  aumento_total2
                 
                        #  reserva.total= total
                          reserva.fecha_entrada= fechaFormateada
                          reserva.fecha_salida = fechaFormateada2
                          
                          reserva.descuento_importe_noche=descuento_porNoche
                          reserva.descuento_total_calcularo=descuento_total_importe
                          reserva.aumento_total= aumento_Total
                          
                          reserva.porcentaje_de_senia = porcentaje_de_senia
                          
                           #-------------------agregue esto porque me generaba error en estas opciones-----
                          reserva.habitacion = habitacion
                          
                          reserva.huesped= huesped
                 
                
                 
                
                 
                          reserva.save()
             
                          messages.success(request, "calculó el porcentaje de la reserva, mas el descuento de la habitacion por noche")
                          return redirect("ModificarReservas")
               
          elif  int(porcentaje_de_senia) !=0  and int(descuento_total_importe) != 0 and int(aumento_Total)==0:
                
                  reserva.importe_estadia= importeEstadia
                
                  descuentoTotal = total* float(descuento_total_importe) /100
                  descuentoTotal2 = descuentoTotal
                  
               
                  reserva.total= total - descuentoTotal2
                 
               
               
                 # messages.success(request, "agrego descuento al total") ---volver atras----
                   #----------------------seña de reserva---------------------
                  reserva.habitacion =habitacion 
          
                  reserva.huesped = huesped
                  reserva.fecha_entrada= fechaFormateada
                  reserva.fecha_salida = fechaFormateada2
          
         
                  reserva.descuento_importe_noche=descuento_porNoche
                  reserva.descuento_total_calcularo=descuento_total_importe
                  reserva.aumento_total= aumento_Total
                  reserva.porcentaje_de_senia= porcentaje_de_senia
                  #reserva.estado=true_variable
                 # reserva.porcentaje_de_senia=porcentaje_de_senia
                  
                
         #----------------------------------------------------------- 
       
                  reserva.importe_otros_gasto = importe_otros_gast
        
                  reserva.estado=true_variable
       
        
                  reserva.importe_estadia= importeEstadia
                
                  aumento_senia = float(reserva.total)* float(porcentaje_de_senia) /100
                  aumento_total2 = aumento_senia
                  reserva.total_senia=  aumento_total2
                 
                 # reserva.total= total
                 
                
                 
                  reserva.save()
              
                  messages.success(request, "agrego descuento al total importe y calculó el porcentaje de la reserva")
                 
                  return redirect("ModificarReservas")
          
              
             #-------------------------------------------------------------------- 
             
          elif  int(porcentaje_de_senia) !=0  and int(aumento_Total) != 0  and int(descuento_porNoche) == 0 and int(descuento_total_importe)==0:
                 reserva.habitacion =habitacion 
          
                 reserva.huesped = huesped
                 reserva.fecha_entrada= fechaFormateada
                 reserva.fecha_salida = fechaFormateada2
                 reserva.estado=true_variable
                 reserva.porcentaje_de_senia= porcentaje_de_senia
                 #reserva.total_senia=0
          
          #-------------------agregue los descuentos ---------------------
          
                 reserva.descuento_importe_noche=descuento_porNoche
                 reserva.descuento_total_calcularo=descuento_total_importe
                 reserva.aumento_total= aumento_Total
                 #-------------------------------------------------------
                 reserva.importe_estadia= importeEstadia
                
                 aumento_total = total* float(aumento_Total) /100
                 aumento_total2 = aumento_total
                 reserva.total= total + aumento_total2
                 
                 #  ----------------seña----------------------------
                 reserva.importe_otros_gasto = importe_otros_gast
        
                 reserva.estado=true_variable
       
        
                 reserva.importe_estadia= importeEstadia
                
                 aumento_senia = float(reserva.total)* float(porcentaje_de_senia) /100
                 aumento_total2 = aumento_senia
                 reserva.total_senia=  aumento_total2
                 
                 # reserva.total= total
                 
                
                 
                 reserva.save()
                 messages.success(request, "se realizo un aumento al total y se calculó un porcentaje a cobrar por la reserva")
                 return redirect("ModificarReservas")
                
          elif int(porcentaje_de_senia) !=0  and int(aumento_Total) != 0 and int(descuento_porNoche) != 0:
               reserva.habitacion =habitacion 
          
               reserva.huesped = huesped
               reserva.fecha_entrada= fechaFormateada
               reserva.fecha_salida = fechaFormateada2
          
          #-------------------agregue los descuentos ---------------------
          
               reserva.descuento_importe_noche=descuento_porNoche
               reserva.descuento_total_calcularo=descuento_total_importe
               reserva.aumento_total= aumento_Total
          
         #----------------------------------------------------------- 
       
               reserva.importe_otros_gasto = importe_otros_gast
        
               reserva.estado=true_variable
               
               reserva.porcentaje_de_senia= porcentaje_de_senia
       
        
         
               messages.success(request, "aplico un descuento por cada noche y un aumento sobre el total, mas el porcentaje de la reserva")
             #---------------------------para volver atras-------------------
               if fechaConvertida2.hour==10 and fechaConvertida2.minute==0:
                     total_estadia_con_descuento_diez =descuento_delTotal_Promocion_chekOut_diez(request, fecha_entra, fecha_sali, habitacions, importe_otros_gast)
                     reserva.importe_estadia= total_estadia_con_descuento_diez
                     reserva.total = total_estadia_con_descuento_diez + float(importe_otros_gast)
                     
               #-------------aumento-----------    
                     total= reserva.total
                     total2 = total *float(aumento_Total)/100
                     total3 = total +total2
                     
                     reserva.total = total3
                     
                     reserva.total_senia=0
                      
                     reserva.save()
                      #-------------la parte de la seña de la reserva---------------
                    
                     aumento_senia = float(reserva.total) * float(porcentaje_de_senia) /100
                     aumento_total2 = aumento_senia
                     reserva.total_senia=  aumento_total2
                 
                     #reserva.total= total
                 
                
                 
                     reserva.save()
                     return redirect("ModificarReservas")
                     
                     
                   
                    
               else:
                    if fechaConvertida2.hour >=10 and fechaConvertida2.hour <18:
                          total_estadia_con_descuento_Late =descuento_delTotal_Promocion_menosLate(request, fecha_entra, fecha_sali, habitacions, importe_otros_gast)
                          reserva.importe_estadia= total_estadia_con_descuento_Late
                          reserva.total= total_estadia_con_descuento_Late + float(importe_otros_gast)
                          
                        
                 
          #---------------------aumento-------------------------------
                  
                      
                    total= reserva.total
                    total2 = total *float(aumento_Total)/100
                    total3 = total +total2
                    
       
                     
                    reserva.total = total3
                    
                    reserva.total_senia=0
                      
                    reserva.save()
                    
                   # messages.success(request, "tres seleccionados")
                    
                    #-------------la parte de la seña de la reserva---------------
                    
                    aumento_senia = float(reserva.total) * float(porcentaje_de_senia) /100
                    aumento_total2 = aumento_senia
                    reserva.total_senia=  aumento_total2
                 
                   # reserva.total= total
                 
                
                 
                    reserva.save()
                    return redirect("ModificarReservas")
                    
          elif int(porcentaje_de_senia) !=0  and int(aumento_Total) != 0 and int(descuento_total_importe) != 0:
                # messages.success(request, "ultimas tres opciones")
                 reserva.habitacion =habitacion 
          
                 reserva.huesped = huesped
                 reserva.fecha_entrada= fechaFormateada
                 reserva.fecha_salida = fechaFormateada2
          
          #-------------------agregue los descuentos ---------------------
          
                 reserva.descuento_importe_noche=descuento_porNoche
                 reserva.descuento_total_calcularo=descuento_total_importe
                 reserva.aumento_total= aumento_Total
          
         #----------------------------------------------------------- 
       
                 reserva.importe_otros_gasto = importe_otros_gast
        
                 reserva.estado=true_variable
       
                
                 reserva.importe_estadia= importeEstadia
                
                 descuentoTotal = total* float(descuento_total_importe) /100
                 descuentoTotal2 = descuentoTotal
                  
               
                 reserva.total= total - descuentoTotal2
                 
                 #-------le agregue estado y total seña---------------------------
                 reserva.estado= true_variable
                 reserva.total_senia=0
                 #-----------------------------------------------
                 
                 reserva.save()
               
                # messages.success(request, "agrego descuento al total importe")
                 #----------------------------------------
                 
                 total= reserva.importe_estadia
                      
                 #estadia_mas_otros_gastos = float(contrato.importe_estadia)+ float(contrato.importe_otros_gasto)
                 estadia_mas_otros_gastos = float(reserva.importe_estadia)+ float(importe_otros_gast)
                      
                 descuento =estadia_mas_otros_gastos*float(descuento_total_importe)/100
                      
                      
                 tota2 = estadia_mas_otros_gastos- descuento
                      
                 tota2 = tota2 + tota2 *float(aumento_Total)/100
                 
                 reserva.porcentaje_de_senia=porcentaje_de_senia
                          
                     
                      
                 reserva.total = tota2
                 
                 messages.success(request, "agrego descuento al total importe, y luego un aumento al total, mas el porcentaje de la reserva")
                      
                 reserva.save()
                 #-------------------la parte de la seña----------------------------------
                 aumento_senia = float(reserva.total) * float(porcentaje_de_senia) /100
                 aumento_total2 = aumento_senia
                 reserva.total_senia=  aumento_total2
                 
                   # reserva.total= total
                 
                
                 
                 reserva.save()
                 return redirect("ModificarReservas")
                       
                    
                
               
          else:
               
               
               reserva.importe_estadia= importeEstadia
               reserva.total= total
             
               
          
         
              
                         
  
              
     
          
               reserva.habitacion =habitacion # obtuve la habitacion mediante el id---volver atras---
          
               reserva.huesped = huesped
               reserva.fecha_entrada= fechaFormateada
               reserva.fecha_salida = fechaFormateada2
          
          #-------------------agregue los descuentos ---------------------
          
               reserva.descuento_importe_noche=descuento_porNoche
               reserva.descuento_total_calcularo=descuento_total_importe
               reserva.aumento_total= aumento_Total
          
         #----------------------------------------------------------- 
       
               reserva.importe_otros_gasto = importe_otros_gast
        
               reserva.estado=true_variable
          
               reserva.total_senia=0
          
               reserva.porcentaje_de_senia= porcentaje_de_senia
       
        
         
          
               
          
          
         #----para---------volver------atras de try----------------------
               try:
          
           
        
           #ponerTrue_alUltimoContrato(request, habitacions)
          # ponerOcupada_ultimaHabitacion(request, habitacions)
          
                 
          
                 
                  
                   
                  reserva.save()
                  
                 
                  #eliminar_para_que_noSeRepita(request)
                  
                 
                 
                 
                  
                 
          
           
          
         
               
               
           
           
          
        
                  messages.success(request, "La reserva se guardo correctamente...")
                  #return redirect('ModificarReservas')
                  return redirect("ModificarReservas")
      
               
            
           
           
               except:
                 messages.error(request, "La reserva no se guardo...")
                 
               
               
               
        
             
                    
      
             
          
     else:
         form2 = FormReserva()
         
    
     
     
     
     return render(request, "reservas/reservas.html", {'FormReservas': formReservas, 'FormHuesped_reservas':formHuesped_reservas, 'total': total, 'importe_de_otros_gastos':importe_otros_gast, 'importe_estadia':importeEstadia, 'diferenciaConvertida':diferenciaConvertida, 'descuento':descuento_porNoche, 'descuento_total': descuento_total_importe, 'aumento':aumento_Total, 'ultimo':ultimoHues})
     
     

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
        
         
     
          importeEstadia =contrato.calcularImporteEstadia(fecha_entra, fecha_sali, habitacions, importe_otros_gast)
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
          
        

     
          importeEstadia =contrato.calcularImporteEstadia(fecha_entra, fecha_sali, habitacions, importe_otros_gast)
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

          
def calcularTotal(request, fecha_entra, fecha_sali, habitacions, importe_otros_gasto):
          contrato = Contrato()
          #total =0
         
     
     
         
          total = contrato.calcularFechas(fecha_entra, fecha_sali, habitacions, importe_otros_gasto)
          
    
     
          return total
    
    
def modificarReservas(request):
      
      reservas = Reserva.objects.all()
      
     
      
      poner_False_despues_despuesDelPlazo_reservas(request)
      
      reservas_true = list()
      
      for reser in reservas:
          if reser.estado== True:
               reservas_true.append(reser)
      
      
      
      return render(request, "reservas/modificarReservas.html", {'reservas': reservas_true})




def enviar_a_contrato(request, id_reserva):
     
     
      
      form1 = FormContrato()
      form2 = FormHuesped()
   #----------------------------huesped----------------volver atras------------------------------   
      huesped=Huesped()
      contrato=Contrato()
      
      reserva =  get_object_or_404(Reserva, id=id_reserva)
      
      id_huesped = reserva.huesped.id
      
      huesped_reserva =  get_object_or_404(HuespedReserva, id=id_huesped)
      
     
      
      #-------------------------------------------------------------------------------------
      #id_reservas= id_huesped
      
      id_reservas = reserva.id
      
      
      
      
      
      habitacion = reserva.habitacion
      
   
      
      
      
      
   
      
      
      
      nombre_responsa = huesped_reserva.nombre
      apellido=huesped_reserva.apellido
        
    
        
    
          
      huesped.nombre_responsable= huesped_reserva.nombre
      huesped.apellido= huesped_reserva.apellido
      huesped.dni = huesped_reserva.dni
      huesped.telefono = huesped_reserva.telefono
      
  #----------------------contrato-----------------------------------------------
      contrato.habitacion= reserva.habitacion
      #contrato.fecha_entrada= str(reserva.fecha_entrada)
      #contrato.fecha_salida= str(reserva.fecha_salida)
      contrato.fecha_entrada= str(reserva.fecha_entrada)
      contrato.fecha_salida= str(reserva.fecha_salida)
      contrato.importe_otros_gasto= reserva.importe_otros_gasto
      contrato.descuento_importe_noche= reserva.descuento_importe_noche
      contrato.descuento_total_calcularo= reserva.descuento_total_calcularo
      contrato.aumento_total = reserva.aumento_total
      
      porcentaje_senia = reserva.porcentaje_de_senia
      #---------------------------------descontar la reserva--------------------------------------
      
     # contrato.total = reserva.total_senia
      
      
      #---------------------------------------------------------------------------------------
      
      data={'fecha_entrada': contrato.fecha_entrada, 'fecha_salida': contrato.fecha_salida, 'otros_gastos': contrato.importe_otros_gasto,
            'descuento_por_noche': contrato.descuento_importe_noche, 'descuento_al_total': contrato.descuento_total_calcularo,
            'aumento_total': contrato.aumento_total, 'habitacion':habitacion}
      
   
      
     # guardarHuesped(request)
     # mostrarContrato(request, id=id_reserva)
    
      
    
     
            
     
      
     
      #recibir_id_reserva(request, id_reserva)
     
     # form2 = FormHuesped(instance=huesped)
     
      
     # form1= FormContrato(instance=contrato)
      
      #recibir_id_reserva(request, id_reserva)
      
     
      
      
      
     
     
     
    
      
      
    
     
     
      return HttpResponseRedirect(reverse("huesped_Reserva", args=[id_reservas]))
       
       
     
     
      #mostrarContrato(request, id_reserva)
      
     
      
     
      #recibir_id_reserva(request, id_reservas)
     # mostrarContrato_reservas(request, id_reservas)
     
     
           
      
    
     
     
   
      
    #  return render(request, "contrato/contrato.html", {'formHuesped': form2, 'formContrato': form1, 'porcentaje_senia': porcentaje_senia, 'data': data, 'huesped_reserva':huesped_reserva})
      
      
     

           
           
            
      
 
    
     
          
      
      
      
     
      
   
      
      
      
      
def guardarHuesped(request):
      
   
    
     form1 = FormContrato()
     form2 = FormHuesped()
      
     huesped = Huesped()
     contrato = Contrato()
     
     
     print("lleca hasta guardar huesped")
     
    
      
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
     if request.method =='POST':
          
          huesped.nombre_responsable= nombre_resp
          huesped.apellido = apelli
          huesped.edad = edadd
          huesped.dni = dnii
          huesped.demas_huespedes = demas_huespe
          huesped.patente_vehiculo= patente_vehicu
          huesped.modelo_vehiculo= modelo_vehicu
          huesped.correo_electronico= correo_electro
          #---------------------------------------
          huesped.direccion= direccion
          huesped.localidad= localidad
          huesped.codigo_postal= codigo_postal
          huesped.pais=pais
          huesped.telefono= telefono
          
        
          
          
         
          
          
         
 
          
        
          
         
          
         
          try:
                
           huesped.save()
           messages.success(request, "El huesped se guardo correctamente...")
           
          except:
                 messages.error(request, "El huesped no se guardo...")
                 
        
                 
         
                 
    # return render(request, "reservas/contratoReservas.html", {'formHuesped': form2, 'formContrato': form1, 'huesped': huesped})
      
                 
         # return redirect('guardarReserva')
                 
    
def modificarHuesped(request):
      
      huespedReserva = HuespedReserva.objects.all()
      
      return render(request, "reservas/modificar_huespedReserva.html", {'huespedReserva': huespedReserva})
      
      
      
      
def modificarTabla_huesped(request, id_huesped):
      huespedReserva = get_object_or_404(HuespedReserva, id=id_huesped)
      
      if request.method =="POST":
            
            nombre = request.POST.get("nombre")
            apellido = request.POST.get("apellido")
            dni = request.POST.get("dni")
            telefono = request.POST.get("telefono")
            
            
            huespedReserva.nombre= nombre
            huespedReserva.apellido= apellido
            huespedReserva.dni=dni
            huespedReserva.telefono= telefono
            
            try:
                  
                  huespedReserva.save()
                  messages.success(request, "El huesped de reserva se actualizo correctamente...")
                  
            except:
                   messages.error(request, "El huesped de reserva no se actualizo...")
            return redirect('modificarHuespedReserva')
                   
                   
      huespedReser = FormHuesped_reserva(instance=huespedReserva)
      
      
      return render(request, "reservas/modificar_TablaHuesped.html", {"huespedReser": huespedReser})
      
            
def eliminarHuesped_reserva(request, id_huesped):
      
      #huespedReserva = get_object_or_404(HuespedReserva, id=id_huesped)
      #-----------volver atras--------------------------
      huespedReserva = get_object_or_404(HuespedReserva, id=id_huesped)
      
      try:
           # if HuespedReserva.objects.filter(id=id_huesped).exists(): 
             # huespedReserva = get_object_or_404(HuespedReserva, id=id_huesped)
              huespedReserva.delete()
              messages.success(request, "El huesped de reserva se elimino correctamente...")
            
      except:
             messages.error(request, "El huesped de reserva no se elimino...")
             
      return redirect('modificarHuespedReserva')
      
          
             
          
#-----------------------------------aca voy a poner todo lo que traje de contrato---------------------------  



          
          
        
          
          
def eliminarReserva(request, id_reserva):
     # reserva = get_object_or_404(Reserva, id=id_reserva)
      #----------volver---atras----------------------------------
      reserva = get_object_or_404(Reserva, id=id_reserva)
      
      try: 
            #if Reserva.objects.filter(id=id_reserva).exists():
           
             reserva.delete()
             messages.success(request, "La reserva se elimino correctamente...")
            
      except:
             messages.error(request, "La reserva no se elimino...")
             
      return redirect('ModificarReservas')
      
      
      
def modificarTabla_reserva(request, id_reserva):
     formHuesped_reservas = FormHuesped_reserva()
     formReserva = FormReserva()
     contrato = Contrato()
     
     true_variable = True
     
     #reserva=Reserva()
     reserva = get_object_or_404(Reserva, id=id_reserva)
     
     
      #-----volver atras-------
     
     ultimoHuesped = HuespedReserva.objects.all()
      
     ultimo = list()
     ultimoHues = list()
     
     for ult in ultimoHuesped:
          if ult.nombre != None:
               ultimo.append(ult)
               ultimoHues= ultimo[-1]
               
     
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
          
          
          porcentaje_de_senia= request.POST.get("porcentaje_de_senia")
          
          
          
          # -----json eliminar-------------------------------------------
        
          
     #.........................cambiar formato calendario.....................
          fechaConvertida = datetime.datetime.strptime(fecha_entra, '%Y-%m-%dT%H:%M') # strptime lo convierto a objeto datetime, el segundo parametro le dice como interpretar la fecha, cual es la hora, el dia, el mes etc
     
          fechaFormateada = fechaConvertida.strftime('%Y-%m-%dT%H:%M') # strftime para darle el formato que quiero
       
        
          fechaConvertida2 = datetime.datetime.strptime(fecha_sali, '%Y-%m-%dT%H:%M')
          fechaFormateada2 = fechaConvertida2.strftime('%Y-%m-%dT%H:%M') 
          
          #habitacion = Habitacion.objects.get(id= habitacions)
          #huesped = Huesped.objects.get(id=huespeds)
          habitacion = get_object_or_404(Habitacion, id=habitacions)
          huesped = get_object_or_404(HuespedReserva, id=huespeds)
          
          #-------------------------id contrato para ponerle True----------------------
          id_contrato = contrato.id
          
          #--------------------------cuando no tengo huesped----------------------
          try:
               reserva.huesped = ultimoHues
               
          except:
                messages.error(request, "La reserva no se guardo, puede ser que no haya ingresado el huesped")
                return redirect("mostrar_reservas")
          #-----------------------------------------------------------   
          
          #-------fuera del horario----------
          if fechaConvertida2.hour <10 or fechaConvertida2.hour>=18:
                messages.error(request, "El horario no corresponde")
                return redirect('mostrar_reservas')
            #-------------para comparar si la fecha entrada es mayor a la fecha salida-----------
          
          elif fechaConvertida >= fechaConvertida2:
                messages.error(request, "La entrada es mayor o igual a la salida")
                return redirect('mostrar_reservas')
          
        #---------------------------hago esto para cuando los años de entrada y salida no coinciden---
          
        
          
          
          total =calcularTotal(request, fecha_entra, fecha_sali, habitacions, importe_otros_gast)
          
          importeEstadia =contrato.calcularImporteEstadia(fecha_entra, fecha_sali, habitacions, importe_otros_gast)
          
          diferenciaConvertida = contrato.nochesDeEstadia(fecha_entra, fecha_sali, habitacions, importe_otros_gast)
          
        
           #---------------para sacar la promocion de descuento-------------- pr volver------
         # total_estadia_con_descuento_Late =descuento_delTotal_Promocion_menosLate(request, fecha_entra, fecha_sali, habitacions, importe_otros_gast)
          #total_estadia_con_descuento_diez =descuento_delTotal_Promocion_chekOut_diez(request, fecha_entra, fecha_sali, habitacions, importe_otros_gast)
           #para volver atras--------------...........----------------------
          
          if int(descuento_porNoche) != 0 and int(descuento_total_importe) != 0:
               
               messages.error(request, "ingreso porcentajes en opciones no permitidas")
               return redirect('mostrar_reservas')
          
         # elif  int(descuento_porNoche) != 0 and int(aumento_Total) != 0:
             #   messages.error(request, "ingreso porcentajes en varias opciones")
             #   return redirect('Contrato')
         # elif int(descuento_total_importe) != 0 and int(aumento_Total) != 0:
             #  messages.error(request,"ingreso porcentajes en varias opciones")
              # return redirect('Contrato')
          
          elif int(descuento_total_importe) != 0 and int(aumento_Total) != 0 and int(descuento_porNoche) != 0 and int(porcentaje_de_senia) !=0:
                messages.error(request,"ingreso porcentajes en opciones no permitidas")
                return redirect('mostrar_reservas')
          
          
          
              
         
          if int(descuento_porNoche) != 0 and int(aumento_Total) ==0 and int(porcentaje_de_senia) ==0:
               messages.success(request, "agrego descuento al precio de la habitacion por cada noche")
               
          
               
             
             
               if fechaConvertida2.hour==10 and fechaConvertida2.minute==0:
                     total_estadia_con_descuento_diez =descuento_delTotal_Promocion_chekOut_diez(request, fecha_entra, fecha_sali, habitacions, importe_otros_gast)
                     reserva.importe_estadia= total_estadia_con_descuento_diez
                     reserva.total = total_estadia_con_descuento_diez + float(importe_otros_gast)
                     #-------------le agregue esto-------------------
                     reserva.total_senia=0
                    #----------------------------------------------------
                     reserva.fecha_entrada= fechaFormateada
                     reserva.fecha_salida = fechaFormateada2
                     reserva.estado=true_variable
                     reserva.porcentaje_de_senia=0
                     reserva.descuento_importe_noche=descuento_porNoche
                     reserva.descuento_total_calcularo=descuento_total_importe
                     reserva.aumento_total= aumento_Total
                     
                     #--------------------------------------
                     reserva.importe_otros_gasto=importe_otros_gast
                     reserva.huesped= huesped
                     
                     reserva.habitacion = habitacion
                   
                     
                     reserva.save()
                     return redirect('ModificarReservas')
                     
                  
                    
                    
               else:
                    if fechaConvertida2.hour >=10 and fechaConvertida2.hour <18:
                          total_estadia_con_descuento_Late =descuento_delTotal_Promocion_menosLate(request, fecha_entra, fecha_sali, habitacions, importe_otros_gast)
                          reserva.importe_estadia= total_estadia_con_descuento_Late
                          reserva.total= total_estadia_con_descuento_Late + float(importe_otros_gast)
                          #------le agregue esto-----------------------
                          reserva.total_senia=0
                          
                          reserva.fecha_entrada= fechaFormateada
                          reserva.fecha_salida = fechaFormateada2
                          reserva.estado=true_variable
                          reserva.porcentaje_de_senia=0
                          reserva.descuento_importe_noche=descuento_porNoche
                          reserva.descuento_total_calcularo=descuento_total_importe
                          reserva.aumento_total= aumento_Total
                          
                          
                           #--------------------------------------
                          reserva.importe_otros_gasto=importe_otros_gast
                          reserva.huesped= huesped
                          
                          reserva.habitacion = habitacion
                          
                   
                          
                          
                          reserva.save()
                          return redirect('ModificarReservas')
                        
                         
                    
                    
          
                     
                     
        
                  
          elif int(aumento_Total) != 0 and  int(descuento_porNoche) == 0 and int(descuento_total_importe)== 0 and int(porcentaje_de_senia) ==0:# esto lo agregue a lo ultimo de la noche
                 reserva.habitacion =habitacion 
          
                 reserva.huesped = huesped
                 reserva.fecha_entrada= fechaFormateada
                 reserva.fecha_salida = fechaFormateada2
                 reserva.estado=true_variable
                 reserva.porcentaje_de_senia=0
                 reserva.total_senia=0
          
          #-------------------agregue los descuentos ---------------------
          
                 reserva.descuento_importe_noche=descuento_porNoche
                 reserva.descuento_total_calcularo=descuento_total_importe
                 reserva.aumento_total= aumento_Total
                 #-------------------------------------------------------
                 reserva.importe_estadia= importeEstadia
                 
                 reserva.importe_otros_gasto=importe_otros_gast
                
                 aumento_total = total* float(aumento_Total) /100
                 aumento_total2 = aumento_total
                 reserva.total= total + aumento_total2
                 #--------------------le agrego esto-------------------------
                 reserva.save()
                
             
                 messages.success(request, "agrego un aumento al total del importe")
                 return redirect('ModificarReservas')
             #-----para volver atras..............................
          
          
          elif  int(descuento_total_importe) !=0  and int(aumento_Total) ==0 and int(porcentaje_de_senia)==0: # esto lo agregue ahor para volver atras-----
                 reserva.importe_estadia= importeEstadia
                
                 descuentoTotal = total* float(descuento_total_importe) /100
                 descuentoTotal2 = descuentoTotal
                  
               
                 reserva.total= total - descuentoTotal2
                 
                 #----------------------------------------------
                 
                 reserva.habitacion =habitacion 
          
                 reserva.huesped = huesped
                 
                 
                 reserva.fecha_entrada= fechaFormateada
                 reserva.fecha_salida = fechaFormateada2
                 reserva.estado= true_variable
                 reserva.porcentaje_de_senia =0
                 reserva.total_senia=0
                 reserva.descuento_importe_noche=descuento_porNoche
                 reserva.descuento_total_calcularo=descuento_total_importe
                 reserva.aumento_total= aumento_Total
                 
                  #--------------------------------------
                 reserva.importe_otros_gasto=importe_otros_gast
                   
                   
                 reserva.save()
                 
               
               
                 messages.success(request, "agrego descuento al total")
                 return redirect('ModificarReservas')
                 
         #---------------------------APRETANDO DOS OPCIONES------------------------------- 
         
          elif int(descuento_porNoche) != 0 and int(aumento_Total) != 0 and int(porcentaje_de_senia)==0:
               reserva.habitacion =habitacion 
          
               reserva.huesped = huesped
               reserva.fecha_entrada= fechaFormateada
               reserva.fecha_salida = fechaFormateada2
          
          #-------------------agregue los descuentos ---------------------
          
               reserva.descuento_importe_noche=descuento_porNoche
               reserva.descuento_total_calcularo=descuento_total_importe
               reserva.aumento_total= aumento_Total
          
         #----------------------------------------------------------- 
       
               reserva.importe_otros_gasto = importe_otros_gast
        
               reserva.estado=true_variable
               
               reserva.porcentaje_de_senia=0
       
        
         
               messages.success(request, "aplico un descuento por cada noche y un aumento sobre el total")
               reserva.save()
              
             #---------------------------para volver atras-------------------
               if fechaConvertida2.hour==10 and fechaConvertida2.minute==0:
                     total_estadia_con_descuento_diez =descuento_delTotal_Promocion_chekOut_diez(request, fecha_entra, fecha_sali, habitacions, importe_otros_gast)
                     reserva.importe_estadia= total_estadia_con_descuento_diez
                     reserva.total = total_estadia_con_descuento_diez + float(importe_otros_gast)
                     
               #-------------aumento-----------    
                     total= reserva.total
                     total2 = total *float(aumento_Total)/100
                     total3 = total +total2
                     
                     reserva.total = total3
                     
                     reserva.total_senia=0
                      
                     reserva.save()
                   
                   
                     
                   
                    
               else:
                    if fechaConvertida2.hour >=10 and fechaConvertida2.hour <18:
                          total_estadia_con_descuento_Late =descuento_delTotal_Promocion_menosLate(request, fecha_entra, fecha_sali, habitacions, importe_otros_gast)
                          reserva.importe_estadia= total_estadia_con_descuento_Late
                          reserva.total= total_estadia_con_descuento_Late + float(importe_otros_gast)
                          
                        
                 
          #---------------------aumento-------------------------------
                  
                      
                    total= reserva.total
                    total2 = total *float(aumento_Total)/100
                    total3 = total +total2
                    
       
                     
                    reserva.total = total3
                    
                    reserva.total_senia=0
                      
                    reserva.save()
               return redirect('ModificarReservas')
                    
                    
                    
          elif  int(descuento_total_importe) !=0  and int(aumento_Total) != 0 and int(porcentaje_de_senia) ==0:
                 reserva.habitacion =habitacion 
          
                 reserva.huesped = huesped
                 reserva.fecha_entrada= fechaFormateada
                 reserva.fecha_salida = fechaFormateada2
          
          #-------------------agregue los descuentos ---------------------
          
                 reserva.descuento_importe_noche=descuento_porNoche
                 reserva.descuento_total_calcularo=descuento_total_importe
                 reserva.aumento_total= aumento_Total
          
         #----------------------------------------------------------- 
       
                 reserva.importe_otros_gasto = importe_otros_gast
        
                 reserva.estado=true_variable
       
                
                 reserva.importe_estadia= importeEstadia
                
                 descuentoTotal = total* float(descuento_total_importe) /100
                 descuentoTotal2 = descuentoTotal
                  
               
                 reserva.total= total - descuentoTotal2
                 
                 #-------le agregue estado y total seña---------------------------
                 reserva.estado= true_variable
                 reserva.total_senia=0
                 #-----------------------------------------------
                 
                 reserva.save()
               
                # messages.success(request, "agrego descuento al total importe")
                 #----------------------------------------
                 
                 total= reserva.importe_estadia
                      
                 #estadia_mas_otros_gastos = float(contrato.importe_estadia)+ float(contrato.importe_otros_gasto)
                 estadia_mas_otros_gastos = float(reserva.importe_estadia)+ float(importe_otros_gast)
                      
                 descuento =estadia_mas_otros_gastos*float(descuento_total_importe)/100
                      
                      
                 tota2 = estadia_mas_otros_gastos- descuento
                      
                 tota2 = tota2 + tota2 *float(aumento_Total)/100
                 
                 reserva.porcentaje_de_senia=0
                          
                     
                      
                 reserva.total = tota2
                 
                 messages.success(request, "agrego descuento al total importe, y luego un aumento al total")
                      
                 reserva.save()
                 return redirect('ModificarReservas')
                   
                     
           #----------------------el total con la seña---------------------------- 
         
           
               
               
          elif  int(porcentaje_de_senia) !=0 and  int(descuento_porNoche) == 0 and int(descuento_total_importe) == 0 and int(aumento_Total)==0:
                
                 reserva.habitacion =habitacion 
          
                 reserva.huesped = huesped
                 reserva.fecha_entrada= fechaFormateada
                 reserva.fecha_salida = fechaFormateada2
          
         
                 reserva.descuento_importe_noche=descuento_porNoche
                 reserva.descuento_total_calcularo=descuento_total_importe
                 reserva.aumento_total= aumento_Total
                 reserva.porcentaje_de_senia= porcentaje_de_senia
          
         #----------------------------------------------------------- 
       
                 reserva.importe_otros_gasto = importe_otros_gast
        
                 reserva.estado=true_variable
       
        
                 reserva.importe_estadia= importeEstadia
                
                 aumento_senia = total* float(porcentaje_de_senia) /100
                 aumento_total2 = aumento_senia
                 reserva.total_senia=  aumento_total2
                 
                 reserva.total= total
                 
                
                 
                 reserva.save()
             
                 messages.success(request, "calculó el porcentaje de la reserva")
                 
                 return redirect('ModificarReservas')
                 
          elif  int(porcentaje_de_senia) !=0 and  int(descuento_porNoche) != 0 and int(descuento_total_importe) == 0  and int(aumento_Total) == 0:
                
                 if fechaConvertida2.hour==10 and fechaConvertida2.minute==0:
                     total_estadia_con_descuento_diez =descuento_delTotal_Promocion_chekOut_diez(request, fecha_entra, fecha_sali, habitacions, importe_otros_gast)
                     reserva.importe_estadia= total_estadia_con_descuento_diez
                     reserva.total = total_estadia_con_descuento_diez + float(importe_otros_gast)
                     
               #-------------aumento-----------    
                     reserva.importe_otros_gasto = float(importe_otros_gast)
        
                     reserva.estado=true_variable
       
        
                    # reserva.importe_estadia= importeEstadia
                
                     aumento_senia = float(reserva.total)* float(porcentaje_de_senia) /100
                     aumento_total2 = aumento_senia
                     reserva.total_senia=  aumento_total2
                 
                    # reserva.total= float(reserva.importe_estadia) +importe_otros_gast
                     
                     reserva.fecha_entrada= fechaFormateada
                     reserva.fecha_salida = fechaFormateada2
                     
                     reserva.descuento_importe_noche=descuento_porNoche
                     reserva.descuento_total_calcularo=descuento_total_importe
                     reserva.aumento_total= aumento_Total
                     
                     reserva.porcentaje_de_senia= porcentaje_de_senia
                     #-------le agrego la habitacion xq en guardar reserva me generaba error sin la habitacion----
                     reserva.habitacion=habitacion
                     
                     reserva.huesped=huesped
                 
                
                 
                     reserva.save()
             
                     messages.success(request, "calculó el porcentaje de la reserva, mas el descuento de habitacion por noche")
                     
                     return redirect('ModificarReservas')
                   
                    
                 else:
                    if fechaConvertida2.hour >=10 and fechaConvertida2.hour <18:
                          total_estadia_con_descuento_Late =descuento_delTotal_Promocion_menosLate(request, fecha_entra, fecha_sali, habitacions, importe_otros_gast)
                          reserva.importe_estadia= total_estadia_con_descuento_Late
                          reserva.total= total_estadia_con_descuento_Late + float(importe_otros_gast)
                          
                      
                 
          #---------------------aumento-------------------------------
                  
                      
                          reserva.importe_otros_gasto = importe_otros_gast
        
                          reserva.estado=true_variable
       
        
                         # reserva.importe_estadia= importeEstadia
                
                          aumento_senia = float(reserva.total) * float(porcentaje_de_senia) /100
                          aumento_total2 = aumento_senia
                          reserva.total_senia=  aumento_total2
                 
                        #  reserva.total= total
                          reserva.fecha_entrada= fechaFormateada
                          reserva.fecha_salida = fechaFormateada2
                          
                          reserva.descuento_importe_noche=descuento_porNoche
                          reserva.descuento_total_calcularo=descuento_total_importe
                          reserva.aumento_total= aumento_Total
                          
                          reserva.porcentaje_de_senia = porcentaje_de_senia
                          
                          
                          #-------------------------------------------
                          reserva.habitacion=habitacion
                          
                          reserva.huesped=huesped
                 
                
                 
                          reserva.save()
             
                          messages.success(request, "calculó el porcentaje de la reserva, mas el descuento de la habitacion por noche")
                          return redirect('ModificarReservas')
               
          elif  int(porcentaje_de_senia) !=0  and int(descuento_total_importe) != 0 and int(aumento_Total)==0:
                
                  reserva.importe_estadia= importeEstadia
                
                  descuentoTotal = total* float(descuento_total_importe) /100
                  descuentoTotal2 = descuentoTotal
                  
               
                  reserva.total= total - descuentoTotal2
                 
               
               
                 # messages.success(request, "agrego descuento al total") ---volver atras----
                   #----------------------seña de reserva---------------------
                  reserva.habitacion =habitacion 
          
                  reserva.huesped = huesped
                  reserva.fecha_entrada= fechaFormateada
                  reserva.fecha_salida = fechaFormateada2
          
         
                  reserva.descuento_importe_noche=descuento_porNoche
                  reserva.descuento_total_calcularo=descuento_total_importe
                  reserva.aumento_total= aumento_Total
                  reserva.porcentaje_de_senia= porcentaje_de_senia
                  #reserva.estado=true_variable
                 # reserva.porcentaje_de_senia=porcentaje_de_senia
                  
                
         #----------------------------------------------------------- 
       
                  reserva.importe_otros_gasto = importe_otros_gast
        
                  reserva.estado=true_variable
       
        
                  reserva.importe_estadia= importeEstadia
                
                  aumento_senia = float(reserva.total)* float(porcentaje_de_senia) /100
                  aumento_total2 = aumento_senia
                  reserva.total_senia=  aumento_total2
                 
                 # reserva.total= total
                 
                
                 
                  reserva.save()
              
                  messages.success(request, "agrego descuento al total importe y calculó el porcentaje de la reserva")
                  
                  return redirect('ModificarReservas')
          
              
             #-------------------------------------------------------------------- 
             
          elif  int(porcentaje_de_senia) !=0  and int(aumento_Total) != 0  and int(descuento_porNoche) == 0 and int(descuento_total_importe)==0:
                 reserva.habitacion =habitacion 
          
                 reserva.huesped = huesped
                 reserva.fecha_entrada= fechaFormateada
                 reserva.fecha_salida = fechaFormateada2
                 reserva.estado=true_variable
                 reserva.porcentaje_de_senia= porcentaje_de_senia
                 #reserva.total_senia=0
          
          #-------------------agregue los descuentos ---------------------
          
                 reserva.descuento_importe_noche=descuento_porNoche
                 reserva.descuento_total_calcularo=descuento_total_importe
                 reserva.aumento_total= aumento_Total
                 #-------------------------------------------------------
                 reserva.importe_estadia= importeEstadia
                
                 aumento_total = total* float(aumento_Total) /100
                 aumento_total2 = aumento_total
                 reserva.total= total + aumento_total2
                 
                 #  ----------------seña----------------------------
                 reserva.importe_otros_gasto = importe_otros_gast
        
                 reserva.estado=true_variable
       
        
                 reserva.importe_estadia= importeEstadia
                
                 aumento_senia = float(reserva.total)* float(porcentaje_de_senia) /100
                 aumento_total2 = aumento_senia
                 reserva.total_senia=  aumento_total2
                 
                 # reserva.total= total
                 
                
                 
                 reserva.save()
                 messages.success(request, "se realizo un aumento al total y se calculó un porcentaje a cobrar por la reserva")
                 return redirect('ModificarReservas')
                
          elif int(porcentaje_de_senia) !=0  and int(aumento_Total) != 0 and int(descuento_porNoche) != 0:
               reserva.habitacion =habitacion 
          
               reserva.huesped = huesped
               reserva.fecha_entrada= fechaFormateada
               reserva.fecha_salida = fechaFormateada2
          
          #-------------------agregue los descuentos ---------------------
          
               reserva.descuento_importe_noche=descuento_porNoche
               reserva.descuento_total_calcularo=descuento_total_importe
               reserva.aumento_total= aumento_Total
          
         #----------------------------------------------------------- 
       
               reserva.importe_otros_gasto = importe_otros_gast
        
               reserva.estado=true_variable
               
               reserva.porcentaje_de_senia= porcentaje_de_senia
       
        
         
               messages.success(request, "aplico un descuento por cada noche y un aumento sobre el total, mas el porcentaje de la reserva")
             #---------------------------para volver atras-------------------
               if fechaConvertida2.hour==10 and fechaConvertida2.minute==0:
                     total_estadia_con_descuento_diez =descuento_delTotal_Promocion_chekOut_diez(request, fecha_entra, fecha_sali, habitacions, importe_otros_gast)
                     reserva.importe_estadia= total_estadia_con_descuento_diez
                     reserva.total = total_estadia_con_descuento_diez + float(importe_otros_gast)
                     
               #-------------aumento-----------    
                     total= reserva.total
                     total2 = total *float(aumento_Total)/100
                     total3 = total +total2
                     
                     reserva.total = total3
                     
                     reserva.total_senia=0
                      
                     reserva.save()
                      #-------------la parte de la seña de la reserva---------------
                    
                     aumento_senia = float(reserva.total) * float(porcentaje_de_senia) /100
                     aumento_total2 = aumento_senia
                     reserva.total_senia=  aumento_total2
                 
                     #reserva.total= total
                 
                
                 
                     reserva.save()
                     
                     
                   
                    
               else:
                    if fechaConvertida2.hour >=10 and fechaConvertida2.hour <18:
                          total_estadia_con_descuento_Late =descuento_delTotal_Promocion_menosLate(request, fecha_entra, fecha_sali, habitacions, importe_otros_gast)
                          reserva.importe_estadia= total_estadia_con_descuento_Late
                          reserva.total= total_estadia_con_descuento_Late + float(importe_otros_gast)
                          
                        
                 
          #---------------------aumento-------------------------------
                  
                      
                    total= reserva.total
                    total2 = total *float(aumento_Total)/100
                    total3 = total +total2
                    
       
                     
                    reserva.total = total3
                    
                    reserva.total_senia=0
                      
                    reserva.save()
                    
                   # messages.success(request, "tres seleccionados")
                    
                    #-------------la parte de la seña de la reserva---------------
                    
                    aumento_senia = float(reserva.total) * float(porcentaje_de_senia) /100
                    aumento_total2 = aumento_senia
                    reserva.total_senia=  aumento_total2
                 
                   # reserva.total= total
                 
                
                 
                    reserva.save()
               return redirect('ModificarReservas')     
          elif int(porcentaje_de_senia) !=0  and int(aumento_Total) != 0 and int(descuento_total_importe) != 0:
                # messages.success(request, "ultimas tres opciones")
                 reserva.habitacion =habitacion 
          
                 reserva.huesped = huesped
                 reserva.fecha_entrada= fechaFormateada
                 reserva.fecha_salida = fechaFormateada2
          
          #-------------------agregue los descuentos ---------------------
          
                 reserva.descuento_importe_noche=descuento_porNoche
                 reserva.descuento_total_calcularo=descuento_total_importe
                 reserva.aumento_total= aumento_Total
          
         #----------------------------------------------------------- 
       
                 reserva.importe_otros_gasto = importe_otros_gast
        
                 reserva.estado=true_variable
       
                
                 reserva.importe_estadia= importeEstadia
                
                 descuentoTotal = total* float(descuento_total_importe) /100
                 descuentoTotal2 = descuentoTotal
                  
               
                 reserva.total= total - descuentoTotal2
                 
                 #-------le agregue estado y total seña---------------------------
                 reserva.estado= true_variable
                 reserva.total_senia=0
                 #-----------------------------------------------
                 
                 reserva.save()
               
                # messages.success(request, "agrego descuento al total importe")
                 #----------------------------------------
                 
                 total= reserva.importe_estadia
                      
                 #estadia_mas_otros_gastos = float(contrato.importe_estadia)+ float(contrato.importe_otros_gasto)
                 estadia_mas_otros_gastos = float(reserva.importe_estadia)+ float(importe_otros_gast)
                      
                 descuento =estadia_mas_otros_gastos*float(descuento_total_importe)/100
                      
                      
                 tota2 = estadia_mas_otros_gastos- descuento
                      
                 tota2 = tota2 + tota2 *float(aumento_Total)/100
                 
                 reserva.porcentaje_de_senia=porcentaje_de_senia
                          
                     
                      
                 reserva.total = tota2
                 
                 messages.success(request, "agrego descuento al total importe, y luego un aumento al total, mas el porcentaje de la reserva")
                      
                 reserva.save()
                 #-------------------la parte de la seña----------------------------------
                 aumento_senia = float(reserva.total) * float(porcentaje_de_senia) /100
                 aumento_total2 = aumento_senia
                 reserva.total_senia=  aumento_total2
                 
                   # reserva.total= total
                 
                
                 
                 reserva.save()
                       
                    
                 return redirect('ModificarReservas') 
               
          else:
               
               
               reserva.importe_estadia= importeEstadia
               reserva.total= total
             
               
          
         
              
                         
  
              
     
          
               reserva.habitacion =habitacion # obtuve la habitacion mediante el id---volver atras---
          
               reserva.huesped = huesped
               reserva.fecha_entrada= fechaFormateada
               reserva.fecha_salida = fechaFormateada2
          
          #-------------------agregue los descuentos ---------------------
          
               reserva.descuento_importe_noche=descuento_porNoche
               reserva.descuento_total_calcularo=descuento_total_importe
               reserva.aumento_total= aumento_Total
          
         #----------------------------------------------------------- 
       
               reserva.importe_otros_gasto = importe_otros_gast
        
               reserva.estado=true_variable
          
               reserva.total_senia=0
          
               reserva.porcentaje_de_senia= porcentaje_de_senia
               
              
               
               
       
        
         
          
               
          
          
         #----para---------volver------atras de try----------------------
               try:
          
           
        
           #ponerTrue_alUltimoContrato(request, habitacions)
          # ponerOcupada_ultimaHabitacion(request, habitacions)
          
           
          
                  reserva.save()
                 
          
           
          
         
               
               
           
           
          
        
                  messages.success(request, "La reserva se actualizo correctamente...")
                  return redirect('ModificarReservas')
                 
          
               
            
           
           
               except:
                 messages.error(request, "La reserva no se actualizo...")
               
               
        
             
                    
      
             
          
     else:
         reserva.fecha_salida=  str(reserva.fecha_salida)
         reserva.fecha_entrada=  str(reserva.fecha_entrada)
         formReserva = FormReserva(instance=reserva)
          
        # form2 = FormReserva()
        
     
     
     
     return render(request, "reservas/modificar_tablaReserva.html", {'formReserva': formReserva})
     
     #me genera error al guardar la reserva descuento por noche mas poecentaje de senia(ya lo solucione, haltaba agregar la variable habitacion)
     
     # me redirecciona a la tabla hasta ahora--comun--desc hab por noche--aumento total---descuento al total
     # descuento_porNoche aumento_Total --- descuento_total_importe aumento_Total---porcentaje de seña-- porcentaje_de_senia descuento_porNoche-----
     #  porcentaje_de_senia descuento_total_importe----- porcentaje_de_senia aumento_Total
     # porcentaje_de_senia aumento_Total descuento_porNoche--- porcentaje_de_senia aumento_Total descuento_total_importe
     

#------------------TRAER CONTRATO PARA GUARDAR CONTRATO RESERVA---------------------------------------


def cancelarReserva(request, id_reserva):
       
        reserva = get_object_or_404(Reserva, id=id_reserva)
       # apellido = huesped.apellido
        
       
        if request.method == "GET": 
         reserva.cancelar = "SI"
         
         reserva.estado=False
         
         reserva.save()
         messages.success(request, "Se cancelo la reserva...")
         
         return redirect('ModificarReservas')
       
               
def quitar_cancelarReserva(request, id_reserva):
       
        reserva = get_object_or_404(Reserva, id=id_reserva)
       # apellido = huesped.apellido
        
       
        if request.method == "GET": 
         reserva.cancelar = "NO"
         
         reserva.estado=True
         
         reserva.save()
         messages.success(request, "Se quito cancelar reserva")
         
         return redirect('ModificarReservas')
       
       
       
def reservas_totales(request):
      
       reservas_totales = Reserva.objects.all()
       FormReservas=FormReserva()
       formHuesped_reservas=FormHuesped_reserva()
       
      
      
      
      
      
       return render(request, "reservas/reservas_totales.html", {'FormReservas': FormReservas, 'FormHuesped_reservas':formHuesped_reservas, 'reservas_totales':reservas_totales})
 
 
def poner_False_despues_despuesDelPlazo_reservas(request): 
    
     reservas = Reserva.objects.all()
     if request.method=="GET":
           hoy = datetime.datetime.now()
            
           
           for reser in reservas:
                 if hoy >= reser.fecha_salida: 
                      # print("fecha salida mas uno")
                       id = reser.id
                       reserva = get_object_or_404(Reserva, id=id)
                       reserva.estado=False
                       reserva.save()
                       
                     
     # fecha_entra = request.GET["fecha_entrada"]
     # fecha_sali = request.GET["fecha_salida"]
   
     # fechaConvertida = datetime.datetime.strptime(fecha_entra, '%Y-%m-%dT%H:%M') # strptime lo convierto a objeto datetime, el segundo parametro le dice como interpretar la fecha, cual es la hora, el dia, el mes etc
     
         
        
     # fechaConvertida2 = datetime.datetime.strptime(fecha_sali, '%Y-%m-%dT%H:%M')
        
    
     # dia_delta = datetime.timedelta(seconds=1)#timedelta es una instacia de datetime
      #fecha_mas_delta = fechaConvertida2 + dia_delta
        
     # if fechaConvertida2 >= fecha_mas_delta:
          
          # print("se aplico el delta", fecha_sali)
        
        
'''def mostrar_calendario(request):
      reserva = Reserva.objects.filter(estado=True)
      for reser in reserva:
            #---------volver--atras--------
      
        diccionario_fechas = [
         {'title': 'Reserva', 'start': str(reser.fecha_entrada), 'end': str(reser.fecha_salida)},
        
    ]
      context = {'diccionario_fecha': diccionario_fechas}
      
      return render(request, "reservas/calendario.html", context)'''


def calendar_events(request):
    reserva = Reserva.objects.filter(estado=True)
    
    #hoy = str(datetime.datetime.now())
   # datatest2 = json.dumps(hoy)
     
     
    event_list = []
    for event in reserva:
        event_list.append({
            'title':"habitación:"+ event.habitacion.nombre_numero,
            'start': str(event.fecha_entrada),
            
            'end': str(event.fecha_salida) if event.fecha_salida else None
           
        })
    #data = JsonResponse((event_list), safe=False)
    datatest = json.dumps(event_list)
    
    context = {
        "datos_calendario": datatest
    }
  


    return render(request, "reservas/calendario.html", context)



def eliminar_para_que_noSeRepita(request):
      
      
     pass
            

