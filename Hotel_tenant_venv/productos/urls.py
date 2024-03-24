from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [

    path('',  login_required(views.guardarProveedor), name="guardarProveedor"),
    path('modificarProveedor',   login_required(views.modificar_Proveedor), name="modificarProveedor"),
    path('modificarTabla_proveedor/<int:id_proveedor>/',   login_required(views.modificarTabla_proveedor), name="modificarTabla_proveedor"),
    path('eliminarProveedor/<int:id_proveedor>/',  login_required(views.eliminarProveedor), name="eliminarProveedor"),
    path('guardarInsumos',   login_required(views.guardarInsumos), name="guardarInsumos"),
    path('modificarInsumos',   login_required(views.modificarInsumos), name="modificarInsumo"),
    path('modificarTabla_insumos/<int:id_insumos>/',   login_required(views.modificar_tabla_insumos), name="modificarTabla_insumos"),
    path('eliminarInsumo/<int:id_insumo>/',   login_required(views.eliminarInsumo), name="eliminarInsumo"),
    path('guardarProducto',  login_required(views.guardarProducto), name="guardarProducto"),
    path('modificarProducto',   login_required(views.modificarProducto), name="modificarProducto"),
    path('modificarTabla_productos/<int:id_producto>/',   login_required(views.modificar_tabla_productos), name="modificarTabla_productos"),
    path('eliminarProducto/<int:id_producto>/',   login_required(views.eliminarProducto), name="eliminarProducto"),
    
    
    
    
]