
# Create your models here.
from asyncio.windows_events import NULL
from django.db import models



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

class bicicletas(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.ForeignKey(categorias, on_delete=models.CASCADE)
    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=500)
    precio = models.IntegerField()
    rodado = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    tipo = models.CharField(max_length=30)
    talle = models.CharField(max_length=30)
    imagen = models.ImageField(upload_to= 'img', null=True)

    class Meta:
        verbose_name = "bicicleta"
        verbose_name_plural = "bicicletas"

    def __str__(self):
        return self.nombre

class indumentarias(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.ForeignKey(categorias, on_delete=models.CASCADE)
    marca = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=100)
    precio = models.FloatField()
    color = models.CharField(max_length=30)
    tipo = models.CharField(max_length=30)
    talle = models.CharField(max_length=30)
    imagen = models.ImageField(upload_to= 'img', null=True)

    class Meta:
        verbose_name = "indumentaria"
        verbose_name_plural = "indumentarias"

    def __str__(self):
        return self.nombre

class repuestos(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.ForeignKey(categorias, on_delete=models.CASCADE)
    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=100)
    precio = models.FloatField()
    imagen = models.ImageField(upload_to= 'img', null=True)

    class Meta:
        verbose_name = "repuesto"
        verbose_name_plural = "repuestos"

    def __str__(self):
        return self.nombre

class accesorios(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.ForeignKey(categorias, on_delete=models.CASCADE)
    marca = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=100)
    precio = models.FloatField()
    tipo = models.CharField(max_length=30)
    imagen = models.ImageField(upload_to= 'img', null=True)

    class Meta:
        verbose_name = "accesorio"
        verbose_name_plural = "accesorios"

    def __str__(self):
        return self.nombre
    


    

class empleado(models.Model):
    cargo=models.CharField(max_length=30)
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    telefono= models.IntegerField() 
    email=models.EmailField(max_length=100)
    user_id=models.OneToOneField(User, on_delete=models.CASCADE)   #Se vincula un empleado con el usuario id correspondiente al modelo User

    def __str__(self):
        return f"{self.nombre, self.apellido, self.cargo, self.telefono, self.email, self.user_id}"


#Avatar
class Avatar(models.Model):

    #vinculo con el usuario
    user=models.ForeignKey(User, on_delete=models.CASCADE) 
    #Subcarpeta avatares de media
    imagen=models.ImageField(upload_to='img', null=True,blank=True)
    #upload_to=donde se van a guardar las imagenes
    
#---------------------------------------------------------------------------


class EnviarMensaje(models.Model):

    name=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    email=models.EmailField(max_length=50)
    subject=models.CharField(max_length=30)
    message=models.TextField()
    # usuario=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)


