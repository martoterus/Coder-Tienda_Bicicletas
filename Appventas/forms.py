from unittest.util import _MAX_LENGTH
from winreg import QueryValue
from django import forms
from django.contrib.auth.forms import UserChangeForm,UserCreationForm,PasswordChangeForm
from django.contrib.auth.models import User
#from Appventas.models import Avatar

from .models import Avatar, categorias, tipoPersonas

class categoriasFormulario(forms.Form):
    Nombre = forms.CharField(max_length=100)

class productosFormularios(forms.Form):
    Nombre = forms.CharField(max_length=100)
    Categoria = forms.ModelChoiceField(queryset=categorias.objects.all())
    Marca = forms.CharField(max_length=30)
    Modelo = forms.CharField(max_length=30)
    Descripcion = forms.CharField(max_length=100)
    Precio = forms.FloatField()
    Rodado = forms.CharField(max_length=30)
    Color = forms.CharField(max_length=30)
    Tipo = forms.CharField(max_length=30)
    Talle = forms.CharField(max_length=30)
    Disponibilidad = forms.BooleanField()


class TipoPersona(forms.Form):
    Nombre=forms.CharField(max_length=100)

# class personaFormularios(forms.Form):
#     username=forms.CharField(max_length=30,label="Nombre")
#     lastname=forms.CharField(max_length=30,label="Apellido")
#     Telefono= forms.IntegerField(label="Telefono") 
#     emial=forms.EmailField(max_length=100,label="Email")
#     Categoria = forms.ModelChoiceField(queryset=tipoPersonas.objects.all())

class clienteFormularios(forms.Form):
    
    nombre=forms.CharField(max_length=30,label="Nombre")
    apellido=forms.CharField(max_length=30,label="Apellido")
    Telefono= forms.IntegerField(label="Telefono") 
    emial=forms.EmailField(max_length=100,label="Email")
    
class empleadoFormularios(forms.Form):
    nombre=forms.CharField(max_length=30,label="Nombre")
    apellido=forms.CharField(max_length=30,label="Apellido")
    Telefono= forms.IntegerField(label="Telefono") 
    emial=forms.EmailField(max_length=100,label="Email")
    cargo=forms.CharField(max_length=30,label="Cargo")
    #Categoria = forms.ModelChoiceField(queryset=tipoPersonas.objects.all())

class CrearUsuario(UserCreationForm):
     # Categoria = forms.ModelChoiceField(queryset=tipoPersonas.objects.all())
    class Meta:
        model=User
        fields=['username','password1','password2']
    

class EditarUsuario(UserChangeForm):
   # lo que queresmos definir del usuario 
    first_name=forms.CharField(max_length=30,label="Modificar nombre")
    last_name=forms.CharField(max_length=30,label="Modificar apellido")
    email=forms.EmailField(label="Modificar E-mail")
    password= forms.CharField(#Para sacar los texto de ayuda.y ocultarlos
    help_text="",
    widget= forms.HiddenInput(), required=False)
   
   
    class Meta:#Para usasr un formulario basado en Modelos
        model= User
        fields=['first_name','last_name','email']
        #help_texts={k:"" for k in fields}   
    #agregar validacines dentro de un formularios
    #definimos metodos con:
    

#cambiar contraseña
# class CambiarContraseña(PasswordChangeForm):
#     # password= forms.CharField(#Para sacar los texto de ayuda.y ocultarlos
#     # help_text="",
#     # widget= forms.HiddenInput(), required=False)
#     # password: forms.Field
#     # #password0= forms.CharField(label="Contraseña actual", widget=forms.PasswordInput)
#     # password1= forms.CharField(label="Contraseña", widget=forms.PasswordInput)
#     # password2= forms.CharField(label="Repetir la Contraseña", widget=forms.PasswordInput)#El forms.passwordInput es para que se vea con asteriscos

#     class Meta:
#         model= User
#         fields=['password']

    def clean_password2(self):
        password2=self.cleaned_data["password2"]
        if password2 != self.cleaned_data["password1"]:
            raise forms.ValidationError("Las contraseñas no coinciden")#lanzo error

        return password2 # aca podriamos modificar el dato si es necesario

class AvatarFormulario(forms.ModelForm):

    class Meta:
        model=Avatar
        fields=('imagen',)

    

class enviarMensaje(forms.Form):

    Nombre=forms.CharField()
    Correo=forms.EmailField()
    Telefono=forms.CharField()
    Mensaje=forms.CharField()



