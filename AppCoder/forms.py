from django import forms

from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User
from .models import Comentario

class AutoridadesForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)
    puesto=forms.CharField(max_length=50)
    email= forms.EmailField()
    fecha_designacion=forms.DateField()

class ProfesionalForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)
    email= forms.EmailField()
    edad=forms.IntegerField()
    puesto=forms.CharField(max_length=50)

class TitulosForm(forms.Form):
    titulo=forms.CharField(max_length=50)
    ano_obtencion=forms.IntegerField()

class RegistroUsuarioForm(UserCreationForm):
    email=forms.EmailField(label="Email usuario")
    password1=forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2=forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=["username", "email", "password1", "password2"]
        help_texts = {k:"" for k in fields}

class UserEditForm(UserCreationForm):

    email= forms.EmailField(label="Email Usuario")
    password1= forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)
    
    class Meta:
        model=User
        fields=["email", "password1", "password2"]
        help_texts = {k:"" for k in fields}

class AvatarForm(forms.Form):
    imagen=forms.ImageField(label="Imagen")

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['contenido']