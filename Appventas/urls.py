from django.contrib import admin
from django.urls import path
from Appventas.views import (
    AvatarNosotros, BusquedaAcc, EditarPerfil, Formularioaccesorios, Formulariobicis, Formulariocategoria, Formularioindumentarias, Formulariorepuestos, LeerAcc, LeerCategoria, ResultAcc, CambiarContraseña, editaraccesorios, editarbicis, editarcategoria, editarindumentaria,
    editarrepuestos, eliminarIndumentaria, eliminaraccesorios, eliminarbici, eliminarcategoria, eliminarrepuestos, iniciar_sesion, inicio, 
    Busquedabicis, registrarse, LeerIndum, LeerBicis, LeerRepu, ResultBici, BusquedaIndu, BusquedaRepues, ResultIndu, ResultRepues,
    Nosotros, Formularios, IrEnviarMensaje, IrRegistrarse, AgregarAvatar
)
from django.contrib.auth.views import LogoutView
#from Appventas.views import BusquedaIndu, BusquedaRepuesto, RespuestaBuscarIndu, RespuestaBuscarRepuesto
#from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, password_reset_complete
                                  


urlpatterns = [
    
     #Simple accesow
    path('', inicio, name="INICIO"),
    path('Formularios', Formularios ,name="Formularios"),
    path('Nosotros/', Nosotros,name="Nosotros"),
    path('Nos-Avatar',AvatarNosotros,name="AvatarNosotros"),
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
    path('CambiarContraseña',CambiarContraseña, name="CambiarContraseña"),
    #Olvide contraseña
    #path('reset/password_reset',password_reset,{'template_name':'templates/LoginPswResetForm.html',
    #'email_template':'templates/'})   
    
    #Imagenes/Avatars
    path('agregar-avatar', AgregarAvatar, name="AgregarAvatar"),
    #path('save-avatar', SavePerfil, name="SaveAvatar"),
]

