
from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User


from .models import categorias, Avatar
from django.contrib.auth.forms import UserChangeForm,UserCreationForm
from django.contrib.auth.models import User
#from Appventas.models import Avatar

from .models import categorias

class categoriasFormulario(forms.Form):
    Nombre = forms.CharField(max_length=100)

class BicicletasFormularios(forms.Form):
    Nombre = forms.CharField(max_length=100)
    Categoria = forms.ModelChoiceField(queryset=categorias.objects.all())
    Marca = forms.CharField(max_length=30)
    Modelo = forms.CharField(max_length=30)
    Descripcion = forms.CharField(max_length=500)
    Precio = forms.IntegerField()
    Rodado = forms.CharField(max_length=30)
    Color = forms.CharField(max_length=30)
    Tipo = forms.CharField(max_length=30)
    Imagen = forms.FileField()

class IndumentariasFormularios(forms.Form):
    Nombre = forms.CharField(max_length=100)
    Categoria = forms.ModelChoiceField(queryset=categorias.objects.all())
    Marca = forms.CharField(max_length=30)
    Descripcion = forms.CharField(max_length=100)
    Precio = forms.FloatField()
    Color = forms.CharField(max_length=30)
    Tipo = forms.CharField(max_length=30)
    Talle = forms.CharField(max_length=30)
    Imagen = forms.FileField()

class RepuestosFormularios(forms.Form):
    Nombre = forms.CharField(max_length=100)
    Categoria = forms.ModelChoiceField(queryset=categorias.objects.all())
    Marca = forms.CharField(max_length=30)
    Modelo = forms.CharField(max_length=30)
    Descripcion = forms.CharField(max_length=100)
    Precio = forms.FloatField()
    Imagen = forms.FileField()

class AccesoriosFormularios(forms.Form):
    Nombre = forms.CharField(max_length=100)
    Categoria = forms.ModelChoiceField(queryset=categorias.objects.all())
    Marca = forms.CharField(max_length=30)
    Descripcion = forms.CharField(max_length=100)
    Precio = forms.FloatField()
    Tipo = forms.CharField(max_length=30)
    Imagen = forms.FileField()
   

class empleadosFormulario(forms.Form):

    Nombre=forms.CharField(max_length=30)
    Apellido=forms.CharField(max_length=30)
    Telefono= forms.IntegerField() 
    Email=forms.EmailField(max_length=100)
    Cargo=forms.CharField(max_length=30)

class clienteFormulario(forms.Form):

    Nombre=forms.CharField(max_length=30)
    Apellido=forms.CharField(max_length=30)
    Telefono= forms.IntegerField() 
    edad=forms.IntegerField() 
    Email=forms.EmailField(max_length=100)
    

class enviarMensaje(forms.Form):

    Nombre=forms.CharField()
    Correo=forms.EmailField()
    Telefono=forms.CharField()
    Mensaje=forms.CharField()


class EditarUsuario(UserChangeForm):
   # lo que queresmos definir del usuario
    first_name=forms.CharField(max_length=30,label="Modificar nombre")
    last_name=forms.CharField(max_length=30,label="Modificar apellido")
    email=forms.EmailField(label="Modificar E-mail")
   # password1= forms.CharField(label="Contraseña", widget=forms.PasswordInput)
   # password2= forms.CharField(label="Repetir la Contraseña", widget=forms.PasswordInput)

    class Meta:
        model= User
        fields=['first_name','last_name','email']
        #help_texts={k:"" for k in fields}   

class FormularioMensaje(forms.Form):

    Nombre=forms.CharField(max_length=30)
    Apellido=forms.CharField(max_length=30)
    Correo=forms.EmailField(max_length=30)
    Asunto=forms.CharField(max_length=30)
    Mensaje=forms.CharField(max_length=300)
    # Usuario=forms.CharField(max_length=30)

class CrearUsuario(UserCreationForm):
     # Categoria = forms.ModelChoiceField(queryset=tipoPersonas.objects.all())
    class Meta:
        model=User
        fields=['username','password1','password2']


class EditarUsuario(forms.Form):
   # lo que queresmos definir del usuario 
    first_name=forms.CharField(max_length=30,label="Modificar nombre")
    last_name=forms.CharField(max_length=30,label="Modificar apellido")
    email=forms.EmailField(label="Modificar E-mail")
    password= forms.CharField(#Para sacar los texto de ayuda.y ocultarlos
    help_text="",
    widget= forms.HiddenInput(), required=False)
 
class AvatarFormulario(forms.ModelForm):

    class Meta:
        model=Avatar
        fields=('imagen',)    

