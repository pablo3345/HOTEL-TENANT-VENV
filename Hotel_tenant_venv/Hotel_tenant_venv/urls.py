"""ProyectoWeb_hotel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404, handler500 
from contrato.views import guardarContrato
from django.contrib.auth.decorators import login_required

from contacto.views import contacto


urlpatterns = [
    path('admin/', admin.site.urls),
    path('habitacion/', include("habitacion.urls")),
    path('contrato/', include("contrato.urls")),
    path('', include("proyectoWebApp.urls")),
   # path('habitacion/', include("habitacion.urls")),
    #path('contrato/', include("contrato.urls")),
    #path('panelAdmin/', include("panel_de_admin.urls")),
   # path('productos/', include("productos.urls")),
    path('mostrarReservas/', include("reservas.urls")),
    path('autenticacion/', include("autenticacion.urls")),
    #---------los saque del tutorial de la pagina de reset password----
    
    path("autenticacion/", include("django.contrib.auth.urls")),
   
    path('guardarContrato/', login_required(guardarContrato)), #en realidad esta url estaba en contrato pero la traje aca xq la url era extensa y no me funcionaba
    path('productos/', include("productos.urls")),
    path('panelAdmin/', include("panel_de_admin.urls")),
    
    
    path('contacto/', contacto),
    
   
    
    #-------------------probar con shared haber que pasa---------------------------------
   
    
    
    
]
handler404 = 'proyectoWebApp.views.miError_404'
handler500 = 'proyectoWebApp.views.miError_500'



