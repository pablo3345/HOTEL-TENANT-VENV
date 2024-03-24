from contrato.models import Contrato
from django import forms
from habitacion.models import Habitacion

from contrato.models import Huesped

class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local' 



        #-----volver atras---------------------
        
class FormContrato(forms.ModelForm):
      
    
        def __init__(self, *args, **kwargs):
                empty_label_message = 'seleccione la habitación' 
                
                empty_label_message2 = 'seleccione el huesped' 
              
               
              
                super(FormContrato, self).__init__(*args, **kwargs) # para filtrar el select de habitacion libres
                
                self.fields['habitacion'].queryset= Habitacion.objects.all().order_by('-id')
              
                
              
                
                #self.fields['habitacion'].queryset= Habitacion.objects.filter(eliminado="False")
               # self.fields['huesped'].empty_label = empty_label_message
                self.fields['huesped'].queryset= Huesped.objects.all().order_by('-id') # la otra manera es el id solo ej: order_by('id')
                
              
             #-----------------------volver atras------------------------------------------------
               
                self.fields['habitacion'].empty_label = empty_label_message
                
                self.fields['huesped'].empty_label = empty_label_message2
                
                self.fields['habitacion'].queryset= Habitacion.objects.filter(estado="Null", eliminado=False).order_by('-id')
                
               
              
                
              
               
                
             
        
                
      
      
    
        class Meta:
            model=Contrato
            
            
            
            fields=[
                'habitacion',
                'huesped',
                'fecha_entrada',
                'fecha_salida',
                #'importe_estadia',
                'importe_otros_gasto',
              
                'descuento_importe_noche',
                'descuento_total_calcularo',
                'aumento_total',
                'porcentaje_de_senia_reservas',
                #'late_chack_out'
                'total',
                'habitacion_reserva',
               # 'total_enviar_desdeReserva_a_contrato',
               
                
                
                
                
                
                
            ]
            
            labels={
                'habitacion': 'Habitaciones (libres)  habilitarlas desde el panel',
                'huesped': 'Huesped',
                'fecha_entrada': 'Fecha Entrada',
                'fecha_salida': 'Fecha Salida',
                'importe_estadia': "Importe estadia se agrega automaticamente",
                'importe_otros_gasto': 'Gastos extras (dejar en cero si no hay importe)',
              
                'descuento_importe_noche':'Hacer descuento  al precio de la habitacion por noche',
                'descuento_total_calcularo':'Hacer descuento al total calculado',
                'aumento_total': 'Hacer un aumento al total',
                'porcentaje_de_senia_reservas':'Porcentaje de la seña',
                #'late_chack_out':'Late check out',
                'total': 'Total se agrega automaticamente',
                
                'habitacion_reserva': 'Habitación reserva',
                #'total_enviar_desdeReserva_a_contrato':'total reserva contrato',
                
                
                
                
            }
            
            widgets={
                
                'habitacion':forms.Select(),
                'huesped': forms.Select(),
                'fecha_entrada':DateTimeInput(), # este DateTimeInput() viene de la clase de arriba que puse para que me muestre el widgets
                'fecha_salida': DateTimeInput(),
                'importe_estadia': forms.NumberInput(attrs={'readonly':True,'hidden': True,'required': False}),
                'importe_otros_gasto': forms.NumberInput(attrs={'placeholder':'0,00'}),
               
                'descuento_importe_noche': forms.Select(),
                'descuento_total_calcularo': forms.Select(),
                'aumento_total': forms.Select(),
                'porcentaje_de_senia_reservas': forms.NumberInput(),
               # 'late_chack_out':  forms.RadioSelect(),
                #'total': forms.NumberInput(attrs={'readonly':True,'hidden': True,'required': False})
                'total': forms.NumberInput(),
                'habitacion_reserva': forms.TextInput(),
               # 'total_enviar_desdeReserva_a_contrato': forms.NumberInput(),
               
                
                
                
                
            }
