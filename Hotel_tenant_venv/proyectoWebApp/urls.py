from proyectoWebApp import views
from django.urls import path
from django.contrib.auth.decorators import login_required


urlpatterns = [

  
   # path('', views.home, name="Home"),
  
 
     path('manual_usuario/', login_required(views.manual_usuario), name="manual_usuario"),
    # path('inicio/', views.inicio, name="Inicio"),
     
     path('', views.paginaPrincipal, name="paginaPrincipal"),
     
     path('politica_privacidad/', views.politica_de_privacidad, name="Politica_privacidad"),
     
     
     path('is_active_false/', views.is_active_false, name="is_active_false"),
    
      path('quienes_somos/', views.quienes_somos, name="quienes_somos"),
    
     
   
     
    
     
  
     
     

]
#handler404 = 'proyectoWebApp.views.miError_404'
#urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #para las imagenes (media)














