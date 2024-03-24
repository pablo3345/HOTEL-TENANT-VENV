from habitacion.models import Habitacion
from django import forms

class FormsHabitacion(forms.ModelForm):

    class Meta:
        model = Habitacion

        fields = [  # aca en esta tupla ponemos los campos del modelo que queremos utilizar

            'nombre_numero',
            'piso',
            'capacidad',
            'precio_por_noche',
            'camita_bebe',
           # 'esta_limpia',
            'posee_heladera',
            'posee_aire_acondicionado',
            'posee_calefaccion',
            'posee_ventana',
            'posee_cama_matrimonial',
            'posee_televisor',
            'posee_wifi',
            'jacuzzi',
            'posee_microondas',
            'check_out_lates',
            'otro_dato'
           
            #'predio_con_pileta'
             # 'estado_libre',
             # 'estado_ocupado',
             # 'estado_post_ocupado',

        ]

        labels = {  # aca en este diccionario pongo las etiqetas que quiero que tengan los textxField en el html

            'nombre_numero': 'Nombre o numero',
            'piso': 'Piso',
            'capacidad': 'Capacidad de personas',
            'precio_por_noche': 'Precio por noche',
            'camita_bebe': 'Posee camita bebe',
           # 'esta_limpia': 'Esta limpia y preparada',
            'posee_heladera': 'Posee frigobar',
            'posee_aire_acondicionado': 'Posee aire acondicionado',
            'posee_calefaccion': 'Posee calefaccion',
            'posee_ventana': 'Posee ventana',
            'posee_cama_matrimonial': 'Posee cama matrimonial',
            'posee_televisor': 'Posee televisor',
            'posee_wifi': 'Posee wifi',
            'jacuzzi': 'Posee jacuzzi',
            'posee_microondas': 'Posee microondas',
            'check_out_lates': 'Precio late check out',
            'otro_dato': 'Agregar otro dato'
           # 'predio_con_pileta': 'Predio con pileta *'
            # 'estado_libre': 'Disponible:',
            # 'estado_ocupado': 'Ocupada:',
            # 'estado_post_ocupado':'Plazo vencido:',

        }

        widgets = {  # lo que se va a ver en el formulario del html
            'nombre_numero': forms.TextInput(),
            'piso': forms.Select(),
            'capacidad': forms.Select(),
            'precio_por_noche': forms.NumberInput(attrs={'placeholder':'0,00'}),

            'camita_bebe': forms.RadioSelect(),

           # 'esta_limpia': forms.RadioSelect(),
            'posee_heladera': forms.RadioSelect(),
            'posee_aire_acondicionado': forms.RadioSelect(),
            'posee_calefaccion':forms.RadioSelect(),
            'posee_ventana':forms.RadioSelect(),
            'posee_cama_matrimonial': forms.RadioSelect(),
            'posee_televisor': forms.RadioSelect(),
            'posee_wifi': forms.RadioSelect(),
            'jacuzzi': forms.RadioSelect(),
            'posee_microondas': forms.RadioSelect(),
            'check_out_lates': forms.NumberInput(attrs={'placeholder':'0,00'}),
            'otro_dato': forms.TextInput()
           # 'predio_con_pileta': forms.RadioSelect(),
            # 'estado_libre':  forms.FileInput(),
            # 'estado_ocupado': forms.FileInput(),
            # 'estado_post_ocupado': forms.FileInput(),

        # attrs={'class':"form-check-input"} poner en () ejemplo TextInput() seria la clase de bootdtrap
        # attrs={'placeholder':'Phone Number'} poner esto en el text input en gris pero que se puede escribir arriba de la palabra
        }