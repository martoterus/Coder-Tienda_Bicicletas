from django.contrib import admin

from Appventas.carrito import carrito

from .models import *#Importamos el archivo Models

# Register your models here.
admin.site.register(Avatar)
admin.site.register(bicicletas)
admin.site.register(indumentarias)
admin.site.register(repuestos)
admin.site.register(accesorios)
admin.site.register(categorias)

