from django.urls import path
from . import views
#from contrato import views
from django.contrib.auth.decorators import login_required












urlpatterns = [

    path('',   login_required(views.mostrar_reserva), name="mostrar_reservas"),
    path('guardarReserva',   login_required(views.guardarReserva), name="guardarReserva"),
    path('modificarReserva',   login_required(views.modificarReservas), name="ModificarReservas"),
    path('enviarContrato/<int:id_reserva>/',   login_required(views.enviar_a_contrato), name="enviarContrato"),
    path('modificarHuespedReserva',   login_required(views.modificarHuesped), name="modificarHuespedReserva"),
    path('modificarTabla_huesped/<int:id_huesped>/',   login_required(views.modificarTabla_huesped), name="modificarTabla_huesped"),
    path('eliminarHuesped_reserva/<int:id_huesped>/',   login_required(views.eliminarHuesped_reserva), name="eliminarHuesped_reserva"),
    path('eliminarReserva/<int:id_reserva>/',   login_required(views.eliminarReserva), name="eliminarReserva"),
   # path('guardarContratoReserva', views.guardarContratoReserva, name="guardarContratoReserva")
   
    path('modificar_tabla_reserva/<int:id_reserva>/',   login_required(views.modificarTabla_reserva), name="modificar_tabla_reserva"),
    
    path('cancelarReserva/<int:id_reserva>/',   login_required(views.cancelarReserva), name="cancelarReserva"),
    path('quitar_cancelarReserva/<int:id_reserva>/',  login_required(views.quitar_cancelarReserva), name="quitar_cancelarReserva"),
    #------------------traje todo de contrato------------------------------
   # path('enviar_contrato/<int:id_reservas>/',  login_required(views.enviar_a_contrato), name="enviar_contrato"),
    path('reservas_totales',  login_required(views.reservas_totales), name="Reservas_totales"),
    
    path('mostrar_calendario',   login_required(views.calendar_events), name="Mostrar_calendario"),
    
    
    
    
    
   
    
   ]