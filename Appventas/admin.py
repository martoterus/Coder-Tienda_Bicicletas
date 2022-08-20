from django.contrib import admin

from .models import *#Importamos el archivo Models

# Register your models here.
admin.site.register(Avatar)
admin.site.register(producto)
admin.site.register(categorias)