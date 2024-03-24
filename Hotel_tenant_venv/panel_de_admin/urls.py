from django.urls import path
from . import views 
from django.contrib.auth.decorators import login_required





urlpatterns = [

    path('',  login_required(views.mostrarPanel), name="Panel"),
    #path('mostrarDiagramas', views.mostrarDiagramas, name="mostrarDiagramas")
    
    path('colocar_diagrama',  login_required(views.colocar_diagrama), name="colocar_diagrama"),
   
   
   
]
