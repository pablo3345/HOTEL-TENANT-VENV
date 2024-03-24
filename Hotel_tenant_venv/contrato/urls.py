
from django.urls import path
from . import views
from .views import generar_reporter_huespedes
from django.contrib.auth.decorators import login_required










urlpatterns = [

    path('', login_required(views.mostrarContrato), name="Contrato"), #contrato es la url que le pase al nav del padre a los botones
    #path('guardarHuesped', views.mostrarContrato, name="guardarHuesped"),
    path('modificarHuesped', login_required(views.modificarHuesped), name="modificarHuesped"),
    path('modificarTablaHuesped/<int:id_huesped>/', login_required(views.modificarTablaHuesped), name="modificarTablaHuesped"),
    path('eliminarHuesped/<int:id_huesped>/', login_required(views.eliminarHuesped), name="eliminarHuesped"),
   # path('guardarContrato/', login_required(views.guardarContrato), name="guardarContrato"),
    path('modificarContrato', login_required(views.modificarContrato), name="modificarContrato"),
    path('modificarTablaContrato/<int:id_contrato>/', login_required(views.modificarTablaContrato), name="modificarTablaContrato"),
    path('eliminarContrato/<int:id_contrato>/', login_required(views.eliminarContrato), name="eliminarContrato"),
    path('calcularTotal', login_required(views.calcularTotal), name="calcularTotal"),
    path('habilitar_ocupadas/<int:id_habitacion>/', login_required(views.habilitar_ocupadas), name="habilitar_ocupadas"), # para hablitar las habitaciones ocupadas
    path('late_check/<int:id_contrato>/', login_required(views.lateCheckout), name="late_check"),
    path('contratosTotales', login_required(views.contratosTotales), name="contratosTotales"),
    path('generarReportes/<int:id>/', generar_reporter_huespedes.as_view(), name="generarReportes"),
   # path('generarReportes/<int:id_huesped>/', views.generar_reporter_huesped, name="generarReportes")
    path('cambiarTotal/<int:id_contrato>/',login_required(views.cambiar_total), name="cambiarTotal"),
    path('penalidad/<int:id_huesped>/', login_required(views.penalidad), name="Penalidad"),
    path('quitar_penalidad/<int:id_huesped>/', login_required(views.quitar_penalidad), name="quitar_penalidad"),
    path('AgregarProductos/<int:id_contrato>/', login_required(views.agregar_Producto), name="AgregarProductos"),
    path('eliminarAgregar/<int:id_agregar>/', login_required(views.eliminarAgregar), name="EliminarAgregar"),

   #--------------------------------------------------------------------------------
    path('recibir_id/<int:id_reservas>/', views.recibir_id_reserva, name="recibir_id"),
    
    path('huesped_reserva/<int:id_reservas>/', login_required(views.mostrarContrato_reservas), name="huesped_Reserva"),
    
   # path('pasarSelect/', login_required(views.pasar_select), name="pasarSelect"),
   
    path('habilitar_ocupadas_tabla_contrato/<int:id_habitacion>/', login_required(views.habilitar_habitaciones_tabla_contrato), name="habilitar_ocupadas_tabla_contrato"),
   
]
