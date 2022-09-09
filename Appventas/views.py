
from http.client import HTTPResponse
from msilib.schema import ListView
from django.shortcuts import redirect
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render
from .carrito import carrito
from Appventas.models import About, accesorios, bicicletas, categorias, empleado, indumentarias, repuestos, EnviarMensaje
from Appventas.forms import AvatarFormulario, AccesoriosFormularios, BicicletasFormularios, FormularioMensaje, IndumentariasFormularios, RepuestosFormularios, categoriasFormulario, empleadosFormulario, enviarMensaje, FormularioMensaje, CrearUsuario
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm , UserChangeForm

from django.contrib.auth import login,authenticate
from django.contrib.auth.mixins import LoginRequiredMixin #solo funciona con las vistas basadas en clases
from django.contrib.auth.decorators import login_required#decorador para vistas basadas en funciones.Aumenta la funcionalidad de una funcion.

# Views de simple acceso
#imports para el chat:

#-----------------------------------------------
from queue import Empty
from django.conf import settings
from django.core.mail import EmailMessage
from django.core.mail import EmailMessage# Toma un temaplate html  
from django.template.loader import render_to_string # transformado en un string
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from Appventas.carrito import carrito
from Appventas.models import  Avatar, EnviarMensaje, categorias
from Appventas.forms import   EditarUsuario, categoriasFormulario
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash

from django.contrib.auth.decorators import login_required#decorador para vistas basadas en funciones.Aumenta la funcionalidad de una funcion.
# Views de simple acceso
def ViewPadre(request):
    return render (request,"Padre.html")

def Nosotros(request):#Template de Nostros
   about=About.objects.all()
   
   try:
    avatar=Avatar.objects.filter(user=request.user.id)                    
    filtro=len(avatar)-1
    
    return render(request, "QuienesSomos.html",{"url":avatar[filtro].imagen.url,"about0":about[0].imagen.url,"about1":about[1].imagen.url})
   except:
    return render(request, "QuienesSomos.html",{"about0":about[0].imagen.url,"about1":about[1].imagen.url})

def inicio(request):#Template de Inivcio
    carr = carrito(request)
    categoria = categorias.objects.all()
    try:
        avatar=Avatar.objects.filter(user=request.user.id)   
        filtro=len(avatar)-1                 #en el registro avatar, en la propiedad imagen, en el campo tipo imagen adentro tiene un url
        return render(request, "Formularios.html", {"categorias": categoria,"url":avatar[filtro].imagen.url})
    except:
        return render(request, "Formularios.html",{ "categorias": categoria})
   

def tienda(request):
    bicicleta=bicicletas.objects.all()
    indumentaria=indumentarias.objects.all()
    accesorio=accesorios.objects.all()
    repuesto=repuestos.objects.all()
    #Paginador, se selecciona la cantidad de productos a mostrar por pagina y se coloca que muestre como predeterminada la pagina 1
    try:
     pagina = request.GET.get("page", 1)
     paginatorBici = Paginator(bicicleta, 1)
     bicicleta = paginatorBici.page(pagina)
     paginatorIndu = Paginator(indumentaria, 1)
     indumentaria = paginatorIndu.page(pagina)
     paginatorAcc = Paginator(accesorio, 1)
     accesorio = paginatorAcc.page(pagina)
     paginatorRepu = Paginator(repuesto, 1)
     repuesto = paginatorRepu.page(pagina)
     
    except:
        raise Http404
    
    return render(request, "tienda.html",{"bicicletas": bicicleta, "paginatorBici": paginatorBici,  "indumentarias": indumentaria, "accesorios": accesorio, "repuestos": repuesto})

def tiendabici(request):
    bicicleta=bicicletas.objects.all()
    try:
        avatar=Avatar.objects.filter(user=request.user.id)   
        filtro=len(avatar)-1
        return render(request, "tienda.html",{ "bicicletas": bicicleta,"url":avatar[filtro].imagen.url})
    except:
        return render(request, "tienda.html",{ "bicicletas": bicicleta})

def tiendarepuestos(request):
    repuesto=repuestos.objects.all()
    try:
        avatar=Avatar.objects.filter(user=request.user.id)   
        filtro=len(avatar)-1
        return render(request, "tienda.html",{ "repuestos": repuesto,"url":avatar[filtro].imagen.url})
    except:
        return render(request, "tienda.html",{ "repuestos": repuesto})


def tiendaaccesorios(request):
    accesorio=accesorios.objects.all()
    try:
        avatar=Avatar.objects.filter(user=request.user.id)   
        filtro=len(avatar)-1
        return render(request, "tienda.html",{ "accesorios": accesorio,"url":avatar[filtro].imagen.url}) 
    except:
        return render(request, "tienda.html",{ "accesorios": accesorio})

def tiendaindumentaria(request):
    indumentaria=indumentarias.objects.all()
    try:
        avatar=Avatar.objects.filter(user=request.user.id)   
        filtro=len(avatar)-1
        return render(request, "tienda.html",{"indumentarias": indumentaria,"url":avatar[filtro].imagen.url})
    except:
        return render(request, "tienda.html",{"indumentarias": indumentaria})
       
    
#Carrito de compras
@login_required
def agregar_bicicleta(request, producto_id):
    carr = carrito(request)                    
    productos = bicicletas.objects.get(id = producto_id)
    carr.agregar(producto=productos)
    return redirect("Tienda")
@login_required
def agregar_repuesto(request, producto_id):
    carr = carrito(request)                    
    productos = repuestos.objects.get(id = producto_id)
    carr.agregar(producto=productos)
    return redirect("Tienda")
@login_required
def agregar_accesorio(request, producto_id):
    carr = carrito(request)                    
    productos = accesorios.objects.get(id = producto_id)
    carr.agregar(producto=productos)
    return redirect("Tienda")
@login_required
def agregar_indumentaria(request, producto_id):
    carr = carrito(request)                    
    productos = indumentarias.objects.get(id = producto_id)
    carr.agregar(producto=productos)
    return redirect("Tienda")
@login_required
def eliminar_producto(request, producto_id):
    carr= carrito(request)
    productos = bicicletas,indumentarias,accesorios,repuestos.objects.get(id = producto_id)
    carr.eliminar(productos)
    return redirect("Tienda")
@login_required
def restar_bicicleta(request, producto_id):
    carr= carrito(request)
    productos = bicicletas.objects.get(id = producto_id)
    carr.restar(productos)
    return redirect("Tienda")
@login_required
def restar_repuesto(request, producto_id):
    carr= carrito(request)
    productos = repuestos.objects.get(id = producto_id)
    carr.restar(productos)
    return redirect("Tienda")
@login_required
def restar_accesorio(request, producto_id):
    carr= carrito(request)
    productos = accesorios.objects.get(id = producto_id)
    carr.restar(productos)
    return redirect("Tienda")
@login_required
def restar_indumentaria(request, producto_id):
    carr= carrito(request)
    productos = indumentarias.objects.get(id = producto_id)
    carr.restar(productos)
    return redirect("Tienda")
@login_required
def limpiar_carrito(request):
    carr= carrito(request)
    carr.limpiar()
    return redirect("Tienda")


def Save(request):#Template de confirmacion de guardado.

    return render(request, "Save.html")



#Formularios

@login_required
def Formulariocategoria(request):#Template cargar una bici en la tabla

    if request.method == 'POST':
        Categoriaformulario=categoriasFormulario(request.POST)
     

        if Categoriaformulario.is_valid():
            print("Entro al 2° if")
            data=Categoriaformulario.cleaned_data
            #En la tabla que creo con la clase le cargo los datos del formulario de Django
            categoria=categorias(nombre=data['Nombre'])
            categoria.save()
            return render(request, "Save.html")

    else:
        Categoriaformulario=categoriasFormulario()
        return render(request,"FormularioCategoria.html", {"CategoriaFormulario": Categoriaformulario})


@login_required
def Formulariobicis(request):#Template cargar una bici en la tabla

    if request.method == 'POST':
        BiciFormulario=BicicletasFormularios(request.POST, files=request.FILES)

        if BiciFormulario.is_valid():
            print("Entro al 2° if")
            data=BiciFormulario.cleaned_data
            #En la tabla que creo con la clase le cargo los datos del formulario de Django
            bici=bicicletas( marca=data['Marca'],modelo=data['Modelo'],tipo=data["Tipo"],rodado=data['Rodado'],color=data['Color'],precio=data['Precio'],categoria=data['Categoria'],nombre=data['Nombre'],descripcion=data['Descripcion'],imagen=data['Imagen'])
            bici.save()
            return render(request, "Save.html")
    else:
        BiciFormulario=BicicletasFormularios()
        return render(request,"FormularioBicicletas.html", {"BiciFormulario": BiciFormulario})

@login_required
def Formularioindumentarias(request):#Template cargar una indumentaria en la tabla

    if request.method == 'POST':
        InduFormulario=IndumentariasFormularios(request.POST, files=request.FILES) 

        if InduFormulario.is_valid():
            data=InduFormulario.cleaned_data
            Indu=indumentarias(tipo=data['Tipo'],marca=data['Marca'],talle=data['Talle'],precio=data['Precio'],nombre=data['Nombre'],descripcion=data['Descripcion'],categoria=data['Categoria'],imagen=data['Imagen'])
            Indu.save()
            return render(request, "Save.html")
    else:
        InduFormulario=IndumentariasFormularios()
        return render(request,"FormularioIndumentaria.html", {"IndumentariaFormularios": InduFormulario})

@login_required
def Formulariorepuestos(request):#Template cargar un repuesto en la tabla

    if request.method == 'POST':
        RepuFormulario=RepuestosFormularios(request.POST, files = request.FILES)
        if RepuFormulario.is_valid():
            data=RepuFormulario.cleaned_data         
            repuesto=repuestos(nombre=data['Nombre'], marca=data['Marca'],descripcion=data['Descripcion'],precio=data['Precio'],categoria=data['Categoria'],imagen=data['Imagen'])
            repuesto.save()
            return render(request, "Save.html")
    else:
        RepuFormulario=RepuestosFormularios()
        return render(request,"FormularioRepuestos.html", {"RepuestosFormularios":RepuFormulario})

@login_required
def Formularioaccesorios(request):#Template cargar un repuesto en la tabla

    if request.method == 'POST':
        AccFormulario=AccesoriosFormularios(request.POST, files=request.FILES)

        if AccFormulario.is_valid():
            print("Entro al 2° if")
            data=AccFormulario.cleaned_data
            #En la tabla que creo con la clase (models) le cargo los datos del formulario de Django(forms)
                     #models.py   (como se lee esto?: tipo=data['Tipo'])          
            repuesto=accesorios(nombre=data['Nombre'],tipo=data['Tipo'],marca=data['Marca'],precio=data['Precio'],descripcion=data['Descripcion'],categoria=data['Categoria'],imagen=data['Imagen'])
            repuesto.save()
            return render(request, "Save.html")
        else:
            return render (request,"FormularioAccesorios.html")
    else:
        AccFormulario=AccesoriosFormularios()
        return render(request,"FormularioAccesorios.html", {"AccesorioFormularios":AccFormulario})   


#VER FORMULARIOS
@login_required
def LeerCategoria(request):
    print("method:", request.method) #Va  a imprimir por terminal el método que utilizamos. 

    FormularioCategorias=categorias.objects.all()
    
    try:
        avatar=Avatar.objects.filter(user=request.user.id)   
        filtro=len(avatar)-1 
        return render (request, "VerFormulario_Categorias.html",{"Categorias":FormularioCategorias,"url":avatar[filtro].imagen.url})
    except:
        return render (request, "VerFormulario_Categorias.html",{"Categorias":FormularioCategorias})
@login_required
def LeerBicis (request):
    print("method:", request.method) #Va  a imprimir por terminal el método que utilizamos. 

    FormularioBicicletas=bicicletas.objects.all()
    
    try:
        avatar=Avatar.objects.filter(user=request.user.id)   
        filtro=len(avatar)-1
        return render (request, "VerFormulario_Bicicletas.html",{"Bicicletas":FormularioBicicletas,"url":avatar[filtro].imagen.url})
    except:
        return render (request, "VerFormulario_Bicicletas.html",{"Bicicletas":FormularioBicicletas})
@login_required
def LeerRepu (request):
    print("method:", request.method) #Va  a imprimir por terminal el método que utilizamos. 

    FormularioRepuestos=repuestos.objects.all()
    
    try:
        avatar=Avatar.objects.filter(user=request.user.id)   
        filtro=len(avatar)-1
        return render (request, "VerFormulario_Repuestos.html",{"Repuestos":FormularioRepuestos,"url":avatar[filtro].imagen.url})
    except:
        return render (request, "VerFormulario_Repuestos.html",{"Repuestos":FormularioRepuestos})

@login_required
def LeerIndum (request):
   

    FormularioIndumentaria=indumentarias.objects.all()
   
    try:
        avatar=Avatar.objects.filter(user=request.user.id)   
        filtro=len(avatar)-1
        return render (request, "VerFormulario_Indumentaria.html",{"Indumentaria":FormularioIndumentaria,"url":avatar[filtro].imagen.url})
    except:
         return render (request, "VerFormulario_Indumentaria.html",{"Indumentaria":FormularioIndumentaria})

@login_required
def LeerAcc (request):
    

    FormularioAccesorios=accesorios.objects.all()
    
    try:
        avatar=Avatar.objects.filter(user=request.user.id)   
        filtro=len(avatar)-1
        return render (request, "VerFormulario_Accesorios.html",{"Accesorios":FormularioAccesorios,"url":avatar[filtro].imagen.url})
    except:
        return render (request, "VerFormulario_Accesorios.html",{"Accesorios":FormularioAccesorios})

@login_required
def LeerEmpleado (request):
    print("method:", request.method) #Va  a imprimir por terminal el método que utilizamos. 
    try:
        if request.user.empleado:
          empleadoForm=empleado.objects.all()
          
          avatar=Avatar.objects.filter(user=request.user.id)   
          filtro=len(avatar)-1
          return render (request, "VerFormulario_Empleados.html",{"Empleados":empleadoForm,"url":avatar[filtro].imagen.url})

        else:
            return render (request, "Formularios.html")

    except:
        return render (request, "Formularios.html")

#BUSQUEDA BICIS
@login_required
def Busquedabicis(request):

    return render (request, "BusquedaBici.html")
@login_required
def ResultBici(request):

    if request.GET["nombre"]: 
       
        nombre=request.GET["nombre"]
      
        nombres=bicicletas.objects.filter(nombre__icontains=nombre)
        
        return render (request,"BusquedaBicicleta.html", {"nombre": nombre , "nombres":nombres})
    else:
       
        respuesta="No enviaste datos"
        return render(respuesta,"BusquedaBicicleta.html")
    

#BUSQUEDA INDUMENTARIA
@login_required
def BusquedaIndu(request):

    return render (request, "BusquedaIndu.html")
@login_required
def ResultIndu(request):
    print(request.GET)

    if request.GET["tipo"]: 
        
        tipo=request.GET["tipo"]
        
        tipos=indumentarias.objects.filter(tipo__icontains=tipo)
        
        return render (request,"BusquedaIndumentaria.html", {"tipos": tipos ,"tipo":tipo})
    else:
        
        respuesta="No enviaste datos"
        return render(respuesta,"BusquedaIndumentaria.html")
 

#BUSQUEDA RESPUESTO
@login_required
def BusquedaRepues(request):

    return render (request, "BusquedaRepu.html")
@login_required
def ResultRepues(request):
    print(request.GET)

    if request.GET["tipo"]: 
        
        tipo=request.GET["tipo"]
        
        tipos = repuestos.objects.filter(tipo__icontains=tipo)
        
        return render (request,"BusquedaRepuesto.html", {"tipos": tipos , "tipo":tipo})
    else:
        
        respuesta="No enviaste datos"
        return render(respuesta,"BusquedaRepuesto.html")
    
#BUSQUEDA ACCESORIOS
@login_required
def BusquedaAcc(request):

    return render (request, "BusquedaAcc.html")
@login_required
def ResultAcc(request):
    print(request.GET)

    if request.GET["tipo"]: 
        
        tipo=request.GET["tipo"]
       
        tipos=accesorios.objects.filter(tipo__icontains=tipo)
        
        return render (request,"BusquedaAccesorios.html", {"tipos": tipos , "tipo":tipo})
    else:
        
        respuesta="No enviaste datos"
        return render(respuesta,"BusquedaAccesorios.html")

#ELIMINAR DATOS

@login_required
def EliminarEmpleado(request, id):

    if request.method == "POST":


       empleados = empleado.objects.get(id = id)
       empleados.delete()

       #vuelvo al menu
       empleados = categorias.objects.all() #trae todas las bicicletas

       contexto = {"empleados" : empleados}
 
       return render (request, "VerFormulario_Empleados.html", contexto)

@login_required
def eliminarcategoria(request, id):

    if request.method == "POST":


       categoria = categorias.objects.get(id = id)
       categoria.delete()

       #vuelvo al menu
       categoria = categorias.objects.all() #trae todas las bicicletas

       contexto = {"categorias" : categoria}
 
       return render (request, "VerFormulario_Bicicletas.html", contexto)
@login_required
def eliminarbici(request, id):

    if request.method == "POST":


       bicicleta = bicicletas.objects.get(id = id)
       bicicleta.delete()

       #vuelvo al menu
       bicicleta = bicicletas.objects.all() #trae todas las bicicletas

       contexto = {"bicicletas" : bicicleta}
 
       return render (request, "VerFormulario_Bicicletas.html", contexto)
@login_required
def eliminarIndumentaria(request, id):

    if request.method == "POST":


       indumentaria = indumentarias.objects.get(id = id)
       indumentaria.delete()

       #vuelvo al menu
       Indumentaria = indumentarias.objects.all() 

       contexto = {"indumentaria" : Indumentaria}
 
       return render (request, "VerFormulario_Indumentaria.html", contexto)
@login_required
def eliminarrepuestos(request, id):

    if request.method == "POST":


       repuesto = repuestos.objects.get(id = id)
       repuesto.delete()

       #vuelvo al menu
       repuesto = repuestos.objects.all() #trae todas las bicicletas

       contexto = {"Repuestos" : repuesto}
 
       return render (request, "VerFormulario_Repuestos.html", contexto)
@login_required
def eliminaraccesorios(request, id):

    if request.method == "POST":


       accesorio = accesorios.objects.get(id = id)
       accesorio.delete()

       #vuelvo al menu
       accesorio = accesorios.objects.all() #trae todas las bicicletas

       contexto = {"Accesorios" : accesorio}
 
       return render (request, "VerFormulario_Accesorios.html", contexto)

#EDITAR

@login_required
def EditarEmpleado(request, id):

    empleados = empleado.objects.get(id = id)

    if request.method == 'POST':

        
        EmpleadoForm=empleadosFormulario(request.POST)

        

        if EmpleadoForm.is_valid():
            
            data=EmpleadoForm.cleaned_data
            

            empleados.nombre = data["Nombre"]
            empleados.apellido = data["Apellido"]
            empleados.telefono = data["Telefono"]
            empleados.cargo = data["Cargo"]
            empleados.email = data["Email"]

            empleados.save()
        return render(request, "Save.html")
    
    else:
        empleadoForm=empleadosFormulario(initial={
            "Nombre": empleados.nombre,
            "Apellido": empleados.apellido,
            "Telefono": empleados.telefono,
            "Cargo": empleados.cargo,
            "Email": empleados.email,
             })
        
        return render(request,"EditarEmpleados.html", {"EmpleadosForm": empleadoForm , "id": id})


@login_required
def editarcategoria(request, id):

    categoria = categorias.objects.get(id = id)

    if request.method == 'POST':

        CatFormulario=categoriasFormulario(request.POST)

        if CatFormulario.is_valid():
            print("Entro al 2° if")
            data=CatFormulario.cleaned_data
        
            categoria.nombre = data["Nombre"]

            categoria.save()
            return render(request, "Save.html")
    
    else:
        CatFormulario=categoriasFormulario(initial={
            "nombre": categoria.nombre,
        })
        return render(request,"EditarCategorias.html", {"Catformulario": CatFormulario , "id": id})
@login_required
def editarbicis(request, id):

    bicicleta = bicicletas.objects.get(id = id)

    if request.method == 'POST':

        BiciFormulario=BicicletasFormularios(request.POST, request.FILES)

        if BiciFormulario.is_valid():
            
            data=BiciFormulario.cleaned_data
        
            bicicleta.nombre = data["Nombre"],
            bicicleta.categoria = data["Categoria"],
            bicicleta.tipo = data["Tipo"],
            bicicleta.marca = data ["Marca"],
            bicicleta.modelo = data ["Modelo"],
            bicicleta.rodado = data ["Rodado"],
            bicicleta.color = data ["Color"],
            bicicleta.descripcion = data ["Descripcion"],
            bicicleta.precio = data ["Precio"],
            bicicleta.imagen = data ["Imagen"],
            
            bicicleta.save()
            
        return render (request, "Save.html")
    
    else:
        BiciFormulario=BicicletasFormularios(initial={
            "Nombre": bicicleta.nombre,
            "Categoria": bicicleta.categoria,
            "Tipo": bicicleta.tipo,
            "Marca": bicicleta.marca,
            "Modelo": bicicleta.modelo,
            "Rodado": bicicleta.rodado,
            "Color": bicicleta.color,
            "Descripcion": bicicleta.descripcion,
            "Precio": bicicleta.precio,
            "Imagen": bicicleta.imagen
            
             }) 
        return render(request,"EditarBicicletas.html", {"BiciFormulario": BiciFormulario , "id": id })

@login_required
def editarrepuestos(request, id):

    repuesto = repuestos.objects.get(id = id)

    if request.method == 'POST':
        
        repuFormulario=RepuestosFormularios(request.POST, files=request.FILES)

        if repuFormulario.is_valid():
            print("Entro al 2° if")
            data=repuFormulario.cleaned_data
        
            repuesto.nombre = data ["Nombre"]
            repuesto.categoria = data["Categoria"]
            repuesto.marca = data ["Marca"]
            repuesto.modelo = data ["Modelo"]
            repuesto.descripcion = data ["Descripcion"]
            repuesto.precio = data ["Precio"]
            repuesto.imagen = data ["Imagen"]

            repuesto.save()
        return render(request, "Save.html")
    
    else:
        repuFormulario=RepuestosFormularios(initial={
            "Nombre": repuesto.nombre,
            "Categoria": repuesto.categoria,
            "Marca": repuesto.marca,
            "Descripcion": repuesto.descripcion,
            "Precio": repuesto.precio,
            "Imagen": repuesto.imagen,
        })
        return render(request,"EditarRepuestos.html", {"RepuFormulario": repuFormulario , "id": repuesto.id})
@login_required
def editarindumentaria(request, id):

    indument = indumentarias.objects.get(id = id)

    if request.method == 'POST':
        
        induFormulario=IndumentariasFormularios(request.POST, files=request.FILES)

        if induFormulario.is_valid():
            print("Entro al 2° if")
            data=induFormulario.cleaned_data
        
            indument.nombre = data ["Nombre"]
            indument.categoria = data["Categoria"]
            indument.marca = data ["Marca"]
            indument.descripcion = data ["Descripcion"]
            indument.precio = data ["Precio"]
            indument.tipo = data ["Tipo"]
            indument.talle = data ["Talle"]
            indument.imagen = data ["Imagen"]

            indument.save()
        return render(request, "Save.html")
    
    else:
        induFormulario=IndumentariasFormularios(initial={
            "Nombre": indument.nombre,
            "Categoria": indument.categoria,
            "Marca": indument.marca,
            "Tipo": indument.tipo,
            "Talle":indument.talle,
            "Descripcion": indument.descripcion,
            "Precio": indument.precio,
            "Imagen": indument.imagen,
             })
        return render(request,"EditarIndumentaria.html", {"InduFormulario": induFormulario , "id": indument.id})

@login_required
def editaraccesorios(request, id):

    acc = accesorios.objects.get(id = id)

    if request.method == 'POST':
        
        accFormulario=AccesoriosFormularios(request.POST, files=request.FILES)

        if accFormulario.is_valid():
           
            data=accFormulario.cleaned_data
        
            acc.nombre = data ["Nombre"]
            acc.categoria = data ["Categoria"]
            acc.marca = data ["Marca"]
            acc.descripcion = data ["Descripcion"]
            acc.precio = data ["Precio"]
         

            acc.save()
        return render(request, "Save.html")
    
    else:
        accFormulario=AccesoriosFormularios(initial={
            "nombre": acc.nombre,
            "categoria": acc.categoria,
            "marca": acc.marca,
            "descripcion": acc.descripcion,
            "precio": acc.precio,
        })
        return render(request,"EditarAccesorios.html", {"AccFormulario": accFormulario , "id": acc.id})


#LOGIN
def iniciar_sesion(request):

    if request.method == "POST":
        print("Entro al metodo: ",request.method)
        form=AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            print("Entro al is valid")
            usuario=form.cleaned_data.get('username')
            clave=form.cleaned_data.get('password')

            user=authenticate(username=usuario,password=clave)

            if user is not None:
                print("Entro al is not none")
                login(request,user)

                return render(request, "Formularios.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                print("Entro al is not none ELSE")
                form = AuthenticationForm()
                return render (request, "Login.html", {"mensaje":"Error!",'form':form}) 
        else:
                print("Entro al is valid ELSE")
                form = AuthenticationForm()
                return render (request, "Login.html", {"mensaje":"Error, datos incorrectos. \n Vuelva a intentarlo.",'form':form}) 
    else:
        print("Entro al metodo GET: ",request.method)
        form = AuthenticationForm()
        return render (request, "Login.html", {'form':form})

 #Crear empleados
def CrearEmpleado(request):

    if request.method == 'POST':

        info = request.POST                            #Se crea variable para traer toda la informacion
        EmpleadoForm=empleadosFormulario({             #Se crea formulario 
            "Nombre": info["Nombre"],
            "Apellido": info["Apellido"],
            "Telefono": info["Telefono"],
            "Email": info["Email"],
            "Cargo": info["Cargo"]
            })  

        userform = UserCreationForm({                  #Se crea formulario
            "username": info["username"],
            "password1": info["password1"],
            "password2": info["password2"],
            })                      
                         
            #Validar datos de ambos
        if EmpleadoForm.is_valid() and userform.is_valid():        #Se tiene que agregar mas keys al dicccionario para mostrar empleados y usuario
            
            data=EmpleadoForm.cleaned_data
            data.update(
                userform.cleaned_data                              #se actualiza con update la variable data, que contiene datos de empleado mas datos de usuario 
            )
            #Crear instancias de empleado y usuario

            user = User(                                            #modelo User que viene por defecto en Django y le pasamos el username 
                username=data["username"]
            )
            user.set_password(data["password1"])                   #se agrega la contraseña del user encriptada
            user.save()                    

                   
            empleados=empleado(nombre=data['Nombre'],apellido=data['Apellido'],telefono=data['Telefono'],email=data['Email'],cargo=data['Cargo'], user_id=user)
            empleados.save()
            return render(request, "Save.html")
        else:
            return render (request,"CreateEmpleado.html")

    else:
        EmpleadoForm=empleadosFormulario()

        userform = UserCreationForm()
        avatar=Avatar.objects.filter(user=request.user.id)  
        filtro=len(avatar)-1                  #en el registro avatar, en la propiedad imagen, en el campo tipo imagen adentro tiene un url
   
        return render(request,"CreateEmpleado.html", {"CrearEmpleado":EmpleadoForm, "userform":userform,"url":avatar[filtro].imagen.url})


#Registrarse

def IrRegistrarse(request):

    
    return render (request, "LoginRegistro.html")

def registrarse(request):

    if request.method == "POST":
        form = CrearUsuario(request.POST)
        
        if form.is_valid() :
          username=form.cleaned_data["username"]
         
          form.save()
          #se autologin al crear usuario:
          user=authenticate(username=form.cleaned_data["username"], password=form.cleaned_data["password1"])
          login(request,user)
          
          return render(request,'Save.html',{"mensaje":f"Usuario {username} creado."})
        else:
            form=CrearUsuario()
            
            mensaje=f"Error. Usuario Invalido."
            return render (request,'LoginRegistro.html', {"CrearUsuario": form,"mensaje":mensaje})
            

    else:
        userForm=CrearUsuario()
        mensaje=f"Siga las instrucciones y cree su usuario."
       

    return render (request,'LoginRegistro.html', {"CrearUsuario": userForm,"mensaje":mensaje})

@login_required
def EditarPerfil(request):

    usuario=request.user
    
    if request.method == "POST":
         formularioPerfil=EditarUsuario (request.POST,request.user)
         if formularioPerfil.is_valid():
                data=formularioPerfil.cleaned_data

                
                usuario.first_name=data["first_name"]
                usuario.last_name=data["last_name"]
                usuario.email=data["email"]
                usuario.save()
                
                return render(request, "Save.html", {"mensaje":"Datos actualizados con exito.."})
    else:
        formularioPerfil=EditarUsuario(initial={
            "first_name":usuario.first_name,
            "last_name":usuario.last_name,
            "email":usuario.email
                })
    return render (request, "LoginPerfil.html", {"PerfilFormulario":formularioPerfil})

#Cambiar contraseña
@login_required
def CambiarPassword(request): 

    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return render(request,"SavePerfil.html",{"mensaje":"Datos actualizados con exito.."})
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'LoginCambiarPassword.html', {'form':form})
    

@login_required
def agregar_avatar(request):

    if request.method == 'POST':
       
        miFormulario = AvatarFormulario(request.POST, request.FILES)

        if miFormulario.is_valid():
           
            data = miFormulario.cleaned_data
            avatar =Avatar(user=request.user, imagen=data['imagen'])
            avatar.save()

            return render(request, "SavePerfil.html")
        else:
           
            miFormulario = AvatarFormulario()
            return render(request, "LoginAgregarAvatar.html", {"miFormulario": miFormulario,"mensaje":"Error"})


    else:
        avatarform = AvatarFormulario()
        
    return render(request, "LoginAgregarAvatar.html", {"miFormulario": avatarform})


#Enviar Mensaje
def IrEnviarMensaje(request):
    return render (request,"EnviarMensaje.html")

def Mensajeria(request):


    if request.method == "POST":
        
        form=FormularioMensaje(request.POST)

        if form.is_valid():
            


            #De esta forma me pide validacion en el formulario
            name=form.cleaned_data["Nombre"]# ["LA VARIABLE DEL FORMULARIO"]
            lastname=form.cleaned_data["Apellido"]
            email=form.cleaned_data["Correo"]
            subject=form.cleaned_data["Asunto"]
            message=form.cleaned_data["Mensaje"]
            usuario=request.user
            # name=request.POST['name']     CUANDO USAMOS name=" " EN EL HTML
            # email=request.POST['email']
            # subject=request.POST['asunto']
            # message=request.POST['mensaje']
            # usuario=request.user


            template=render_to_string('EnviarEmailTemaplte.html',{
                'name':name,
                'lastname': lastname,
                'email':email,
                'message':message,
                'usuario':usuario
                #el asunto se envia por defecto
            })
            #creamos Email: Toma parametros
            email=EmailMessage(
                subject,
                template,
                settings.EMAIL_HOST_USER,
                ['biciclteria.app@gmail.com']
            )

            email.send()
            #cuando se recargue la pagina aparece el mensaje en el template
            messages.success(request,'Correo Enviado')
            try:
                avatar=Avatar.objects.filter(user=request.user.id)   
                filtro=len(avatar)-1 
                return render (request,"Save.html",{"mensaje":"Nos contactaremos a la brevedad..","url":avatar[filtro].imagen.url})
            except:
                return render (request,"Save.html",{"mensaje":"Nos contactaremos a la brevedad.."})

        else:
            form=FormularioMensaje()
            messages.error(request,'Correo No valido')
    else:
        form=FormularioMensaje()
        try:
            avatar=Avatar.objects.filter(user=request.user.id)   
            filtro=len(avatar)-1 
            return render (request,"EnviarMensaje.html",{"formularioMensaje":form,"url":avatar[filtro].imagen.url})
        except:
            return render (request,"EnviarMensaje.html",{"formularioMensaje":form})






