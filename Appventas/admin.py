from django.contrib import admin

from .models import *#Importamos el archivo Models

# Register your models here.
#admin.site.register(Avatar)
admin.site.register(producto)
admin.site.register(categorias)
admin.site.register(empleado)
admin.site.register(cliente)

#para el chat
class CanalMensajeInline(admin.TabularInline):
    model= CanalMensaje
    extra= 1

class CanalUsuarioInline(admin.TabularInline):
    model= CanalUsuario
    extra=1

class CanalAdmin(admin.ModelAdmin):
    inlines = [CanalMensajeInline,CanalUsuarioInline]

    class Meta:
        model = Canal


admin.site.register(Canal, CanalAdmin)
admin.site.register(CanalUsuario)
admin.site.register(CanalMensaje)

