from .views import VRegistro, cerrar_sesion, logear
from django.urls import path


urlpatterns = [



    path('registrarse', VRegistro.as_view(), name="Registrarse"), # as_view es para que nos muestre esta clase como una vista
    path('cerrar_sesion', cerrar_sesion, name="Cerrar_sesion"),
    path('logear', logear, name="Logear"),
  
   #---------------------------------------------------------------------
  


]
