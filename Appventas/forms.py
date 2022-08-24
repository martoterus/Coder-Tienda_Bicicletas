from urllib import request
from winreg import QueryValue
from django import forms
from django.forms import HiddenInput
from django.contrib.auth.forms import UserChangeForm,UserCreationForm
from django.contrib.auth.models import User


from .models import Avatar, NosotrosAvt, categorias, perfiles, producto

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


#Registrar Usuario
class UserRegisterForm(UserCreationForm):
    username=forms.CharField(label='Usuario')
    first_name=forms.CharField(max_length=30,label="Nombre")
    email=forms.EmailField()
    password1= forms.CharField(label='Contraseña',widget=forms.PasswordInput)
    password2= forms.CharField(label='Repetir Contraseña',widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=['username','first_name','email','password1','password2']
        #saca los mensajes de ayuda.
        help_texts = {k:"" for k in fields}



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
class CambiarContraseña(UserChangeForm):
    password= forms.CharField(#Para sacar los texto de ayuda.y ocultarlos
    help_text="",
    widget= forms.HiddenInput(), required=False)
    #password0= forms.CharField(label="Contraseña actual", widget=forms.PasswordInput)
    password1= forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Repetir la Contraseña", widget=forms.PasswordInput)#El forms.passwordInput es para que se vea con asteriscos

    class Meta:
        model= User
        fields=['password']

    def clean_password2(self):
        password2=self.cleaned_data["password2"]
        if password2 != self.cleaned_data["password1"]:
            raise forms.ValidationError("Las contraseñas no coinciden")#lanzo error

        return password2 # aca podriamos modificar el dato si es necesario

    # def clean_password0(self):
    #     password=self.cleaned_data["password"]
    #     if password != self.clean_password0["password0"]:
    #         raise forms.ValidationError("Error en contraseña actual")





class AvatarFormulario(forms.ModelForm):
    imagen=forms.ImageField(label="Seleccione la imagen:")
    class Meta:#Para usasr un formulario basado en Modelos
        model=Avatar
        fields=('imagen',)

class NosotrsAvtFormulario(forms.ModelForm):

    class Meta:#Para usasr un formulario basado en Modelos
        model=NosotrosAvt
        fields=('imagen',)
    
    

