from productos.models import Agregar_productos
from django import forms
from productos.models import Producto_al_publico


class FormsProductos_agregados(forms.ModelForm):
    def __init__(self, *args, **kwargs):
                super(FormsProductos_agregados, self).__init__(*args, **kwargs) # para filtrar el select de habitacion libres
                self.fields['producto'].queryset= Producto_al_publico.objects.filter(eliminado=False)
                
                
    
    class Meta():
        
     model= Agregar_productos
        
     fields=[
        
        'producto',
        'contrato',
        'cantidad',
        'total'
    ]
    
    
     labels={
        
        'producto': 'Producto',
        'contrato': 'Huesped del contrato',
        'cantidad': 'Cantidad',
        'total': 'Total'
        
        
    }
    
     widgets={
        
        'producto': forms.Select(),
        'contrato': forms.Select(),
        'cantidad': forms.NumberInput(attrs={'placeholder':'0'}),
        'total': forms.NumberInput(attrs={'readonly':True,'hidden': True,'required': False})
        
        
        
    }
    
    