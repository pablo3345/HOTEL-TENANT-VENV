
from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required





urlpatterns = [

    path('', login_required(views.mostrarHabitacion), name="Habitacion"),
    path('modificarHabitacion', login_required(views.actualizarHabitacion), name="modificarHabitacion"),
    path('actualizarTabla/<int:id_habitacion>/', login_required(views.tabla_modificar), name="actualizarTabla"),
    path('eliminar/<int:id_habitacion>/', login_required(views.eliminarHabitacion), name="eliminar"),
   # path('habilitar_NoLimpias/<int:id_habitacion>/', login_required(views. habilitar_NoLimpias), name=" habilitar_NoLimpias"),
   # path('habilitarPost_time/<int:id_habitacion>/', login_required(views.habilitarPost_time), name="habilitarPost_time"),
    
    path('ocultarHabitacion/<int:id_habitacion>/', login_required(views.eliminar_ocultar_habitacion), name="ocultarHabitacion"),

]
