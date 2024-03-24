from productos.models import Proveedores, Insumos, Producto_al_publico
from django import forms

class ProveedoresForm(forms.ModelForm):
    
    class Meta:
        model= Proveedores
        
        fields= [
                'nombre_proveedor',
                'apellido',
                'direccion',
                'telefono',
                'mail',
                'nombre_empresa',
                'algun_otro_dato',
            
            
                           ]
        
        labels={
                'nombre_proveedor': 'Nombre',
                'apellido': 'Apellido',
                'direccion': 'Direccion',
                'telefono': 'Telefono',
                'mail': 'email',
                'nombre_empresa': 'Nombre empresa',
                'algun_otro_dato': 'Algun otro dato'
            
            
            
        }
        
        widgets={
            
            
            'nombre_proveedor':  forms.TextInput(),
            'apellido': forms.TextInput(),
            'direccion':  forms.TextInput(),
            'telefono': forms.TextInput(),
            'mail': forms.EmailInput(),
            'nombre_empresa': forms.TextInput(),
            'algun_otro_dato':  forms.TextInput(),
        }
            
            
            
class InsumosForm(forms.ModelForm):
    
    
    def __init__(self, *args, **kwargs):
          empty_label_message = 'seleccione el proveedor' 
          super().__init__(*args, **kwargs)
          self.fields['proveedor'].empty_label = empty_label_message
          
          self.fields['proveedor'].queryset= Proveedores.objects.all().order_by('-id')
                
    
    class Meta:
        model = Insumos
        
         
       
                
        
        
        fields=[
            'nombre_insumos',
            'marca_insumos',
            'precio',
            'medida',
            'proveedor',
            'algun_otro_dato',
            'disponibilidad'
            
            
            
            
        ]
        labels ={
            
            'nombre_insumos': 'Nombre',
            'marca_insumos': 'Marca',
            'precio': 'Precio',
            'medida': 'Medida',
            'proveedor': 'Proveedor',
            'algun_otro_dato': 'Algun otro dato',
            'disponibilidad': 'Stock disponible'
            
        }
        
        widgets = {
            
            'nombre_insumos':  forms.TextInput(),
            'marca_insumos': forms.TextInput(),
            'precio': forms.NumberInput(),
            'medida':  forms.NumberInput(),
            'proveedor': forms.Select(),
            'algun_otro_dato': forms.TextInput(),
            'disponibilidad': forms.RadioSelect()
            
            
            
        }
        
class ProductoPublicoForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
          empty_label_message = 'seleccione el proveedor' 
          super().__init__(*args, **kwargs)
          self.fields['proveedor'].empty_label = empty_label_message
          
          self.fields['proveedor'].queryset= Proveedores.objects.all().order_by('-id')
             
    
    class Meta:
        model=Producto_al_publico
        
        
         
                
        
        fields= [
             'nombre_producto',
             'marca_producto', 
             'precio_al_publico', 
             'precio_de_costo', 
             'medida',
             'proveedor',
             'algun_otro_dato',  
             'disponibilidad', 
            # 'precio_promocion' 
    
        ]
        
        labels = {
            
             'nombre_producto':'Nombre',
             'marca_producto':'Marca' ,
             'precio_al_publico': 'Precio al publico',
             'precio_de_costo': 'Precio al costo', 
             'medida': 'Medida',
             'proveedor': 'Proveedor', 
             'algun_otro_dato':'Algún otro dato', 
             'disponibilidad': 'Stock disponible', 
           #  'precio_promocion': 'Precio promocion'
            
            
            
        }
        
        widgets ={
            
             'nombre_producto': forms.TextInput(),
             'marca_producto': forms.TextInput(),
             'precio_al_publico':  forms.NumberInput(),
             'precio_de_costo':  forms.NumberInput(), 
             'medida':  forms.NumberInput(),
             'proveedor':  forms.Select(),
             'algun_otro_dato': forms.TextInput(),
             'disponibilidad':  forms.RadioSelect()
            # 'precio_promocion': forms.NumberInput()
            
            
            
        }
        
        
        
    
