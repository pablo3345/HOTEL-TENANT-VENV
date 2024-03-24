from django.db import models
from django_tenants.models import TenantMixin, DomainMixin

from django.http import HttpResponse








class Client(TenantMixin): #hereda de TenantMixin, esta clase Cliente puede tener los campos que yo le quiera agregar
    name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=80)
    last_name=  models.CharField(max_length=80)
    email= models.EmailField()
    email2= models.EmailField( blank=True, null=True)
    dni= models.CharField(max_length=60)
    phone_number= models.CharField(max_length=60) # ouede ser el dato segun vi por internet PhoneNumberField
    business_name= models.CharField(max_length=80) # nombre del establecimiento
    #paid_until =  models.DateField() # en ingles significa pagado hasta
    is_active = models.BooleanField()  # is_active es por ejemplo si el cliente no paga le desactivo esto en false
    created_on = models.DateField(auto_now_add=True) # me captura el momento del registro en la bbdd
    
    cantidad_habitacion= models.CharField(max_length=50)
                                        

    auto_create_schema = True  #esto es cada ves que creo un cliente me vas a guardar un esquema en la bbdd
    
  
    
    def __str__(self):
        return f'{self.name}  {self.first_name} {self.last_name} {self.dni}'
    
    
   
        
    
    
    

    
    
class Domain(DomainMixin):
    
    # is_primary significa si este es el dominio principal del tenant (True) puede tener varios dominios
    pass



    '''def servicio_desactivado():
    
       dominio=Domain()
    
       if dominio.tenant.is_active==False:
        # mensaje="El servicio fue desactivado"
        # return HttpResponse(mensaje)
        print("is_active False---------------------------------")'''
