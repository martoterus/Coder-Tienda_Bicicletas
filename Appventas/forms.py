
from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User


from .models import categorias

class categoriasFormulario(forms.Form):
    Nombre = forms.CharField(max_length=100)

class BicicletasFormularios(forms.Form):
    Nombre = forms.CharField(max_length=100)
    Categoria = forms.ModelChoiceField(queryset=categorias.objects.all())
    Marca = forms.CharField(max_length=30)
    Modelo = forms.CharField(max_length=30)
    Descripcion = forms.CharField(max_length=500)
    Precio = forms.FloatField()
    Rodado = forms.CharField(max_length=30)
    Color = forms.CharField(max_length=30)
    Tipo = forms.CharField(max_length=30)
    Talle = forms.CharField(max_length=30)
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
    Emial=forms.EmailField(max_length=100)
    Cargo=forms.CharField(max_length=30)

class clienteFormulario(forms.Form):

    Nombre=forms.CharField(max_length=30)
    Apellido=forms.CharField(max_length=30)
    Telefono= forms.IntegerField() 
    edad=forms.IntegerField() 
    Emial=forms.EmailField(max_length=100)
    

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



#Formulario para Registrarse
# class registroFormulario(UserCreationForm):

#     # email= forms.EmailField()
#     # password1= forms.CharField(label='Contraseña',widget=forms.PasswordInput)
#     # password2= forms.CharField(label='Repetir la contraseña',widget=forms.PasswordInput)

#     # class Meta:
#     #     model= Use 
    
    

