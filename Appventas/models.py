
# Create your models here.
from cProfile import label
import uuid
from django.db import models
from django.contrib.auth.models import User
#from django.db.models.query import QuerySet
from django.db.models import Count
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


class EnviarMensajes(models.Model):

    nombre=models.CharField(max_length=30)
    correo=models.EmailField(max_length=30)
    telefono=models.CharField(max_length=30)
    mensaje=models.CharField(max_length=100)
       
    def __str__(self):
        return f"{self.nombre,self.correo,self.telefono, self.mensaje}"

#Comentar todo: selecciono . 1°ctrl+k . 2°ctrl+c (comentar) 2°ctrl+u (descomentar)

#Avatar
class Avatar(models.Model):

    #vinculo con el usuario
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    #Subcarpeta avatares de media
    imagen=models.ImageField(upload_to='avatares', null=True,blank=True)
    
#Chat entre usuarios
class ChatModeloBase(models.Model):
    id = models.UUIDField(default=uuid.uuid4,primary_key=True,db_index=True,editable=False)
    #editable: no se puede editar
    tiempo= models.DateTimeField(auto_now_add=True)
    actualizar= models.DateTimeField(auto_now=True)

    class Meta:#no crea ninguna taba en la base de datos, solo cuando sea heredada en otra clase
        abstract = True

#asi van a tomar los ID de nuestras tarjetas con uuid.uuid4: UUID('155bcf1f-fd2e-4b0e-bde4-70e44d0adba5')
 
class ChatMensaje(ChatModeloBase):#se usan comillas porque esta clase esta arriba de la otra clase q hace referncia, sino iria sin comillas
    canal= models.ForeignKey("Canal",on_delete=models.CASCADE)
    usuario=models.ForeignKey(User, on_delete=models.CASCADE)#cuando se elimina el usuario elimina todo a lo q se le hace referencia
    texto= models.TextField()

class CanalUsuario(ChatModeloBase):
    canal = models.ForeignKey("Canal", null=True,on_delete=models.SET_NULL)
    usuario=models.ForeignKey(User,on_delete=models.CASCADE)


class CanalQuerySet(models.QuerySet):

	def solo_uno(self):
		return self.annotate(num_usuarios=Count("usuarios")).filter(num_usuarios=1)

	def solo_dos(self):
		return self.annotate(num_usuarios=Count("usuarios")).filter(num_usuarios=2)

	def filtrar_por_username(self, username):#para filtrar por usuario
		return self.filter(canalusuario__usuario__username=username)
                    #agarramos nutra clase CanalUsuario y le sacamos las mayuculas

class CanalManager(models.Manager):
                                    #contexto del diccionario
    def get_queryset(self, *args,**kwargs):
        return CanalQuerySet(self.model,using=self._db)

    def filtrar_ms_por_privado(self,username_a,username_b):
        return self.get_queryset().solo_dos().filtrar_por_username(username_a).filtrar_por_username(username_b)
class Canal(ChatModeloBase):
    #como funciona slak
    #1user a uno
    #2 users
    #2+

    usuarios= models.ManyToManyField(User,blank=True,through=CanalUsuario)
    #muchos usuarios se van a poder agregar. 
    objects = CanalManager()# sin esto aparece el siguiente error en el test: AttributeError: 'QuerySet' object has no attribute 'solo_uno'



