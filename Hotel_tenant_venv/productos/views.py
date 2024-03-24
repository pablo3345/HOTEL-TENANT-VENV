from django.shortcuts import render, redirect, get_object_or_404
from productos.formsProducto import ProveedoresForm, InsumosForm, ProductoPublicoForm
from django.contrib import messages
from productos.models import Proveedores, Insumos, Producto_al_publico, Agregar_productos
from contrato.models import Contrato



# Create your views here.

def guardarProveedor(request):
    
    formProvee = ProveedoresForm()
    formInsu = InsumosForm()
    formProdPubli = ProductoPublicoForm()
    
    mensaje1=""
    mensaje2=""
    #-------------------disponibilidad-------------------------------------------------------
    insumos = Insumos.objects.all()
    productos = Producto_al_publico.objects.all()
    for insumo in insumos:
        
        if insumo.disponibilidad== False:
            
            mensaje1= "hay insumos con poca disponibilidad de stock..."
    messages.error(request, mensaje1)
             
    
    
    for producto in productos:
        if producto.disponibilidad==False:
           mensaje2="hay productos con poca disponibilidad de stock..."
    messages.error(request, mensaje2)
    
    #------------------------------------------------------------------------------------
    
    if request.method=="POST":
        formProvee = ProveedoresForm(request.POST)
        
        if formProvee.is_valid():
            
            formProvee.save()
            messages.success(request, "El proveedor se guardo correctamente...")
            return redirect('modificarProveedor')
            
        else:
            messages.error(request, "El proveedor no se guardo...")
       # return redirect('guardarProveedor')
            
            
    else:
        formProvee= ProveedoresForm()
            
    
    
    
    
    
    
    
    return render(request, "productos/productos.html", {'formProveedor': formProvee, 'formInsumos': formInsu, 'formProductoPublico':formProdPubli})




def modificar_Proveedor(request):
    
    proveedores = Proveedores.objects.all()
    
    #proveedor = Proveedores.objects.get(id = id_proveedor)
    
    
    
    return render(request, "productos/modificarProveedor.html", {'proveedores': proveedores})
    
    
    
def modificarTabla_proveedor(request, id_proveedor):
    
    formProveedor= ProveedoresForm()
    
   # proveedor = Proveedores.objects.get(id = id_proveedor)
    proveedor = get_object_or_404(Proveedores, id=id_proveedor)
    
    if request.method == "POST":
        
       nombre_proveedor = request.POST.get("nombre_proveedor")
       apellido =request.POST.get("apellido")
       direccion = request.POST.get("direccion")
       telefono= request.POST.get("telefono")
       mail= request.POST.get("mail")
       nombre_empresa= request.POST.get("nombre_empresa")
       algun_otro_dato =  request.POST.get("algun_otro_dato")
       
       proveedor.nombre_proveedor= nombre_proveedor
       proveedor.apellido=apellido
       proveedor.direccion=direccion
       proveedor.telefono=telefono
       proveedor.mail=mail
       proveedor.nombre_empresa=nombre_empresa
       proveedor.algun_otro_dato=algun_otro_dato
       
       try:
           proveedor.save()
           messages.success(request, "El proveedor se actualizo correctamente...")
           return redirect('modificarProveedor')
            
       except:
            messages.error(request, "El proveedor no se actualizo...")
            return redirect('modificarProveedor')
    
    
    
    else:
        formProveedor = ProveedoresForm(instance=proveedor)
        
        
    return render(request, "productos/modificarTabla_proveedor.html", {'formProveedor': formProveedor})
   
   
def eliminarProveedor(request, id_proveedor):
    #proveedor = Proveedores.objects.get(id = id_proveedor)
    
    #proveedor = get_object_or_404(Proveedores, id=id_proveedor)
    proveedor = get_object_or_404(Proveedores, id=id_proveedor) 
    
    try:
       # if Proveedores.objects.filter(id=id_proveedor).exists():
        
         proveedor.delete()
         messages.success(request, "El proveedor se elimino correctamente...")
         #return redirect('modificarProveedor')
    
    except:
        messages.error(request, "El proveedor no se elimino...")
    return redirect('modificarProveedor')
    
    
    
    
def guardarInsumos(request):
    formProvee = ProveedoresForm()
    formInsu = InsumosForm()
    formProdPubli = ProductoPublicoForm()
    
    if request.method=="POST":
        formInsu = InsumosForm(request.POST)
        
        if formInsu.is_valid():
            
            formInsu.save()
            messages.success(request, "El insumo se guardo correctamente...")
            
            
        else:
            messages.error(request, "El insumo no se guardo...")
        return redirect('modificarInsumo')
            
            
    else:
        formInsu= InsumosForm()
            
    
    
    
    
    
    
    
    return render(request, "productos/productos.html", {'formProveedor': formProvee, 'formInsumos': formInsu, 'formProductoPublico':formProdPubli})



def modificarInsumos(request):
    
    insumos= Insumos.objects.all()
    
    
    
    return render(request, "productos/modificarInsumos.html", {'insumos': insumos})



def modificar_tabla_insumos(request, id_insumos):
    
   # insumo = Insumos.objects.get(id = id_insumos)
    insumo = get_object_or_404(Insumos, id=id_insumos)
    formInsumos = InsumosForm()
    
    
    
    
    
    
    if request.method=="POST":
        
        nombre_insumos = request.POST.get("nombre_insumos")
        marca_insumos =  request.POST.get("marca_insumos")
        precio =  request.POST.get("precio")
        medida =  request.POST.get("medida")
       
        algun_otro_dato=  request.POST.get("algun_otro_dato")
        disponibilidad =  request.POST.get("disponibilidad")
        #---------------------------------------------------
        id = request.POST.get("proveedor")
   
        proveedor_id= Proveedores.objects.get(id=id)
        #-----------------------------------------
        
        
        insumo.nombre_insumos=nombre_insumos
        insumo.marca_insumos= marca_insumos
        insumo.precio= precio
        insumo.medida= medida
        insumo.proveedor= proveedor_id
        insumo.algun_otro_dato= algun_otro_dato
        insumo.disponibilidad= disponibilidad
        
        try:
            insumo.save()
            messages.success(request, "El insumo se actualizo correctamente...")
            
        except:
             messages.error(request, "El insumo no se actualizo...")
             
        return redirect('modificarInsumo')
    
    
    
    else:
        formInsumos = InsumosForm(instance=insumo)
        
        
    return render(request, "productos/modificarTabla_Insumos.html", {'formInsumos': formInsumos})



def eliminarInsumo(request, id_insumo):
   # insumo= Insumos.objects.get(id= id_insumo) volver---atras-------------
   # insumo = get_object_or_404(Insumos, id=id_insumo)
    insumo = get_object_or_404(Insumos, id=id_insumo)
    
    
    
    try:
        #if Insumos.objects.filter(id=id_insumo).exists():
        
        
         insumo.delete()
         messages.success(request, "El insumo se elimino correctamente...")
    
    except:
         messages.error(request, "El insumo no se elimino...")
         
    return redirect('modificarInsumo')



def guardarProducto(request):
    formProvee = ProveedoresForm()
    formInsu = InsumosForm()
    formProdPubli = ProductoPublicoForm()
    
    if request.method=="POST":
        formProduc = ProductoPublicoForm(request.POST)
        
        if formProduc.is_valid():
            
            formProduc.save()
            messages.success(request, "El producto se guardo correctamente...")
            
            
        else:
            messages.error(request, "El producto no se guardo...")
        return redirect('modificarProducto')
            
            
    else:
        formProduc= ProductoPublicoForm()
            
    
    
    
    
    
    
    
    return render(request, "productos/productos.html", {'formProveedor': formProvee, 'formInsumos': formInsu, 'formProductoPublico':formProduc})


def modificarProducto(request):
    
   # productos= Producto_al_publico.objects.all()
     productos= Producto_al_publico.objects.filter(eliminado=False)
    
    
    
     return render(request, "productos/modificarProducto.html", {'productos': productos})


    
    

def modificar_tabla_productos(request, id_producto):
    
   # producto = Producto_al_publico.objects.get(id = id_producto)
    producto = get_object_or_404(Producto_al_publico, id=id_producto)
    formProducto = ProductoPublicoForm()
    
    
    if producto.eliminado == True:
          messages.error(request, "Este producto ya aparece como eliminado u oculto")
          return redirect('modificarProducto')
        
    
    
    
    if request.method=="POST":
        
        nombre_producto = request.POST.get("nombre_producto")
        marca_producto =  request.POST.get("marca_producto")
        precio_al_publico =  request.POST.get("precio_al_publico")
        precio_de_costo =  request.POST.get("precio_de_costo")
       
        medida=  request.POST.get("medida")
         #---------------------------------------------------
        id = request.POST.get("proveedor")
   
        proveedor_id= Proveedores.objects.get(id=id)
        #-----------------------------------------
        
        
        disponibilidad =  request.POST.get("disponibilidad")
        
        
        #---------------------------------------------------
       # precio_promocion = request.POST.get("precio_promocion")
        algun_otro_dato = request.POST.get("algun_otro_dato")
   
       
        
        
        producto.nombre_producto=nombre_producto
        producto.marca_producto= marca_producto
        producto.precio_al_publico= precio_al_publico
        producto.precio_de_costo= precio_de_costo
        producto.medida=medida
        producto.proveedor= proveedor_id
        producto.disponibilidad= disponibilidad
       # producto.precio_promocion= precio_promocion
        producto.algun_otro_dato= algun_otro_dato
       
        try:
            producto.save()
            messages.success(request, "El producto se actualizo correctamente...")
            
        except:
             messages.error(request, "El producto no se actualizo...")
             
       # actualizarElTotalDeAgregar(request, id_producto)
             
        return redirect('modificarProducto')
    
    
    
    else:
         formProducto =ProductoPublicoForm(instance=producto)
        
        
    return render(request, "productos/modificar_TablaProductos.html", {'formProducto': formProducto})


def eliminarProducto(request, id_producto):
    # filtrar en el formsModel si eliminado true o false para que no apareazcan en el select
    
  
    producto = get_object_or_404(Producto_al_publico, id=id_producto)
    variables_True = True
    variables_True2 = True
   
  
    try:
         producto.disponibilidad= variables_True2
        
         producto.eliminado= variables_True
         
         producto.save()
       # producto.delete()
         messages.success(request, "El producto aparece como estado eliminado...")
        
    except:
         messages.error(request, "El producto no se elimino...")
         
         
   
         
    return redirect('modificarProducto')
   
              
         
    
         
         

    
   
      
      
      
      
      
      
     
         
         
         
    
   







    
      
            
        
      

