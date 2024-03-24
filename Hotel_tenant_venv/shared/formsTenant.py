from shared.models import Client


from django import forms






class FormClient(forms.ModelForm):
    
        class Meta:
            model=Client
        
        
            fields=[
               'first_name', 
               'last_name',
               'email',
               
               'dni',
               'phone_number',
               'business_name',
               'cantidad_habitacion',
              
             
            
             
  
            
        ]
        
        
            labels={
            
               'first_name':'Nombre', 
               'last_name': 'Apellido',
              
               'email': 'email',
               'dni': 'dni',
               'phone_number': 'WhatsApp',
               'business_name': 'Nombre del establecimiento'
             
             
            
    
            
        }
        
        
            widgets={
            
               'first_name': forms.TextInput(),
                'last_name': forms.TextInput(),
                 'email': forms.EmailInput(),
              
               'dni': forms.TextInput(),
             
              
               'phone_number':forms.TextInput(),
               
                 'business_name':forms.TextInput(),
             
            
                 'cantidad_habitacion': forms.TextInput(),
            
        }
            
        
                
                
        
            
      
    
        
                
                
                
                
                
         
             