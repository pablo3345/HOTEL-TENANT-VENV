from django.shortcuts import render, redirect
from django.contrib.auth.models import User
#from django.contrib.auth.decorators import login_required

from django.contrib import messages
#import phonenumbers
#from django.http import HttpResponse
#---volver atras--------------------------------------------------
from shared.models import Client, Domain
# Create your views here.
from django.http import HttpResponseRedirect 

#from django.urls import reverse
from django.template.loader import render_to_string

from django.utils.html import strip_tags
from django.core.mail import send_mail

from django.http import HttpResponse


def manual_usuario(request):
    
    return render(request, "proyectoWebApp/manual_usuario.html")


def inicio(request):
    
   # variable_inicio= kwargs.get("variable_inicio")
    
    usuarios = User.objects.all()
    
    ultimo_domonio = Domain.objects.last()
    variable_inicio= ultimo_domonio.domain
    
    #------ultimo cliente para obtener el nombre para la pagina inicio
    
    cliente = Client.objects.last()
    nombre = cliente.first_name
          
    
   # print("llego hasta inicio para probar ultima", variable_inicio)
    
  
    
  
    return render(request, "proyectoWebApp/inicio.html", {'usuarios': usuarios, 'variable_inicio': variable_inicio, 'nombre':nombre})



def paginaPrincipal(request):
   
    
   #-------------cuando is_active esta en False--------------------------------------------------
   
   # dominio_actual = request.get_host() # dominio actual
    
   
    
   # subdominioActual= dominio_actual.split('.')[0] # subdominio actual
    
    '''tenant_actual = request.tenant # cliente actual
    
    
    if tenant_actual.is_active ==False:
        
        mensaje="Esta página de desactivo"
        
        return redirect("is_active_false")'''
    
    
   
    
    totalClientes = Client.objects.all()
    
    cliente=Client()
    
    
    
    domain=Domain()
    
   
    
    
    usuarios = User.objects.all()
    
   
    if request.method == 'POST':
        
        
        
        
       
        
         
         numero_telefono = request.POST.get("mobile-number2")
         firsr_name = request.POST.get("first_name")
         last_name = request.POST.get("last_name")
         email = request.POST.get("email")
         email2 = request.POST.get("email2")
         dni = request.POST.get("dni")
         business_name= request.POST.get("business_name")
         cant_habi=request.POST.get("cant_habi")
         
         clave=request.POST.get("clave")
         
         
         
     #volver atras----------------------------------------------------------
         
         if email != email2:
              messages.error(request, "Los correo electronicos no coinciden, vuelva a cargar el formulario...")
              return redirect("paginaPrincipal")
          
         elif len(clave) >12:
                messages.error(request, "La clave es demasiada larga, intentelo nuevamente...")
                return redirect("paginaPrincipal")
             
         for cli in totalClientes:
             if clave== cli.clave:
                messages.error(request, "Esta clave es igual a otra, vuelva a intentarlo nuevamente...")
                return redirect("paginaPrincipal")
              
           
            
        
         
         cliente.first_name= firsr_name
         cliente.last_name=last_name
         cliente.email=email
         cliente.email2=email2
         cliente.dni=dni
         cliente.business_name=business_name
         cliente.cantidad_habitacion=cant_habi
         cliente.phone_number=numero_telefono
         
         cliente.clave=clave
         
        
        # cliente.schema_name= cliente.last_name +"-dni-"+ cliente.dni
         cliente.schema_name= cliente.last_name +"-"+ cliente.clave.lower()
         
         cliente.name=cliente.last_name +"-dni-"+ cliente.dni
         
         cliente.is_active=True
         
         
         #-------------volver atras----------------------------------------------------------
         #--------------domain-----------------------------
         
         #------esto lo hago para obtener los ultimos 1 numeros del dni---------------
         
         ultimos_uno = cliente.dni[-1:]
         
         
         domain.is_primary=True
         domain.tenant=cliente
         domain.domain=clave.lower()+"-"+ultimos_uno+"."+"localhost" # con lower() convierto a minusculas
         
        
        # variable=cliente.dni
      
         variable=clave+"-"+ultimos_uno
    
         
  
         try:
         
             
          cliente.save()
          domain.save()
        #  messages.success(request, "El cliente se guardo correctamente, le enviamos un mail con su dominio para que lo guarde y entre con al sistema")
        
         
        
          enviar_mail(request)
        
        
        
         
               
        
       
          dynamic_url = f"http://{variable}.localhost:8000/inicio"
          return redirect(dynamic_url)
      
        
        
    
             
         except:
              messages.error(request, "Surgió un error...")
         
        
       
       
      
         
        
         
         

        
       
    return render(request, "proyectoWebApp/paginaPrincipal.html", {'usuarios':usuarios})
    
  
    
   
    
  
    
  
   






def miError_404(request, exception):
    
    
    
    return render(request, "proyectoWebApp/404.html")
           
def miError_500(request):
    
    return render(request, "proyectoWebApp/500.html")
       
       



def enviar_mail(request):
    
   ultimo_domonio = Domain.objects.last()
   ultimo_cliente = Client.objects.last()
   
   nombre = ultimo_cliente.first_name
   apellido= ultimo_cliente.last_name
   dominio= ultimo_domonio.domain 
   
   email_destino= ultimo_cliente.email
    
     # render_to_string es que me renderice en pedido.html estos datos
   asunto = "dominio para ingresar a sycod hotel"
   mensaje= render_to_string("proyectoWebApp/email.html",  {'nombre': nombre,
                                                            'apellido': apellido,
                                                            'dominio':dominio

    

   }) # aca vamos a guardar todas las lineas de pedido como lineas pedidos de arriba, con render_to_string le decimos que renderice el siguiente html

   mensaje_texto=strip_tags(mensaje) # esto va a ser igual a la variable mensaje que creamos arriba donde hemos renderizado toda la informacion, pero ignorando toda etiqueta html como esta<> lo hacemos con strip_tags, le decimos que ignore las etiquetas html de la variable mensaje

   from_mail="sycod.hotel@gmail.com" # de quien es el correo electronico, el de la tienda, el que los manda
   #to=  kwargs.get("emailusuario")# el destinatario de los correos, con kwargs.get() obtengo los parametros de la funcion de arriba que le pase enviar_mail(), como no puse ningun usuario con un correo valido a esto lo comento y pongo mi correo personal

   to= email_destino
  # to2= "pabloandresperuchi@gmail.com" # cuando quiero enviar a mas de un destinatario



   #ahora entra la funcion send_mail para enviar el mail

   send_mail(asunto, mensaje_texto, from_mail, [to], html_message=mensaje) #mensaje texto es el mensaje sin etiquetas html, cuando enviamos un mensaje html debemos especificarlo con html_message=
   
   
   
   

def politica_de_privacidad(request):
    
    
    return render(request, "proyectoWebApp/politica_privacidad.html")




def is_active_false(request):
    
    return render(request, "proyectoWebApp/is_active_false.html")




