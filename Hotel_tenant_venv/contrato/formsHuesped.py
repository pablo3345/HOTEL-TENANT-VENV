from contrato.models import Huesped
from django import forms


class FormHuesped(forms.ModelForm):
    
        class Meta:
            model=Huesped
        
        
            fields=[
               'nombre_responsable', 
               'apellido',
               'edad',
               'dni',
               'direccion',
               'localidad',
               'codigo_postal',
               'pais',
               'telefono',
               'demas_huespedes',
               'patente_vehiculo',
               'modelo_vehiculo',
               'correo_electronico',
               #'penalidad'
    
  
            
        ]
        
        
            labels={
            
               'nombre_responsable':'Nombre responsable', 
               'apellido': 'Apellido',
               'edad': 'Edad',
               'dni': 'DNI',
               'direccion': 'Direccion',
               'localidad': 'Localidad',
               'codigo_postal': 'Codigo Postal',
               'pais': 'Pais',
               'telefono': 'Telefono',
               'demas_huespedes': 'Demas huespedes',
               'patente_vehiculo': 'Patente vehiculo',
               'modelo_vehiculo': 'Modelo vehiculo',
               'correo_electronico': 'Email',
              # 'penalidad': 'Penalidad'
            
            
    
            
        }
        
        
            widgets={
            
               'nombre_responsable': forms.TextInput(),
               'apellido':  forms.TextInput(),
               'edad':  forms.NumberInput(),
               'dni': forms.TextInput(),
               'direccion': forms.TextInput(),
               'localidad': forms.TextInput(),
               'codigo_postal': forms.TextInput(),
               'pais': forms.TextInput(),
               'telefono':forms.TextInput(),
               
               'demas_huespedes': forms.Textarea(attrs={'placeholder':'puede poner DNI, nombre, apellido, direccion'}),
               'patente_vehiculo': forms.TextInput(),
               'modelo_vehiculo':  forms.TextInput(),
               'correo_electronico': forms.EmailInput(),
              # 'penalidad': forms.RadioSelect()
               
            
            
            
            
        }
        