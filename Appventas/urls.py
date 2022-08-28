from django.contrib import admin
from django.urls import path
# from Appventas.models import Avatar
from Appventas.views import (#Tupla
    BusquedaAcc, CambiarPassword, EditarPerfil, Formularioaccesorios, Formulariobicis, Formulariocategoria, 
    Formularioindumentarias, Formulariorepuestos, LeerAcc, LeerCategoria, MensajesPrivados, ResultAcc, agregar_avatar,
     agregar_producto, editaraccesorios, editarbicis, editarcategoria, editarindumentaria,
    editarrepuestos, eliminar_producto, eliminarIndumentaria, eliminaraccesorios, eliminarbici, 
    eliminarcategoria, eliminarrepuestos, iniciar_sesion, inicio, 
    Busquedabicis, limpiar_carrito, registrarse, LeerIndum, LeerBicis, LeerRepu, ResultBici, BusquedaIndu, 
    BusquedaRepues, ResultIndu, ResultRepues,
    Nosotros, Formularios, IrEnviarMensaje, IrRegistrarse, restar_producto, tienda,
    

)
from django.contrib.auth.views import LogoutView
from .import views

#from Appventas.views import BusquedaIndu, BusquedaRepuesto, RespuestaBuscarIndu, RespuestaBuscarRepuesto
                                  


urlpatterns = [
    
     #Simple accesow
    path('', inicio, name="INICIO"),
    path('Formularios', Formularios ,name="Formularios"),
    path('Nosotros/', Nosotros,name="Nosotros"),
    path('EnviarMensaje/',IrEnviarMensaje,name="EnviarMensaje"),
    #CARGAR DATOS
    path('FormularioBici/', Formulariobicis, name="bici_formulario"),
    path('repu_formulario/', Formulariorepuestos, name="repu_formulario"),
    path('indu_formulario/', Formularioindumentarias, name="indu_formulario"),
    path('acc_formulario/', Formularioaccesorios, name="acc_formulario"),
    path('cat_formulario/', Formulariocategoria, name="cat_formulario"),
    #VER FORULARIOS
    path('Leerindumentria/', LeerIndum, name="Leerindume"),
    path('LeerBicicletas/', LeerBicis, name="LeerBicis"),
    path('LeerRepuestos/',LeerRepu, name="LeerRepues") ,
    path('LeerAccesorios/',LeerAcc, name="LeerAcc") ,
    path('LeerCategorias/',LeerCategoria, name="LeerCategorias") , 
    #BUSCAR
    #en el template. con "direccion"(sin /) entre las comillas, y con "{% url 'name'%}" va el name.         
    path('BusquedaBici/', Busquedabicis, name="Buscar1"),#Ir pagina de busqueda bicis
    path('IrBici/', ResultBici, name="Busqueda1"),#Buscar bici
    path('BuscarRepuesto/',BusquedaRepues,name="Buscar2"),
    path('IrRepues/',ResultRepues,name="Busqueda2"),
    path('BuscarIndumentaria/',BusquedaIndu, name="Buscar3"),
    path('Irndumentaria/', ResultIndu, name="Busqueda3"),
    path('BuscarAccesorio/', BusquedaAcc, name="BuscarAcc"),
    path('IrAccesorio/', ResultAcc, name="ResultAcc"),
    #ELIMINAR
    path('eliminarbici/<int:id>', eliminarbici, name="Eliminarbici"),
    path('eliminarindu/<int:id>', eliminarIndumentaria, name="Eliminarindu"),
    path('eliminarrepu/<int:id>', eliminarrepuestos, name="Eliminarrepu"),
    path('eliminaracc/<int:id>', eliminaraccesorios, name="Eliminaracc"),
    path('eliminarcat/<int:id>', eliminarcategoria, name="Eliminarcat"),

    #EDITAR
    path('editarbicis/<int:id>', editarbicis, name="Editarbicis"),
    path('editarrepu/<int:id>', editarrepuestos, name="Editarrepu"),
    path('editarindu/<int:id>', editarindumentaria, name="Editarindu"),
    path('editaracc/<int:id>', editaraccesorios, name="Editaracc"),
    path('editarcat/<int:id>', editarcategoria, name="Editarcat"),
    
    #LOGIN
    path('login', iniciar_sesion, name='Login'),
    path('IrRegistro', IrRegistrarse,name="IrRegistro" ),
    path('registrarse', registrarse, name='Registrarse'),
    path('logout', LogoutView.as_view(template_name='logout.html'),name='Logout'),
    path('loginPerfil', EditarPerfil, name="Perfil"),
   

    #carrito
    path('tienda', tienda, name="Tienda"),
    path('agregar/<int:producto_id>', agregar_producto, name="Agregar"),
    path('eliminar/<int:producto_id>', eliminar_producto, name="Eliminar"),
    path('restar/<int:producto_id>', restar_producto, name="Restar"),
    path('limpiar/<int:producto_id>', limpiar_carrito, name="Limpiar"),
    path('CambiarContraseña',CambiarPassword, name="CambiarContraseña"),
    
    #Imagenes/Avatars
    path('CambiarAvatar',agregar_avatar, name="CambiarAvatar"),
    #chat entre usuarios
    path('ChatUsuarios/<str:username>',MensajesPrivados, name="ChatUsuarios"),
]

