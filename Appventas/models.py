
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
#------------------------------------------------------------------
class tipoPersonas(models.Model):
    nombre = models.CharField(max_length=100)


    # class Meta:
    #     verbose_name = "categoria"
    #     verbose_name_plural = "categorias"
    
    def __str__(self):
        return self.nombre


class Persona(models.Model):
    
    Nombre=models.CharField(max_length=30)
    Apellido=models.CharField(max_length=30)
    Telefono=models.IntegerField()
    Email=models.EmailField(max_length=30)
    Categoria = models.ForeignKey(tipoPersonas, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.Nombre


#Comentar todo: selecciono . 1°ctrl+k . 2°ctrl+c (comentar) 2°ctrl+u (descomentar)

#Avatar
class Avatar(models.Model):

    #vinculo con el usuario
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    #Subcarpeta avatares de media
    imagen=models.ImageField(upload_to='avatares', null=True,blank=True)
    
#---------------------------------------------------------------------------


class EnviarMensaje(models.Model):

    name=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    email=models.EmailField(max_length=50)
    subject=models.CharField(max_length=30)
    message=models.TextField()
    # usuario=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)