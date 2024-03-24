from django.shortcuts import render
from habitacion.models import Habitacion
from contrato.models import Contrato
import datetime

# Create your views here.

def mostrarPanel(request):
  
    data={}
  
  
    habitacion = Habitacion.objects.all()
    contrato = Contrato.objects.all()
    #habitacion = Habitacion()
    
    
   #------------DIAGRAMA-------------------
    contratos = Contrato.objects.all()
    ultimoFecha = datetime.datetime.now()
    ultimo= ultimoFecha.year
    
    anteultimo_anio = ultimo -1 
    
   
   
    
    

    
    enero=list()
    febrero=list()
    marzo=list()
    abril=list()
    mayo=list()
    junio=list()
    julio=list()
    agosto=list()
    septiembre=list()
    octubre=list()
    noviembre=list()
    diciembre=list()
    #------------
    actual=list()
    anteUltimo=list()
    #------------
    cantidadEnero=0
    
    cantidadFebrero=0
    cantidadMarzo=0
    cantidadAbril=0
    cantidadMayo=0
    
    cantidadJunio=0
    cantidadJulio=0
    cantidadAgosto=0
    cantidadSeptiembre=0
    cantidadOctubre=0
    cantidadNoviembre=0
    cantidadDiciembre=0
    
    #--------------
    total_anioActual=0
    total_anioAnterior=0
    
    
    #---año anterior---
     #------------
    cantidadEneroAnterior=0
    
    cantidadFebreroAnterior=0
    cantidadMarzoAnterior=0
    cantidadAbrilAnterior=0
    cantidadMayoAnterior=0
    
    cantidadJunioAnterior=0
    cantidadJulioAnterior=0
    cantidadAgostoAnterior=0
    cantidadSeptiembreAnterior=0
    cantidadOctubreAnterior=0
    cantidadNoviembreAnterior=0
    cantidadDiciembreAnterior=0
    
    eneroAnt=list()
    febreroAnt=list()
    marzoAnt=list()
    abrilAnt=list()
    mayoAnt=list()
    junioAnt=list()
    julioAnt=list()
    agostoAnt=list()
    septiembreAnt=list()
    octubreAnt=list()
    noviembreAnt=list()
    diciembreAnt=list()
    
    
    
    
    
    
    
    
   
    
    
    #  #---------------------------------------timeDelta-----------------------------------------------
    #fecha_sali = request.POST.get("fecha_salida")

     
    #fechaConvertida2 = datetime.datetime.strptime(fecha_sali, '%Y-%m-%dT%H:%M')
   
    #dia_delta = datetime.timedelta(seconds=1)
    #fechaFutura = fechaConvertida2+dia_delta
    
     #-----------------------------------------------------------------------------------------------
  
    
    
    habitacionesLibres = list()
   # habitacionesPostOcupadas = list()
    habitacionesNoLimpias = list()
    #----------------------------
    habitaciones_post = list()
    habitacionesOcupadas = list()
    #-----------traer el ultimo elemento de la lista----------
    ultimo_ocupado=list()
    ultimo_Post=list()
    
    
    
    
    
    
   
    #volver atras---------------------------------------------------------------------------
    for habi in habitacion:
      if habi.estado =="Null" and habi.eliminado==False: # agregue eliminado==False porque en el panel me aparecian las habitaciones eliminadas (26/11/23, 20:34 hs.)
          habitacionesLibres.append(habi)
          
      
    
    
   
      
          
   
          
    
          
        
    for contra in contrato:
       fecha_sali = contra.fecha_salida
       hoy = datetime.datetime.now()
       #fechaConvertida2 = datetime.datetime.strptime(fecha_sali, '%Y-%m-%dT%H:%M')
      # dia_delta = datetime.timedelta(seconds=1)
      # fecha_futura = fecha_sali+dia_delta
     
      
      
      
       if hoy >= fecha_sali and contra.habitacion.estado == "ocupada" and contra.estado==True: # le agregue el true
         
          habitaciones_post.append(contra)
         # ultimo_Post= habitaciones_post[-1]
        
       
       elif  fecha_sali > hoy and contra.habitacion.estado == "ocupada" and contra.estado==True:
           habitacionesOcupadas.append(contra)
          # ultimo_ocupado= habitacionesOcupadas[-1]
          
          
          #--------------------------------DIAGRAMA----------------------------------
          
          
    for con in contratos:
       #---------------------------enero------------------------------------------------------------
       if con.fecha_entrada.month==1  and con.fecha_entrada.year==ultimo:
         enero.append(con)
         cantidadEnero= len(enero)
         #-----------------------------------------------------------------------------------------------
          #---------------------------febrero------------------------------------------------------------
       elif con.fecha_entrada.month==2 and con.fecha_entrada.year==ultimo:
         febrero.append(con)
         cantidadFebrero= len(febrero)
         #-----------------------------------------------------------------------------------------------
          #---------------------------marzo------------------------------------------------------------
       elif con.fecha_entrada.month==3  and con.fecha_entrada.year==ultimo:
         marzo.append(con)
         cantidadMarzo= len(marzo)
         #-----------------------------------------------------------------------------------------------
          #---------------------------abril------------------------------------------------------------
       elif con.fecha_entrada.month==4 and con.fecha_entrada.year==ultimo:
         abril.append(con)
         cantidadAbril= len(abril)
         #-----------------------------------------------------------------------------------------------
          #---------------------------mayo------------------------------------------------------------
       elif con.fecha_entrada.month==5 and con.fecha_entrada.year==ultimo:
         mayo.append(con)
         cantidadMayo= len(mayo)
         #-----------------------------------------------------------------------------------------------
         
       #---------------------------junio------------------------------------------------------------
       elif con.fecha_entrada.month==6 and con.fecha_entrada.year==ultimo:
         junio.append(con)
         cantidadJunio= len(junio)
         #-----------------------------------------------------------------------------------------------
         
           #---------------------------julio------------------------------------------------------------
       elif con.fecha_entrada.month==7 and con.fecha_entrada.year==ultimo:
         julio.append(con)
         cantidadJulio= len(julio)
         #-----------------------------------------------------------------------------------------------
          #---------------------------agosto------------------------------------------------------------
       elif con.fecha_entrada.month==8 and con.fecha_entrada.year==ultimo:
         agosto.append(con)
         cantidadAgosto= len(agosto)
         #-----------------------------------------------------------------------------------------------
          #---------------------------septiembre------------------------------------------------------------
       elif con.fecha_entrada.month==9  and con.fecha_entrada.year==ultimo:
         septiembre.append(con)
         cantidadSeptiembre= len(septiembre)
         #-----------------------------------------------------------------------------------------------
          #---------------------------octubre------------------------------------------------------------
       elif con.fecha_entrada.month==10 and con.fecha_entrada.year==ultimo:
         octubre.append(con)
         cantidadOctubre= len(octubre)
         #-----------------------------------------------------------------------------------------------
          #---------------------------noviembre------------------------------------------------------------
       elif con.fecha_entrada.month==11  and con.fecha_entrada.year==ultimo:
         noviembre.append(con)
         cantidadNoviembre= len(noviembre)
         #-----------------------------------------------------------------------------------------------
          #---------------------------diciembre------------------------------------------------------------
       elif con.fecha_entrada.month==12 and con.fecha_entrada.year==ultimo:
         diciembre.append(con)
         cantidadDiciembre= len(diciembre)
         
         
         
         
         
         #--------------------------------CONTRATOS DEL AÑO ANTERIOR------------------------------------------------------
         
       elif con.fecha_entrada.month==1  and con.fecha_entrada.year== anteultimo_anio:
         eneroAnt.append(con)
         cantidadEneroAnterior= len(eneroAnt)
         #-----------------------------------------------------------------------------------------------
          #---------------------------febrero------------------------------------------------------------
       elif con.fecha_entrada.month==2 and con.fecha_entrada.year== anteultimo_anio:
         febreroAnt.append(con)
         cantidadFebreroAnterior= len(febreroAnt)
         #-----------------------------------------------------------------------------------------------
          #---------------------------marzo------------------------------------------------------------
       elif con.fecha_entrada.month==3  and con.fecha_entrada.year== anteultimo_anio:
         marzoAnt.append(con)
         cantidadMarzoAnterior= len(marzoAnt)
         #-----------------------------------------------------------------------------------------------
          #---------------------------abril------------------------------------------------------------
       elif con.fecha_entrada.month==4 and con.fecha_entrada.year== anteultimo_anio:
         abrilAnt.append(con)
         cantidadAbrilAnterior= len(abrilAnt)
         #-----------------------------------------------------------------------------------------------
          #---------------------------mayo------------------------------------------------------------
       elif con.fecha_entrada.month==5 and con.fecha_entrada.year== anteultimo_anio:
         mayoAnt.append(con)
         cantidadMayoAnterior= len(mayoAnt)
         #-----------------------------------------------------------------------------------------------
         
       #---------------------------junio------------------------------------------------------------
       elif con.fecha_entrada.month==6 and con.fecha_entrada.year== anteultimo_anio:
         junioAnt.append(con)
         cantidadJunioAnterior= len(junioAnt)
         #-----------------------------------------------------------------------------------------------
         
           #---------------------------julio------------------------------------------------------------
       elif con.fecha_entrada.month==7 and con.fecha_entrada.year== anteultimo_anio:
         julioAnt.append(con)
         cantidadJulioAnterior= len(julioAnt)
         #-----------------------------------------------------------------------------------------------
          #---------------------------agosto------------------------------------------------------------
       elif con.fecha_entrada.month==8 and con.fecha_entrada.year== anteultimo_anio:
         agostoAnt.append(con)
         cantidadAgostoAnterior= len(agostoAnt)
         #-----------------------------------------------------------------------------------------------
          #---------------------------septiembre------------------------------------------------------------
       elif con.fecha_entrada.month==9  and con.fecha_entrada.year== anteultimo_anio:
         septiembreAnt.append(con)
         cantidadSeptiembreAnterior= len(septiembreAnt)
         #-----------------------------------------------------------------------------------------------
          #---------------------------octubre------------------------------------------------------------
       elif con.fecha_entrada.month==10 and con.fecha_entrada.year== anteultimo_anio:
         octubreAnt.append(con)
         cantidadOctubreAnterior= len(octubreAnt)
         #-----------------------------------------------------------------------------------------------
          #---------------------------noviembre------------------------------------------------------------
       elif con.fecha_entrada.month==11  and con.fecha_entrada.year== anteultimo_anio:
         noviembreAnt.append(con)
         cantidadNoviembreAnterior= len(noviembreAnt)
         #-----------------------------------------------------------------------------------------------
          #---------------------------diciembre------------------------------------------------------------
       elif con.fecha_entrada.month==12 and con.fecha_entrada.year== anteultimo_anio:
         diciembreAnt.append(con)
         cantidadDiciembreAnterior= len(diciembreAnt)
         
       total_anioActual= cantidadEnero+cantidadFebrero+cantidadMarzo+cantidadAbril+cantidadMayo+cantidadJunio +cantidadJulio + cantidadAgosto +cantidadSeptiembre+ cantidadOctubre + cantidadNoviembre + cantidadDiciembre
       total_anioAnterior= cantidadEneroAnterior +cantidadFebreroAnterior +cantidadMarzoAnterior +cantidadAbrilAnterior +cantidadMayoAnterior +cantidadJunioAnterior +cantidadJulioAnterior + cantidadAgostoAnterior +cantidadSeptiembreAnterior+ cantidadOctubreAnterior + cantidadNoviembreAnterior + cantidadDiciembreAnterior
      
      
         
         
       data={"mesEnero": cantidadEnero, "mesFebrero":cantidadFebrero, "mesMarzo":cantidadMarzo, "mesAbril":cantidadAbril,
             "mesMayo": cantidadMayo, "mesJunio": cantidadJunio, "mesJulio": cantidadJulio, "mesAgosto": cantidadAgosto,
             "mesSeptiembre": cantidadSeptiembre, "mesOctubre": cantidadOctubre, "mesNoviembre":cantidadNoviembre,
             "mesDiciembre": cantidadDiciembre, "total_anioActual": total_anioActual, "total_anioAnterior":total_anioAnterior, "ultimo":ultimo, "anteultimo":anteultimo_anio}
         
         
      
        
         
   
    
    return render(request, "panel_de_admin/index.html", {'data':data,'habitacion': habitacionesLibres, 'contrato': contrato, 'habitacionesNoLimpias': habitacionesNoLimpias,
 'habitaciones_post':habitaciones_post, 'habitacionesOcupadas': habitacionesOcupadas})




# def datos_diagrama(request):
#     contratos = Contrato.objects.all()
#     #-----------------------------------------
#     enero=list()
#     febrero=list()
#     marzo=list()
    
#     abril=list()
#     mayo=list()
#     junio=list()
#     julio=list()
#     agosto=list()
#     septiembre=list()
#     octubre=list()
#     noviembre=list()
#     diciembre=list()
#     #----------------------------------
#     ultimoAnio = list()
    
    
    
#     ultimoFecha = datetime.datetime.now()
#     ultimo= ultimoFecha.year
    
#     probar = 100
  
  
    
# #     for contr in contratos:
# #          if contr.fecha_entrada.year>2022:
# #               ultimoAnio.append(contr)
# #               ultimo = ultimoAnio[-1]
         
    
#     for contrato in contratos:
#           if contrato.fecha_entrada.month==1 and contrato.fecha_entrada.year== contrato.fecha_entrada.year==ultimo:
#               enero.append(contrato)
#               cantidadEnero = enero.count
              
#           elif contrato.fecha_entrada.month==2 and contrato.fecha_entrada.year==ultimo:
#               febrero.append(contrato)
#               cantidadFebrero = febrero.count
              
#           elif contrato.fecha_entrada.month==3 and contrato.fecha_entrada.year==ultimo:
#               marzo.append(contrato)
#               cantidadMarzo = marzo.count
              
#           elif contrato.fecha_entrada.month==4 and contrato.fecha_entrada.year==ultimo:
#               abril.append(contrato)
#               cantidadAbril = abril.count
              
#           elif contrato.fecha_entrada.month==5 and contrato.fecha_entrada.year==ultimo:
#               mayo.append(contrato)
#               cantidadMayo = mayo.count
              
#           elif contrato.fecha_entrada.month==6 and contrato.fecha_entrada.year==ultimo:
#               junio.append(contrato)
#               cantidadJunio = junio.count
              
#           elif contrato.fecha_entrada.month==7 and contrato.fecha_entrada.year==ultimo:
#               julio.append(contrato)
#               cantidadJulio = julio.count
              
#           elif contrato.fecha_entrada.month==8 and contrato.fecha_entrada.year==ultimo:
#               agosto.append(contrato)
#               cantidadAgosto = agosto.count
              
#           elif contrato.fecha_entrada.month==9 and contrato.fecha_entrada.year==ultimo:
#               septiembre.append(contrato)
#               cantidadSeptiembre = septiembre.count
              
#           elif contrato.fecha_entrada.month==10 and contrato.fecha_entrada.year==ultimo:
#               octubre.append(contrato)
#               cantidadOctubre = octubre.count
              
#           elif contrato.fecha_entrada.month==11 and contrato.fecha_entrada.year==ultimo:
#               noviembre.append(contrato)
#               cantidadNoviembre = noviembre.count
              
#           elif contrato.fecha_entrada.month==12 and contrato.fecha_entrada.year==ultimo:
#               diciembre.append(contrato)
#               cantidadDiciembre = diciembre.count
              
              
#     data={'enero': cantidadEnero, 'febrero': cantidadFebrero, 'marzo': cantidadMarzo, 'abril': cantidadAbril,
#                'mayo': cantidadMayo, 'junio': cantidadJunio, 'julio': cantidadJulio, 'agosto': cantidadAgosto,
#                'septiembre': cantidadSeptiembre, 'octubre': cantidadOctubre, 'noviembre': cantidadNoviembre, 'diciembre': cantidadDiciembre}
              
              
              
              
         
         
#     return render(request, "panel_de_admin/diagramas.html", {'data': data, 'ultimo': ultimo, 'probar':probar})
              
              
     
    
def colocar_diagrama(request): 
    data={}
  
  
    habitacion = Habitacion.objects.all()
    contrato = Contrato.objects.all()
    #habitacion = Habitacion()
    
    
   #------------DIAGRAMA-------------------
    contratos = Contrato.objects.all()
    ultimoFecha = datetime.datetime.now()
    ultimo= ultimoFecha.year
    
    anteultimo_anio = ultimo -1 
    
   
   
    
    

    
    enero=list()
    febrero=list()
    marzo=list()
    abril=list()
    mayo=list()
    junio=list()
    julio=list()
    agosto=list()
    septiembre=list()
    octubre=list()
    noviembre=list()
    diciembre=list()
    #------------
    actual=list()
    anteUltimo=list()
    #------------
    cantidadEnero=0
    
    cantidadFebrero=0
    cantidadMarzo=0
    cantidadAbril=0
    cantidadMayo=0
    
    cantidadJunio=0
    cantidadJulio=0
    cantidadAgosto=0
    cantidadSeptiembre=0
    cantidadOctubre=0
    cantidadNoviembre=0
    cantidadDiciembre=0
    
    #--------------
    total_anioActual=0
    total_anioAnterior=0
    
    
    #---año anterior---
     #------------
    cantidadEneroAnterior=0
    
    cantidadFebreroAnterior=0
    cantidadMarzoAnterior=0
    cantidadAbrilAnterior=0
    cantidadMayoAnterior=0
    
    cantidadJunioAnterior=0
    cantidadJulioAnterior=0
    cantidadAgostoAnterior=0
    cantidadSeptiembreAnterior=0
    cantidadOctubreAnterior=0
    cantidadNoviembreAnterior=0
    cantidadDiciembreAnterior=0
    
    eneroAnt=list()
    febreroAnt=list()
    marzoAnt=list()
    abrilAnt=list()
    mayoAnt=list()
    junioAnt=list()
    julioAnt=list()
    agostoAnt=list()
    septiembreAnt=list()
    octubreAnt=list()
    noviembreAnt=list()
    diciembreAnt=list()
    
    
    
    
    
    
    
    
   
    
    
    #  #---------------------------------------timeDelta-----------------------------------------------
    #fecha_sali = request.POST.get("fecha_salida")

     
    #fechaConvertida2 = datetime.datetime.strptime(fecha_sali, '%Y-%m-%dT%H:%M')
   
    #dia_delta = datetime.timedelta(seconds=1)
    #fechaFutura = fechaConvertida2+dia_delta
    
     #-----------------------------------------------------------------------------------------------
  
    
    
    habitacionesLibres = list()
   # habitacionesPostOcupadas = list()
    habitacionesNoLimpias = list()
    #----------------------------
    habitaciones_post = list()
    habitacionesOcupadas = list()
    #-----------traer el ultimo elemento de la lista----------
    ultimo_ocupado=list()
    ultimo_Post=list()
    
    
    
    
    
    
   
    #volver atras---------------------------------------------------------------------------
    for habi in habitacion:
      if habi.estado =="Null" and habi.eliminado==False: # agregue eliminado==False porque en el panel me aparecian las habitaciones eliminadas (26/11/23, 20:34 hs.)
          habitacionesLibres.append(habi)
          
      
    
    
   
      
          
   
          
    
          
        
    for contra in contrato:
       fecha_sali = contra.fecha_salida
       hoy = datetime.datetime.now()
       #fechaConvertida2 = datetime.datetime.strptime(fecha_sali, '%Y-%m-%dT%H:%M')
      # dia_delta = datetime.timedelta(seconds=1)
      # fecha_futura = fecha_sali+dia_delta
     
      
      
      
       if hoy >= fecha_sali and contra.habitacion.estado == "ocupada" and contra.estado==True: # le agregue el true
         
          habitaciones_post.append(contra)
         # ultimo_Post= habitaciones_post[-1]
        
       
       elif  fecha_sali > hoy and contra.habitacion.estado == "ocupada" and contra.estado==True:
           habitacionesOcupadas.append(contra)
          # ultimo_ocupado= habitacionesOcupadas[-1]
          
          
          #--------------------------------DIAGRAMA----------------------------------
          
          
    for con in contratos:
       #---------------------------enero------------------------------------------------------------
       if con.fecha_entrada.month==1  and con.fecha_entrada.year==ultimo:
         enero.append(con)
         cantidadEnero= len(enero)
         #-----------------------------------------------------------------------------------------------
          #---------------------------febrero------------------------------------------------------------
       elif con.fecha_entrada.month==2 and con.fecha_entrada.year==ultimo:
         febrero.append(con)
         cantidadFebrero= len(febrero)
         #-----------------------------------------------------------------------------------------------
          #---------------------------marzo------------------------------------------------------------
       elif con.fecha_entrada.month==3  and con.fecha_entrada.year==ultimo:
         marzo.append(con)
         cantidadMarzo= len(marzo)
         #-----------------------------------------------------------------------------------------------
          #---------------------------abril------------------------------------------------------------
       elif con.fecha_entrada.month==4 and con.fecha_entrada.year==ultimo:
         abril.append(con)
         cantidadAbril= len(abril)
         #-----------------------------------------------------------------------------------------------
          #---------------------------mayo------------------------------------------------------------
       elif con.fecha_entrada.month==5 and con.fecha_entrada.year==ultimo:
         mayo.append(con)
         cantidadMayo= len(mayo)
         #-----------------------------------------------------------------------------------------------
         
       #---------------------------junio------------------------------------------------------------
       elif con.fecha_entrada.month==6 and con.fecha_entrada.year==ultimo:
         junio.append(con)
         cantidadJunio= len(junio)
         #-----------------------------------------------------------------------------------------------
         
           #---------------------------julio------------------------------------------------------------
       elif con.fecha_entrada.month==7 and con.fecha_entrada.year==ultimo:
         julio.append(con)
         cantidadJulio= len(julio)
         #-----------------------------------------------------------------------------------------------
          #---------------------------agosto------------------------------------------------------------
       elif con.fecha_entrada.month==8 and con.fecha_entrada.year==ultimo:
         agosto.append(con)
         cantidadAgosto= len(agosto)
         #-----------------------------------------------------------------------------------------------
          #---------------------------septiembre------------------------------------------------------------
       elif con.fecha_entrada.month==9  and con.fecha_entrada.year==ultimo:
         septiembre.append(con)
         cantidadSeptiembre= len(septiembre)
         #-----------------------------------------------------------------------------------------------
          #---------------------------octubre------------------------------------------------------------
       elif con.fecha_entrada.month==10 and con.fecha_entrada.year==ultimo:
         octubre.append(con)
         cantidadOctubre= len(octubre)
         #-----------------------------------------------------------------------------------------------
          #---------------------------noviembre------------------------------------------------------------
       elif con.fecha_entrada.month==11  and con.fecha_entrada.year==ultimo:
         noviembre.append(con)
         cantidadNoviembre= len(noviembre)
         #-----------------------------------------------------------------------------------------------
          #---------------------------diciembre------------------------------------------------------------
       elif con.fecha_entrada.month==12 and con.fecha_entrada.year==ultimo:
         diciembre.append(con)
         cantidadDiciembre= len(diciembre)
         
         
         
         
         
         #--------------------------------CONTRATOS DEL AÑO ANTERIOR------------------------------------------------------
         
       elif con.fecha_entrada.month==1  and con.fecha_entrada.year== anteultimo_anio:
         eneroAnt.append(con)
         cantidadEneroAnterior= len(eneroAnt)
         #-----------------------------------------------------------------------------------------------
          #---------------------------febrero------------------------------------------------------------
       elif con.fecha_entrada.month==2 and con.fecha_entrada.year== anteultimo_anio:
         febreroAnt.append(con)
         cantidadFebreroAnterior= len(febreroAnt)
         #-----------------------------------------------------------------------------------------------
          #---------------------------marzo------------------------------------------------------------
       elif con.fecha_entrada.month==3  and con.fecha_entrada.year== anteultimo_anio:
         marzoAnt.append(con)
         cantidadMarzoAnterior= len(marzoAnt)
         #-----------------------------------------------------------------------------------------------
          #---------------------------abril------------------------------------------------------------
       elif con.fecha_entrada.month==4 and con.fecha_entrada.year== anteultimo_anio:
         abrilAnt.append(con)
         cantidadAbrilAnterior= len(abrilAnt)
         #-----------------------------------------------------------------------------------------------
          #---------------------------mayo------------------------------------------------------------
       elif con.fecha_entrada.month==5 and con.fecha_entrada.year== anteultimo_anio:
         mayoAnt.append(con)
         cantidadMayoAnterior= len(mayoAnt)
         #-----------------------------------------------------------------------------------------------
         
       #---------------------------junio------------------------------------------------------------
       elif con.fecha_entrada.month==6 and con.fecha_entrada.year== anteultimo_anio:
         junioAnt.append(con)
         cantidadJunioAnterior= len(junioAnt)
         #-----------------------------------------------------------------------------------------------
         
           #---------------------------julio------------------------------------------------------------
       elif con.fecha_entrada.month==7 and con.fecha_entrada.year== anteultimo_anio:
         julioAnt.append(con)
         cantidadJulioAnterior= len(julioAnt)
         #-----------------------------------------------------------------------------------------------
          #---------------------------agosto------------------------------------------------------------
       elif con.fecha_entrada.month==8 and con.fecha_entrada.year== anteultimo_anio:
         agostoAnt.append(con)
         cantidadAgostoAnterior= len(agostoAnt)
         #-----------------------------------------------------------------------------------------------
          #---------------------------septiembre------------------------------------------------------------
       elif con.fecha_entrada.month==9  and con.fecha_entrada.year== anteultimo_anio:
         septiembreAnt.append(con)
         cantidadSeptiembreAnterior= len(septiembreAnt)
         #-----------------------------------------------------------------------------------------------
          #---------------------------octubre------------------------------------------------------------
       elif con.fecha_entrada.month==10 and con.fecha_entrada.year== anteultimo_anio:
         octubreAnt.append(con)
         cantidadOctubreAnterior= len(octubreAnt)
         #-----------------------------------------------------------------------------------------------
          #---------------------------noviembre------------------------------------------------------------
       elif con.fecha_entrada.month==11  and con.fecha_entrada.year== anteultimo_anio:
         noviembreAnt.append(con)
         cantidadNoviembreAnterior= len(noviembreAnt)
         #-----------------------------------------------------------------------------------------------
          #---------------------------diciembre------------------------------------------------------------
       elif con.fecha_entrada.month==12 and con.fecha_entrada.year== anteultimo_anio:
         diciembreAnt.append(con)
         cantidadDiciembreAnterior= len(diciembreAnt)
         
       total_anioActual= cantidadEnero+cantidadFebrero+cantidadMarzo+cantidadAbril+cantidadMayo+cantidadJunio +cantidadJulio + cantidadAgosto +cantidadSeptiembre+ cantidadOctubre + cantidadNoviembre + cantidadDiciembre
       total_anioAnterior= cantidadEneroAnterior +cantidadFebreroAnterior +cantidadMarzoAnterior +cantidadAbrilAnterior +cantidadMayoAnterior +cantidadJunioAnterior +cantidadJulioAnterior + cantidadAgostoAnterior +cantidadSeptiembreAnterior+ cantidadOctubreAnterior + cantidadNoviembreAnterior + cantidadDiciembreAnterior
      
      
         
         
       data={"mesEnero": cantidadEnero, "mesFebrero":cantidadFebrero, "mesMarzo":cantidadMarzo, "mesAbril":cantidadAbril,
             "mesMayo": cantidadMayo, "mesJunio": cantidadJunio, "mesJulio": cantidadJulio, "mesAgosto": cantidadAgosto,
             "mesSeptiembre": cantidadSeptiembre, "mesOctubre": cantidadOctubre, "mesNoviembre":cantidadNoviembre,
             "mesDiciembre": cantidadDiciembre, "total_anioActual": total_anioActual, "total_anioAnterior":total_anioAnterior, "ultimo":ultimo, "anteultimo":anteultimo_anio}
         
         
      
        
         
   
    
    return render(request, "panel_de_admin/colocar_diagrama.html", {'data':data,'habitacion': habitacionesLibres, 'contrato': contrato, 'habitacionesNoLimpias': habitacionesNoLimpias,
 'habitaciones_post':habitaciones_post, 'habitacionesOcupadas': habitacionesOcupadas})



  
  
  

    

