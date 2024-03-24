from io import BytesIO # antes de convertirlo a pdf va a pasar por un formato Bytes
from django.http import HttpResponse
from django.template.loader import get_template # como voy a a cargar una plantilla en mi vista y luego la convierto a html
#-----------------------------------
from xhtml2pdf import pisa # recien aca uso esta libreria que descargue, para html a PDF




def render_to_pdf(template_src, context_dic={}): # esta funcion significa renderzar el html a pdf (primer parametro la plantilla que voy a renderizar que se la mando desde la vista, y el segundo es el contenido que va a tener, el contexto)
    
    template = get_template(template_src) # aca le paso el template
    html = template.render(context_dic) # y aca le paso el contenido, seria el contexto
    result=BytesIO()
    pdf= pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result) # ISO-8859... es para que reconozca caracteres especiales
    
    
    if not pdf.err: # si no tiene errores el pdf
        
        return HttpResponse(result.getvalue(), content_type="application/pdf") # o sea si el pdf no tiene errores me vas a retornar el pdf
    
    return None # sino no me retornes nada, o sea si tiene errores(esto vendria a ser como el else del if)
        
        


