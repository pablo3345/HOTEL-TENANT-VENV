
from django.shortcuts import render, redirect
#from contacto.forms import FormularioContacto
from django.core.mail import EmailMessage

from django.contrib import messages
#----volver atras--------------------------------------------------------------------------------------
# Create your views here.
def contacto(request):
   # formulario_Contacto = FormularioContacto()

    if request.method =="POST": #si se ha hecho POST tiene que rescatar la informacion que esta en el formulario
       # formulario_Contacto = FormularioContacto(data=request.POST) #aca lo que hicimos es cargar en el formulario la informacion que ha ido introduciendo en el formulario (esto lo hago con date=request.POST)
       # if formulario_Contacto.is_valid(): si el formulario es valido me vas a guardar en las variable lo que tenemos almacenado

            nombre = request.POST.get("nombre2")
            email = request.POST.get("email2")
            contenido = request.POST.get("mensaje2")
            
            tel = request.POST.get("mobile-number3")
            
            name_establecimiento= request.POST.get("establecimento_dos")

            #nombreParaEliminar = formulario_Contacto.cleaned_data.get("nombre") # solo hice esto para probar a ver si obtengo solo el nombre del formulario

            email=EmailMessage("Mensaje desde sycod hotel", # el asunto del correo cuando lo recibo
            "El usuario con nombre {} y establecimiento {} con telefono {} con direccion {} escribe lo siguiente:\n\n {}".format(nombre, name_establecimiento, tel, email, contenido), "", ["sycod.hotel@gmail.com"], reply_to=[email]) # las "" no pongo nada xq ya se que el mail viene de la aplicacion, el reply_to significa que puedo responderle al correo que me envian

            try:
                email.send() # creiria que este email se relaciona solo con email=EmailMessage, los otros email deben ser del formulario
                messages.success(request, "el mail se envio correctamente")
                return redirect("paginaPrincipal") #le paso por parametro la palabra valido en la url para hacer un if en el html con la palabra valido, y me aparezca el mensaje que la informacion se envio correctamente


            except:
                messages.error(request, "el mail no se envio")

                return redirect("paginaPrincipal")
            
            
    return redirect(request, "proyectoWebApp/paginaPrincipal.html")



    
         

          
