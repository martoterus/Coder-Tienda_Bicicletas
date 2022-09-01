
# Create your models here.

from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User




class categorias(models.Model):
    nombre = models.CharField(max_length=100)


    class Meta:
        verbose_name = "categoria"
        verbose_name_plural = "categorias"
    
    def __str__(self):
        return self.nombre

class producto(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.ForeignKey(categorias, on_delete=models.CASCADE)
    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=100)
    precio = models.FloatField()
    rodado = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    tipo = models.CharField(max_length=30)
    talle = models.CharField(max_length=30)
    disponibilidad = models.BooleanField(default=True)

    class Meta:
        verbose_name = "producto"
        verbose_name_plural = "productos"

    def __str__(self):
        return self.nombre

class tipoPersonas(models.Model):
    nombre = models.CharField(max_length=100)


    # class Meta:
    #     verbose_name = "categoria"
    #     verbose_name_plural = "categorias"
    
    def __str__(self):
        return self.nombre


class empleado(models.Model):
    
    nombre=models.CharField(max_length=30,)
    Apellido=models.CharField(max_length=30,)
    Telefono=models.IntegerField()
    nombre=models.EmailField(max_length=30)
   # categoria = models.ForeignKey(tipoPersonas, on_delete=models.CASCADE)
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        verbose_name = "empleado"
        verbose_name_plural = "empleados"

    def __str__(self):
        return self.nombre

class cliente(models.Model):
    
    nombre=models.CharField(max_length=30,)
    Apellido=models.CharField(max_length=30,)
    Telefono=models.IntegerField()
    nombre=models.EmailField(max_length=30)
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        verbose_name = "cliente"
        verbose_name_plural = "clientes"

    def __str__(self):
        return self.nombre


# class perfiles(models.Model):
#     nombre=models.CharField(max_length=30, )
#     apellido=models.CharField(max_length=30)
#     telefono= models.IntegerField() 
#     emial=models.EmailField(max_length=100)
    
#     class Meta:
#         abstract=True

# class empleado(perfiles):
#    cargo=models.CharField(max_length=30)

#    def __str__(self):
#     return f"{self.nombre,self.apellido, self.telefono,self.emial,self.cargo}"

# class cliente(perfiles):
#     edad=models.IntegerField()

#     def __str__(self):
#      return f"{self.nombre,self.apellido, self.telefono,self.emial,self.edad}"



#Comentar todo: selecciono . 1°ctrl+k . 2°ctrl+c (comentar) 2°ctrl+u (descomentar)

#Avatar
class Avatar(models.Model):

    #vinculo con el usuario
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    #Subcarpeta avatares de media
    imagen=models.ImageField(upload_to='avatares', null=True,blank=True)
    
#Chat entre usuarios
# class destino(models.Model):
#     destino=models.ForeignKey(User, related_name='mensaje', on_delete=models.CASCADE)
    

# # class EnviarMensajes(models.Model):
# #     destino = models.ForeignKey(destino, related_name='mensaje', on_delete=models.CASCADE)
# #     user = models.ForeignKey(User, related_name='mensaje', on_delete=models.CASCADE)
# #     content = models.TextField()
# #     date_added = models.DateTimeField(auto_now_add=True)
# #     class Meta:
# #         ordering = ('date_added',)
