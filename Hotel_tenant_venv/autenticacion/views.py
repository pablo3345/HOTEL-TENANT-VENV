from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from autenticacion.forms import RegistroForms

# Create your views here.

class VRegistro(View):
    
    def get(self, request): #get para mostrar el formulario
       #formRegistro= UserCreationForm
       formRegistro= RegistroForms()
       return render(request, "registro/registro.html", {'formRegistro':formRegistro})
        
        
        
    def post(self, request): #post para enviar los datos a la bbdd
        # formRegistro =  UserCreationForm(request.POST)
       formRegistro= RegistroForms(request.POST)#request es la peticion y POST es todos los datos que estamos enviando como el usuario y la contraseña
       if formRegistro.is_valid(): # por si no me marca error al crear la contraseña, osea si no respeto lo que dice el formulario de autenticacion
         usuario = formRegistro.save() #creamos una variable usuario, donde se va a almacenar la informacion del formulario, con esto save() se almacenan los datos en la base de datos de usuarios
         login(request, usuario) # una vez que lo guardo en la base de datos, quiero que el usuario este logeado
         return redirect('Habitacion') # nos redirecciona a la url home
     
       else:
           for msg in formRegistro.error_messages: # un for para recorrer los errores que haya en el formulario
             messages.error(request, formRegistro.error_messages[msg]) #esto es para mostrarme ese error, [msg] esto es porque es un array de errores, msg para mostrar la ubicacion del error en concreto
          
       return render(request, "registro/registro.html", {"formRegistro": formRegistro}) # para que me muestre el formulario con los errores, esta fuera del for


def cerrar_sesion(request): #una nueva vista
    logout(request)
    return redirect('paginaPrincipal')


    
def logear(request):
   if request.method == "POST": # si ha apretado el boton, si hizo un post
        formLogear = AuthenticationForm(request, data=request.POST) # aca en form me guarda los datos del formulario con los datos
        if formLogear.is_valid():
            nombre_usuario = formLogear.cleaned_data.get("username") #dame la informacion que tengo guardado en el cuadro de texto que por defecto se llama "usurname"
            contraseniaa = formLogear.cleaned_data.get("password")
            usuario = authenticate(username= nombre_usuario, password = contraseniaa) # la forma de autenticar el usuario
            if usuario is not None: # si hay algo como un usuario y contraseña,  entonces me haces un login
                login(request, usuario)
                return redirect('Habitacion')
            else:
                messages.error(request, "usuario no valido") # si no hay usuario entonce me pones este mensaje
        else:   
            messages.error(request, "informacion incorrecta")  # este else viene de arriba, si el usuario no ha ingresado los datos correctamente




   formLogear = AuthenticationForm() # con esto ya tenemos en form el formulario de login
   return render(request, "login/login.html", {"formLogear": formLogear}) # esta dos lineas de codigo es x si el usuario no le da al boton de logear, si no hace un post



