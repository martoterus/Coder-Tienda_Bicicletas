from django.contrib import admin
from django.urls import path
from Appventas.views import (
    BusquedaAcc, CrearEmpleado, EditarEmpleado, EditarPerfil, EliminarEmpleado, Formularioaccesorios, Formulariobicis, Formulariocategoria, Formularioindumentarias, Formulariorepuestos, LeerAcc, LeerCategoria, LeerEmpleado, ResultAcc, editaraccesorios, editarbicis, editarcategoria, editarindumentaria,
    editarrepuestos, eliminarIndumentaria, eliminaraccesorios, eliminarbici, eliminarcategoria, eliminarrepuestos, iniciar_sesion, inicio, 
    Busquedabicis, registrarse, LeerIndum, LeerBicis, LeerRepu, ResultBici, BusquedaIndu, BusquedaRepues, ResultIndu, ResultRepues,
    Nosotros, IrEnviarMensaje, IrRegistrarse
)
from django.contrib.auth.views import LogoutView
from .import views
from django.conf import settings
from django.conf.urls.static import static

#from Appventas.views import BusquedaIndu, BusquedaRepuesto, RespuestaBuscarIndu, RespuestaBuscarRepuesto
                                  


from django.contrib import admin
from django.urls import path

# from Appventas.models import Avatar
from Appventas.views import (#Tupla
    BusquedaAcc, CambiarPassword, EditarPerfil, Formularioaccesorios, Formulariobicis, Formulariocategoria, 
    Formularioindumentarias, Formulariorepuestos,LeerAcc, LeerCategoria, Mensajeria, ResultAcc, editaraccesorios, editarbicis, editarcategoria, editarindumentaria,
    editarrepuestos, eliminar_producto, eliminarIndumentaria, eliminaraccesorios, eliminarbici, 
    eliminarcategoria, eliminarrepuestos, iniciar_sesion, inicio, 
    Busquedabicis, limpiar_carrito, registrarse, LeerIndum, LeerBicis, LeerRepu, ResultBici, BusquedaIndu, 
    BusquedaRepues, ResultIndu, ResultRepues,
    Nosotros, IrEnviarMensaje, IrRegistrarse, tienda
    

)
from django.contrib.auth.views import LogoutView

urlpatterns = [
    
     #Simple accesow
    path('', inicio, name="INICIO"),
    #path('Formularios', Formularios ,name="Formularios"),
    path('Nosotros/', Nosotros,name="Nosotros"),
    path('EnviarMensaje/',IrEnviarMensaje,name="EnviarMensaje"),
    #CARGAR DATOS
    path('FormularioEmpleado/', CrearEmpleado, name="FormularioEmpleado"),
    path('FormularioBici/', Formulariobicis, name="bici_formulario"),
    path('repu_formulario/', Formulariorepuestos, name="repu_formulario"),
    path('indu_formulario/', Formularioindumentarias, name="indu_formulario"),
    path('acc_formulario/', Formularioaccesorios, name="acc_formulario"),
    path('cat_formulario/', Formulariocategoria, name="cat_formulario"),
    #VER FORMULARIOS
    path('Leerindumentria/', LeerIndum, name="Leerindume"),
    path('LeerBicicletas/', LeerBicis, name="LeerBicis"),
    path('LeerRepuestos/',LeerRepu, name="LeerRepues") ,
    path('LeerAccesorios/',LeerAcc, name="LeerAcc") ,
    path('LeerCategorias/',LeerCategoria, name="LeerCategorias"),
    path('LeerEmpleados/',LeerEmpleado, name="LeerEmpleados"),  
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
    path('eliminarEmpleado/<int:id>', EliminarEmpleado, name="EliminarEmpleado"),

    #EDITAR
    path('editarbicis/<int:id>', editarbicis, name="Editarbicis"),
    path('editarrepu/<int:id>', editarrepuestos, name="Editarrepu"),
    path('editarindu/<int:id>', editarindumentaria, name="Editarindu"),
    path('editaracc/<int:id>', editaraccesorios, name="Editaracc"),
    path('editarcat/<int:id>', editarcategoria, name="Editarcat"),
    path('editarEmpleado/<int:id>', EditarEmpleado, name="EditarEmpleado"),
    
    #LOGIN
    path('login', iniciar_sesion, name='Login'),
    path('IrRegistro', IrRegistrarse,name="IrRegistro" ),
    path('registrarse', registrarse, name='Registrarse'),
    path('logout', LogoutView.as_view(template_name='logout.html'),name='Logout'),
    path('loginPerfil', EditarPerfil, name="Perfil"),
    path('CambiarContraseña', CambiarPassword, name="CambiarContraseña"),

    #Tienda
    path('tienda', views.tienda, name="Tienda"),
    path('tiendabici', views.tiendabici, name="Tiendabici"),
    path('tiendarepu', views.tiendarepuestos, name="Tiendarepu"),
    path('tiendaacc', views.tiendaaccesorios, name="Tiendaacc"),
    path('tiendaindu', views.tiendaindumentaria, name="Tiendaindu"),

    #carrito
    path('agregarbici/<int:producto_id>', views.agregar_bicicleta, name="Agregarbici"),
    path('agregarrepu/<int:producto_id>', views.agregar_repuesto, name="Agregarrepu"),
    path('agregaracc/<int:producto_id>', views.agregar_accesorio, name="Agregaracc"),
    path('agregarindu/<int:producto_id>', views.agregar_indumentaria, name="Agregarindu"),
    path('eliminar/<int:producto_id>', views.eliminar_producto, name="Eliminar"),
    path('restarbici/<int:producto_id>', views.restar_bicicleta, name="Restarbici"),
    path('restarrepu/<int:producto_id>', views.restar_repuesto, name="Restarrepu"),
    path('restaracc/<int:producto_id>', views.restar_accesorio, name="Restaracc"),
    path('restarindu/<int:producto_id>', views.restar_indumentaria, name="Restarindu"),
    path('limpiar/', views.limpiar_carrito, name="Limpiar"),
    
    #Emviar Correo
    #path('IrEnviarMensaje',IrEnviarMensaje,name="Contacto"),
    path('EnviarMensaje',Mensajeria,name="MensajeCorreo"),

    #Imagenes/Avatars
    #path('CambiarAvatar',agregar_avatar,name="CambiarAvatar"),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
