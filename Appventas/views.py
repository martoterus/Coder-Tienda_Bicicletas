from msilib.schema import ListView
from django.shortcuts import redirect
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from .carrito import carrito
from Appventas.models import accesorios, bicicletas, categorias, indumentarias, repuestos, EnviarMensaje
from Appventas.forms import AvatarFormulario, AccesoriosFormularios, BicicletasFormularios, FormularioMensaje, IndumentariasFormularios, RepuestosFormularios, categoriasFormulario, enviarMensaje, FormularioMensaje, CrearUsuario
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm , UserChangeForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin #solo funciona con las vistas basadas en clases
from django.contrib.auth.decorators import login_required#decorador para vistas basadas en funciones.Aumenta la funcionalidad de una funcion.

# Views de simple acceso
#imports para el chat:

#-----------------------------------------------
from queue import Empty
from unicodedata import name
from django.conf import settings
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

    return render(request, "QuienesSomos.html")

#def Formularios(request):#Template de Formularios
 #   categoria = categorias.objects.all()
  #  return render(request, "Formularios.html", {"categorias": categoria})


def inicio(request):#Template de Inivcio
    carr = carrito(request)
    categoria = categorias.objects.all()
    return render(request, "Formularios.html", {"categorias": categoria})

def tienda(request):
    bicicleta=bicicletas.objects.all()
    indumentaria=indumentarias.objects.all()
    accesorio=accesorios.objects.all()
    repuesto=repuestos.objects.all()

    pagina = request.GET.get("page", 1)
    paginatorBici = Paginator(bicicleta, 2)
    bicicleta = paginatorBici.page(pagina)
    paginatorIndu = Paginator(indumentaria, 2)
    indumentaria = paginatorIndu.page(pagina)
    return render(request, "tienda.html",{"bicicletas": bicicleta, "indumentarias": indumentaria, "accesorios": accesorio, "repuestos": repuesto})

def tiendabici(request):
    bicicleta=bicicletas.objects.all()
    return render(request, "tienda.html",{ "bicicletas": bicicleta})

def tiendarepuestos(request):
    repuesto=repuestos.objects.all()
    return render(request, "tienda.html",{ "repuestos": repuesto})

def tiendaaccesorios(request):
    accesorio=accesorios.objects.all()
    return render(request, "tienda.html",{ "accesorios": accesorio}) 

def tiendaindumentaria(request):
    indumentaria=indumentarias.objects.all()
    return render(request, "tienda.html",{ "indumentarias": indumentaria}) 
       
    
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

#Enviar Mensaje
# def IrEnviarMensaje(request):
#     print("method:", request.method)
#     if request.method == 'POST':
#             print("1° IF")
#             MensajeEnviado=enviarMensaje(request.POST)

#             if MensajeEnviado.is_valid():
#                 print("2do IF")
#                 data=MensajeEnviado.cleaned_data# si le pongo parentesis o corchetes y entre comillas una variable en particular pide solo esa
#                 mensaje=EnviarMensaje(nombre=data["Nombre"],correo=["Correo"],telefono=["Telefono"],mensaje=["Mensaje"])
#                 mensaje.save()
#                 return render(request,"Save.html")
#     else:
#         print("method:", request.method)
#         MensajeEnviado=enviarMensaje()
#         return render (request,"EnviarMensaje.html",{"MensajeEnviar":MensajeEnviado})



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
            bici=bicicletas(marca=data['Marca'],modelo=data['Modelo'],tipo=data["Tipo"],rodado=data['Rodado'],color=data['Color'],precio=data['Precio'],categoria=data['Categoria'],nombre=data['Nombre'],descripcion=data['Descripcion'],imagen=data['Imagen'])
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
    contexto={"Categorias":FormularioCategorias}
    return render (request, "VerFormulario_Categorias.html",contexto)
@login_required
def LeerBicis (request):
    print("method:", request.method) #Va  a imprimir por terminal el método que utilizamos. 

    FormularioBicicletas=bicicletas.objects.all()
    contexto={"Bicicletas":FormularioBicicletas}
    return render (request, "VerFormulario_Bicicletas.html",contexto)
@login_required
def LeerRepu (request):
    print("method:", request.method) #Va  a imprimir por terminal el método que utilizamos. 

    FormularioRepuestos=repuestos.objects.all()
    contexto={"Repuestos":FormularioRepuestos}
    return render (request, "VerFormulario_Repuestos.html",contexto)

@login_required
def LeerIndum (request):
    print("method:", request.method) #Va  a imprimir por terminal el método que utilizamos. 

    FormularioIndumentaria=indumentarias.objects.all()
    contexto={"Indumentaria":FormularioIndumentaria}
    return render (request, "VerFormulario_Indumentaria.html",contexto)
@login_required
def LeerAcc (request):
    print("method:", request.method) #Va  a imprimir por terminal el método que utilizamos. 

    FormularioAccesorios=accesorios.objects.all()
    contexto={"Accesorios":FormularioAccesorios}
    return render (request, "VerFormulario_Accesorios.html",contexto)


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

        BiciFormulario=BicicletasFormularios(request.POST, files=request.FILES)

        if BiciFormulario.is_valid():
            print("Entro al 2° if")
            data=BiciFormulario.cleaned_data
        
            bicicleta.nombre = data["Nombre"]
            bicicleta.categoria = data["Categoria"]
            bicicleta.tipo = data["Tipo"]
            bicicleta.marca = data ["Marca"]
            bicicleta.modelo = data ["Modelo"]
            bicicleta.rodado = data ["Rodado"]
            bicicleta.color = data ["Color"]
            bicicleta.descripcion = data ["Descripcion"]
            bicicleta.precio = data ["Precio"]
            bicicleta.imagen = data ["Imagen"]

            bicicleta.save()
            return render(request, "Save.html")
    
    else:
        BiciFormulario=BicicletasFormularios(initial={
            "nombre": bicicleta.nombre,
            "categoria": bicicleta.categoria,
            "tipo": bicicleta.tipo,
            "marca": bicicleta.marca,
            "modelo": bicicleta.modelo,
            "rodado": bicicleta.rodado,
            "color": bicicleta.color,
            "descripcion": bicicleta.descripcion,
            "precio": bicicleta.precio,
            "imagen": bicicleta.imagen,
        

        })
        return render(request,"EditarBicicletas.html", {"BiciFormulario": BiciFormulario , "id": id})
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
            "nombre": repuesto.nombre,
            "categoria": repuesto.categoria,
            "marca": repuesto.marca,
            "descripcion": repuesto.descripcion,
            "precio": repuesto.precio,
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
            indument.modelo = data ["Modelo"]
            indument.descripcion = data ["Descripcion"]
            indument.precio = data ["Precio"]
            indument.tipo = data ["Tipo"]
            indument.talle = data ["Talle"]

            indument.save()
            return render(request, "Save.html")
    
    else:
        induFormulario=IndumentariasFormularios(initial={
            "nombre": indument.nombre,
            "categoria": indument.categoria,
            "marca": indument.marca,
            "modelo": indument.modelo,
            "tipo": indument.tipo,
            "talle":indument.talle,
            "descripcion": indument.descripcion,
            "precio": indument.precio,
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

                return render(request, "inicio.html", {"mensaje":f"Bienvenido {usuario}"})
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
        formularioPerfil=EditarUsuario (instance=request.user)
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
        print("metodo:",request.method)
        miFormulario = AvatarFormulario(request.POST, request.FILES)

        if miFormulario.is_valid():
            print("1")

            data = miFormulario.cleaned_data

            avatar =Avatar(user=request.user, imagen=data['imagen'])
            print("2")
            avatar.save()

            return render(request, "SavePerfil.html", {"mensaje": "Avatar cargado."})
        else:
            print("no valida")
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
        print("1",request.method)
        form=FormularioMensaje(request.POST)

        if form.is_valid():
            print("2")


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

            return render (request,"Save.html",{"mensaje":"Nos contactaremos a la brevedad.."})

        else:
            print("3")

            form=FormularioMensaje()
            messages.error(request,'Correo No valido')
    else:
        form=FormularioMensaje()
    return render (request,"EnviarMensaje.html",{"formularioMensaje":form})

