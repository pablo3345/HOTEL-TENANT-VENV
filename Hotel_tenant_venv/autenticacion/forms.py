from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistroForms(UserCreationForm):
    class Meta:
        model =User
        fields=['username',
               
                'email',
                ]
        
        
        labels={'username': 'Nombre de usuario:',
             
                'email': 'Correo (puede colocar el mismo que anteriormente)',
                
                
                }