from django.shortcuts import redirect
from multiprocessing import context
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from Appventas.carrito import carrito
from Appventas.models import EnviarMensajes, categorias,producto
from Appventas.forms import productosFormularios, categoriasFormulario, enviarMensaje
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm , UserChangeForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin #solo funciona con las vistas basadas en clases
from django.contrib.auth.decorators import login_required#decorador para vistas basadas en funciones.Aumenta la funcionalidad de una funcion.
# Views de simple acceso
def Nosotros(request):#Template de Nostros

    return render(request, "QuienesSomos.html")

def Formularios(request):#Template de Formularios

    return render(request, "Formularios.html")

def inicio(request):#Template de Inivcio

    return render(request, "inicio.html")
    
#Carrito de compras
def agregar_producto(request, producto_id):
     carr = carrito(request)                            
     productos = producto.objects.get(id = producto_id)
     carr.agregar(productos)
     return redirect("Appventas:inicio")

def eliminar_producto(request, producto_id):
    carr= carrito(request)
    productos = producto.objects.get(id = producto_id)
    carr.eliminar(productos)
    return redirect("Appventas:inicio")

def restar_producto(request, producto_id):
    carr= carrito(request)
    productos = producto.objects.get(id = producto_id)
    carr.restar(productos)
    return redirect("Appventas:inicio")

def limpiar_carrito(request):
    carr= carrito(request)
    carr.limpiar_carrito()
    return redirect("Appventas:inicio")

#Enviar Mensaje
def IrEnviarMensaje(request):
    print("method:", request.method)
    if request.method == 'POST':
            print("1° IF")
            MensajeEnviado=enviarMensaje(request.POST)

            if MensajeEnviado.is_valid():
                print("2do IF")
                data=MensajeEnviado.cleaned_data# si le pongo parentesis o corchetes y entre comillas una variable en particular pide solo esa
                mensaje=EnviarMensajes(nombre=data["Nombre"],correo=["Correo"],telefono=["Telefono"],mensaje=["Mensaje"])
                mensaje.save()
                return render(request,"Save.html")
    else:
        print("method:", request.method)
        MensajeEnviado=enviarMensaje()
        return render (request,"EnviarMensaje.html",{"MensajeEnviar":MensajeEnviado})



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
        BiciFormulario=productosFormularios(request.POST)
        print("method:", request.method) #Va  a imprimir por terminal el método que utilizamos. 
        print("Formulario:",BiciFormulario ) 

        if BiciFormulario.is_valid():
            print("Entro al 2° if")
            data=BiciFormulario.cleaned_data
            #En la tabla que creo con la clase le cargo los datos del formulario de Django
            bici=producto(marca=data['Marca'],modelo=data['Modelo'],tipo=data["Tipo"],rodado=data['Rodado'],color=data['Color'],precio=data['Precio'],categoria=data['Categoria'],nombre=data['Nombre'],descripcion=data['Descripcion'],disponibilidad=data['Disponibilidad'])
            bici.save()
            return render(request, "Save.html")
       # else:
        #    return render (request,"inicio2.html")
    else:
        BiciFormulario=productosFormularios()
        return render(request,"FormularioBicicletas.html", {"BiciFormulario": BiciFormulario})

@login_required
def Formularioindumentarias(request):#Template cargar una indumentaria en la tabla


    if request.method == 'POST':
        InduFormulario=productosFormularios(request.POST)
        print("method:", request.method) #Va  a imprimir por terminal el método que utilizamos. 
        print("Formulario:",InduFormulario ) 

        if InduFormulario.is_valid():
            print("Entro al 2° if")
            data=InduFormulario.cleaned_data
            #En la tabla que creo con la clase le cargo los datos del formulario de Django
            Indu=producto(tipo=data['Tipo'],marca=data['Marca'],modelo=data['Modelo'],talle=data['Talle'],precio=data['Precio'],nombre=data['Nombre'],descripcion=data['Descripcion'],categoria=data['Categoria'],disponibilidad=data['Disponibilidad'])
            Indu.save()
            return render(request, "Save.html")
        else:
            return render (request,"inicio2.html")
    else:
        InduFormulario=productosFormularios()
        return render(request,"FormularioIndumentaria.html", {"IndumentariaFormularios": InduFormulario})

@login_required
def Formulariorepuestos(request):#Template cargar un repuesto en la tabla

    if request.method == 'POST':
                        #forms.py
        RepuFormulario=productosFormularios(request.POST)
        print("method:", request.method) #Va  a imprimir por terminal el método que utilizamos. 
        print("Formulario:",RepuFormulario ) 

        if RepuFormulario.is_valid():
            print("Entro al 2° if")
            data=RepuFormulario.cleaned_data
            #En la tabla que creo con la clase (models) le cargo los datos del formulario de Django(forms)
                     #models.py   (como se lee esto?: tipo=data['Tipo'])          
            repuesto=producto(tipo=data['Tipo'], nombre=data['Nombre'], marca=data['Marca'],modelo=data['Modelo'],descripcion=data['Descripcion'],precio=data['Precio'],categoria=data['Categoria'],disponibilidad=data['Disponibilidad'])
            repuesto.save()
            return render(request, "Save.html")
        else:
            return render (request,"inicio2.html")
    else:
        RepuFormulario=productosFormularios()
        return render(request,"FormularioRepuestos.html", {"RepuestosFormularios":RepuFormulario})

@login_required
def Formularioaccesorios(request):#Template cargar un repuesto en la tabla

    if request.method == 'POST':
                        #forms.py
        AccFormulario=productosFormularios(request.POST)
        print("method:", request.method) #Va  a imprimir por terminal el método que utilizamos. 
        print("Formulario:",AccFormulario ) 

        if AccFormulario.is_valid():
            print("Entro al 2° if")
            data=AccFormulario.cleaned_data
            #En la tabla que creo con la clase (models) le cargo los datos del formulario de Django(forms)
                     #models.py   (como se lee esto?: tipo=data['Tipo'])          
            repuesto=producto(tipo=data['Tipo'],marca=data['Marca'],modelo=data['Modelo'],precio=data['Precio'],nombre=data['Nombre'],descripcion=data['Descripcion'],categoria=data['Categoria'],disponibilidad=data['Disponibilidad'])
            repuesto.save()
            return render(request, "Save.html")
        else:
            return render (request,"inicio2.html")
    else:
        AccFormulario=productosFormularios()
        return render(request,"FormularioAccesorios.html", {"AccesorioFormularios":AccFormulario})   


#VER FORMULARIOS

def LeerCategoria(request):
    print("method:", request.method) #Va  a imprimir por terminal el método que utilizamos. 

    FormularioCategorias=categorias.objects.all()
    contexto={"Categorias":FormularioCategorias}
    return render (request, "VerFormulario_Categorias.html",contexto)

def LeerBicis (request):
    print("method:", request.method) #Va  a imprimir por terminal el método que utilizamos. 

    FormularioBicicletas=producto.objects.all()
    contexto={"Bicicletas":FormularioBicicletas}
    return render (request, "VerFormulario_Bicicletas.html",contexto)

def LeerRepu (request):
    print("method:", request.method) #Va  a imprimir por terminal el método que utilizamos. 

    FormularioRepuestos=producto.objects.all()
    contexto={"Repuestos":FormularioRepuestos}
    return render (request, "VerFormulario_Repuestos.html",contexto)



def LeerIndum (request):
    print("method:", request.method) #Va  a imprimir por terminal el método que utilizamos. 

    FormularioIndumentaria=producto.objects.all()
    contexto={"Indumentaria":FormularioIndumentaria}
    return render (request, "VerFormulario_Indumentaria.html",contexto)

def LeerAcc (request):
    print("method:", request.method) #Va  a imprimir por terminal el método que utilizamos. 

    FormularioAccesorios=producto.objects.all()
    contexto={"Accesorios":FormularioAccesorios}
    return render (request, "VerFormulario_Accesorios.html",contexto)


#BUSQUEDA BICIS

def Busquedabicis(request):

    return render (request, "BusquedaBici.html")

def ResultBici(request):
    print(request.GET)

    if request.GET["modelo"]: 
       
        modelo=request.GET["modelo"]
      
        modelos=producto.objects.filter(modelo__icontains=modelo)
        
        return render (request,"BusquedaBicicleta.html", {"modelos": modelos , "modelo":modelo})
    else:
       
        respuesta="No enviaste datos"
        return render(respuesta,"BusquedaBicicleta.html")
    

#BUSQUEDA INDUMENTARIA
def BusquedaIndu(request):

    return render (request, "BusquedaIndu.html")

def ResultIndu(request):
    print(request.GET)

    if request.GET["tipo"]: 
        
        tipo=request.GET["tipo"]
        
        tipos=producto.objects.filter(tipo__icontains=tipo)
        
        return render (request,"BusquedaIndumentaria.html", {"tipos": tipos ,"tipo":tipo})
    else:
        
        respuesta="No enviaste datos"
        return render(respuesta,"BusquedaIndumentaria.html")
 

#BUSQUEDA RESPUESTO
def BusquedaRepues(request):

    return render (request, "BusquedaRepu.html")

def ResultRepues(request):
    print(request.GET)

    if request.GET["tipo"]: 
        
        tipo=request.GET["tipo"]
        
        tipos = producto.objects.filter(tipo__icontains=tipo)
        
        return render (request,"BusquedaRepuesto.html", {"tipos": tipos , "tipo":tipo})
    else:
        
        respuesta="No enviaste datos"
        return render(respuesta,"BusquedaRepuesto.html")
    
#BUSQUEDA ACCESORIOS
def BusquedaAcc(request):

    return render (request, "BusquedaAcc.html")

def ResultAcc(request):
    print(request.GET)

    if request.GET["tipo"]: 
        
        tipo=request.GET["tipo"]
       
        tipos=producto.objects.filter(tipo__icontains=tipo)
        
        return render (request,"BusquedaAccesorios.html", {"tipos": tipos , "tipo":tipo})
    else:
        
        respuesta="No enviaste datos"
        return render(respuesta,"BusquedaAccesorios.html")

#ELIMINAR DATOS

def eliminarcategoria(request, id):

    if request.method == "POST":


       categoria = categorias.objects.get(id = id)
       categoria.delete()

       #vuelvo al menu
       categoria = categorias.objects.all() #trae todas las bicicletas

       contexto = {"categorias" : categoria}
 
       return render (request, "VerFormulario_Bicicletas.html", contexto)

def eliminarbici(request, id):

    if request.method == "POST":


       bicicleta = producto.objects.get(id = id)
       bicicleta.delete()

       #vuelvo al menu
       bicicleta = producto.objects.all() #trae todas las bicicletas

       contexto = {"bicicletas" : bicicleta}
 
       return render (request, "VerFormulario_Bicicletas.html", contexto)

def eliminarIndumentaria(request, id):

    if request.method == "POST":


       indumentarias = producto.objects.get(id = id)
       indumentarias.delete()

       #vuelvo al menu
       Indumentaria = producto.objects.all() #trae todas las bicicletas

       contexto = {"indumentaria" : Indumentaria}
 
       return render (request, "VerFormulario_Indumentaria.html", contexto)

def eliminarrepuestos(request, id):

    if request.method == "POST":


       repuesto = producto.objects.get(id = id)
       repuesto.delete()

       #vuelvo al menu
       repuesto = producto.objects.all() #trae todas las bicicletas

       contexto = {"indumentaria" : repuesto}
 
       return render (request, "VerFormulario_Repuestos.html", contexto)

def eliminaraccesorios(request, id):

    if request.method == "POST":


       accesorio = producto.objects.get(id = id)
       accesorio.delete()

       #vuelvo al menu
       accesorio = producto.objects.all() #trae todas las bicicletas

       contexto = {"indumentaria" : accesorio}
 
       return render (request, "VerFormulario_Accesorios.html", contexto)

#EDITAR

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

def editarbicis(request, id):

    bicicleta = producto.objects.get(id = id)

    if request.method == 'POST':

        BiciFormulario=productosFormularios(request.POST)

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

            bicicleta.save()
            return render(request, "Save.html")
    
    else:
        BiciFormulario=productosFormularios(initial={
            "nombre": bicicleta.nombre,
            "categoria": bicicleta.categoria,
            "tipo": bicicleta.tipo,
            "marca": bicicleta.marca,
            "modelo": bicicleta.modelo,
            "rodado": bicicleta.rodado,
            "color": bicicleta.color,
            "descripcion": bicicleta.descripcion,
            "precio": bicicleta.precio,
        

        })
        return render(request,"EditarBicicletas.html", {"BiciFormulario": BiciFormulario , "id": id})

def editarrepuestos(request, id):

    repuesto = producto.objects.get(id = id)

    if request.method == 'POST':
        
        repuFormulario=productosFormularios(request.POST)

        if repuFormulario.is_valid():
            print("Entro al 2° if")
            data=repuFormulario.cleaned_data
        
            repuesto.nombre = data ["Nombre"]
            repuesto.categoria = data["Categoria"]
            repuesto.marca = data ["Marca"]
            repuesto.tipo = data ["Tipo"]
            repuesto.modelo = data ["Modelo"]
            repuesto.descripcion = data ["Repuesto"]
            repuesto.precio = data ["Repuesto"]

            repuesto.save()
            return render(request, "Save.html")
    
    else:
        repuFormulario=productosFormularios(initial={
            "nombre": repuesto.nombre,
            "categoria": repuesto.categoria,
            "marca": repuesto.marca,
            "modelo": repuesto.modelo,
            "tipo": repuesto.tipo,
            "descripcion": repuesto.descripcion,
            "precio": repuesto.precio,
        })
        return render(request,"EditarRepuestos.html", {"RepuFormulario": repuFormulario , "id": repuesto.id})

def editarindumentaria(request, id):

    indument = producto.objects.get(id = id)

    if request.method == 'POST':
        
        induFormulario=productosFormularios(request.POST)

        if induFormulario.is_valid():
            print("Entro al 2° if")
            data=induFormulario.cleaned_data
        
            indument.nombre = data ["Nombre"]
            indument.categoria = data["Categoria"]
            indument.marca = data ["Marca"]
            indument.modelo = data ["Modelo"]
            indument.descripcion = data ["Repuesto"]
            indument.precio = data ["Repuesto"]
            indument.tipo = data ["tipo"]
            indument.talle = data ["Talle"]

            indument.save()
            return render(request, "Save.html")
    
    else:
        induFormulario=productosFormularios(initial={
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


def editaraccesorios(request, id):

    acc = producto.objects.get(id = id)

    if request.method == 'POST':
        
        accFormulario=productosFormularios(request.POST)

        if accFormulario.is_valid():
           
            data=accFormulario.cleaned_data
        
            acc.nombre = data ["Nombre"]
            acc.categoria = data ["Categoria"]
            acc.marca = data ["Marca"]
            acc.modelo = data ["Modelo"]
            acc.descripcion = data ["Descripcion"]
            acc.precio = data ["Precio"]
            acc.tipo = data ["Tipo"]
            acc.talle = data ["Talle"]

            acc.save()
            return render(request, "Save.html")
    
    else:
        accFormulario=productosFormularios(initial={
            "nombre": acc.nombre,
            "categoria": acc.categoria,
            "marca": acc.marca,
            "modelo": acc.modelo,
            "tipo": acc.tipo,
            "talle":acc.talle,
            "descripcion": acc.descripcion,
            "precio": acc.precio,
        })
        return render(request,"EditarAccesorios.html", {"AccFormulario": accFormulario , "id": acc.id})

#LOGIN
def iniciar_sesion(request):

    if request.method == "POST":
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

    if request.method =="POST":
        print("1)method:", request.method)
        form=UserCreationForm(request.POST)
        #form=UserRegisterForm(request.POST)
        if form.is_valid():
            print("2)method:", request.method)
            username = form.cleaned_data['username']
            form.save()
            return render(request,'Save.html',{"mensaje":f"Usuario {username} creado."})
        else:
            form=UserCreationForm()
            return render (request, 'LoginRegistro.html',{"mensaje":f"Usuario no valido. Vuelva a Intentarlo.","form": form})
        
    else:
        form=UserCreationForm()
        return render (request,'LoginRegistro.html', {"form": form})

# #Perfil Usuario


def EditarPerfil(request):

    usuario=request.user
    
    if request.method == "POST":
         
        formularioPerfil=EditarUsuario (request.POST)


        if formularioPerfil.is_valid():
                
                data=formularioPerfil.cleaned_data

                usuario.first_name=data["first_name"]
                usuario.last_name=data["last_name"]
                usuario.email=data["email"]
                #usuario.password1=data["password1"]
                #usuario.password2=data["password2"]

                usuario.save()

                return render(request, "Save.html", {"mensaje":"Datos actualizados con exito.."})
    else:
          
        formularioPerfil=EditarUsuario (initial={'Nombre':usuario.first_name,'Apellido':usuario.last_name,'Email':usuario.email})
        #formularioPerfil=UserChangeForm (instance=request.user)
        
    return render (request, "LoginPerfil.html", {"PerfilFormulario":formularioPerfil}) 
        
   


