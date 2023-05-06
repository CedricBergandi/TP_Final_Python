from django.shortcuts import render
from .models import Autoridades, Profesional, Titulos, Avatar, Comentario
from .forms import AutoridadesForm, RegistroUsuarioForm, UserEditForm, AvatarForm, ComentarioForm
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy

from django.contrib.auth.forms import  UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import render, redirect, get_object_or_404

   
def profesionales(request):
    avatar= obtenerAvatar(request)
    profesionales = Profesional.objects.all().order_by('puesto')
    return render(request, "RiverPlate/profesionales.html",{"profesionales": profesionales, "avatar":avatar})


@login_required
def autoridades(request):

    if request.method == "POST":
        form = AutoridadesForm(request.POST)
        if form.is_valid():
            autoridad = Autoridad()
            autoridad.nombre = form.cleaned_data['nombre']
            autoridad.apellido = form.cleaned_data['apellido']
            autoridad.email = form.cleaned_data['email']    
            autoridad.puesto = form.cleaned_data['puesto']
            autoridad.fecha_designacion = form.cleaned_data['fecha_designacion']
            autoridad.save()
            form = AutoridadesForm()
    else:
        form = AutoridadesForm()

    autoridades = Autoridades.objects.all()

    avatar= obtenerAvatar(request)
    
    return render(request, "RiverPlate/autoridades.html", {"autoridades": autoridades, "form" : form, "avatar":avatar})

@login_required
def busquedaTitulos(request):
    
    return render(request, "RiverPlate/busquedaTitulos.html", {"avatar":obtenerAvatar(request)})

def obtenerAvatar(request):

    avatares=Avatar.objects.filter(user=request.user.id)
    if len(avatares)!=0:
        return avatares[0].imagen.url
    else:
        return "/media/avatars/avatarpordefecto.png"


def buscar(request):
    
    ano_obtencion= int(request.GET["ano_obtencion"])
    if ano_obtencion!="":
        titulos= Titulos.objects.filter(ano_obtencion__icontains=ano_obtencion)
        return render(request, "RiverPlate/resultadosBusqueda.html", {"titulos": titulos})
    return render(request, "RiverPlate/busquedaTitulos.html", {"mensaje": "Aún no hay títulos en la base de datos", "avatar":obtenerAvatar(request)})

@login_required
def eliminarAutoridad(request, id):
    autoridad=Autoridades.objects.get(id=id)
    print(autoridad)
    autoridad.delete()
    autoridades=Autoridades.objects.all()
    form = AutoridadesForm()
    return render(request, "RiverPlate/Autoridades.html", {"autoridades": autoridades, "mensaje": "Autoridad eliminado correctamente", "form": form})


@login_required
def editarAutoridad(request, id):
    autoridad=Autoridades.objects.get(id=id)
    if request.method=="POST":
        form= AutoridadesForm(request.POST)
        if form.is_valid():
            
            info=form.cleaned_data
            
            autoridad.nombre=info["nombre"]
            autoridad.apellido=info["apellido"]
            autoridad.email=info["email"]
            autoridad.puesto=info["puesto"]
            autoridad.ano_designacion=info["ano_designacion"]

            autoridad.save()
            autoridades=Autoridades.objects.all()
            form = AutoridadesForm()
            return render(request, "RiverPlate/Autoridades.html" ,{"autoridades":autoridades, "mensaje": "Autoridad editada correctamente", "form": form})
        pass
    else:
        formulario= AutoridadesForm(initial={"nombre":autoridad.nombre, "apellido":autoridad.apellido, "email":autoridad.email, "puesto":autoridad.puesto, "fecha de designación":autoridad.fecha_designacion})
        return render(request, "RiverPlate/editarAutoridad.html", {"form": formulario, "autoridad": autoridad})

@login_required
def titulos(request):
    avatar= obtenerAvatar(request)
    titulos = Titulos.objects.all().order_by('-ano_obtencion')
    return render(request, "RiverPlate/titulos.html",{"titulos":titulos,"avatar":avatar})

def inicio(request):
    return HttpResponse("Bienvenido a la pagina principal del Club Atlético River Plate")


def inicioApp(request):
    comentarios = Comentario.objects.all()
    return render(request, "RiverPlate/inicio.html", {"avatar":obtenerAvatar(request), "comentarios":comentarios})


class AutoridadesCreacion(LoginRequiredMixin, CreateView):
    model= Autoridades
    template_name="RiverPlate/autoridades_form.html"
    success_url= reverse_lazy("autoridades")
    fields=['nombre', 'apellido', 'email', 'puesto', 'fecha_designacion']

class AutoridadesDetalle(LoginRequiredMixin, DetailView):
    model=Autoridades
    template_name="RiverPlate/autoridades_detalle.html"

class AutoridadesDelete(LoginRequiredMixin, DeleteView):
    model=Autoridades
    template_name="RiverPlate/autoridades_confirm_delete.html"
    success_url= reverse_lazy("autoridades")

class AutoridadesUpdate(LoginRequiredMixin, UpdateView):
    model = Autoridades
    template_name="RiverPlate/autoridades_form.html"
    success_url = reverse_lazy('autoridades')
    fields=['nombre', 'apellido', 'email', 'puesto', 'fecha_designacion']

class ProfesionalesCreacion(LoginRequiredMixin, CreateView):
    model= Profesional
    template_name="RiverPlate/profesional_form.html"
    success_url= reverse_lazy("profesionales")
    fields=['nombre', 'apellido', 'email', 'edad', 'puesto']

class ProfesionalesDetalle(LoginRequiredMixin, DetailView):
    model=Profesional
    template_name="RiverPlate/profesional_detalle.html"

class ProfesionalesDelete(LoginRequiredMixin, DeleteView):
    model=Profesional
    template_name="RiverPlate/profesional_confirm_delete.html"
    success_url= reverse_lazy("profesionales")

class ProfesionalesUpdate(LoginRequiredMixin, UpdateView):
    model = Profesional
    template_name="RiverPlate/profesional_form.html"
    success_url = reverse_lazy('profesionales')
    fields=['nombre', 'apellido', 'email', 'edad', 'puesto']

class TitulosCreacion(LoginRequiredMixin, CreateView):
    model= Titulos
    template_name="RiverPlate/titulos_form.html"
    success_url= reverse_lazy("titulos")
    fields=['titulo', 'ano_obtencion']

class TitulosDetalle(LoginRequiredMixin, DetailView):
    model=Titulos
    template_name="RiverPlate/titulos_detalle.html"

class TitulosDelete(LoginRequiredMixin, DeleteView):
    model=Titulos
    template_name="RiverPlate/titulos_confirm_delete.html"
    success_url= reverse_lazy("titulos")

class TitulosUpdate(LoginRequiredMixin, UpdateView):
    model = Titulos
    template_name="RiverPlate/titulos_form.html"
    success_url = reverse_lazy('titulos')
    fields=['titulo', 'ano_obtencion']


def login_request(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            info=form.cleaned_data
            
            usu=info["username"]
            clave=info["password"]
            usuario=authenticate(username=usu, password=clave)
            
            if usuario is not None:
                login(request, usuario)
                return redirect('inicioApp')
            else:
                return render(request, "RiverPlate/login.html", {"form": form, "mensaje":"Usuario o contraseña incorrectos"})
        else:
            return render(request, "RiverPlate/login.html", {"form": form, "mensaje":"Usuario o contraseña incorrectos"})
    else:
        form=AuthenticationForm()
        return render(request, "RiverPlate/login.html", {"form": form})


def register(request):
    if request.method=="POST":
        form= RegistroUsuarioForm(request.POST)
        if form.is_valid():
            username= form.cleaned_data.get("username")
            form.save()
            return render(request, "RiverPlate/inicio.html", {"mensaje":f"Usuario {username} creado correctamente"})
        else:
            return render(request, "RiverPlate/register.html", {"form": form, "mensaje":"Error al crear el usuario"})
    else:
        form= RegistroUsuarioForm()
        return render(request, "RiverPlate/register.html", {"form": form})

@login_required
def editarPerfil(request):
    usuario=request.user

    if request.method=="POST":
        form=UserEditForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usuario.email=info["email"]
            usuario.password1=info["password1"]
            usuario.password2=info["password2"]
            usuario.save()
            avatar= obtenerAvatar(request)
            return render(request, "RiverPlate/inicio.html", {"mensaje":f"Usuario {usuario.username} editado correctamente", "avatar":avatar})
        else:
            avatar= obtenerAvatar(request)
            return render(request, "RiverPlate/editarPerfil.html", {"form": form, "nombreusuario":usuario.username, "avatar":avatar})
    else:
        form=UserEditForm(instance=usuario)
        avatar= obtenerAvatar(request)
        return render(request, "RiverPlate/editarPerfil.html", {"form": form, "nombreusuario":usuario.username, "avatar":avatar})

@login_required
def agregarAvatar(request):
    if request.method=="POST":
        form=AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            avatar=Avatar(user=request.user, imagen=request.FILES["imagen"])#antes de guardarlo, tengo q hacer algo
            
            avatarViejo=Avatar.objects.filter(user=request.user)
            if len(avatarViejo)>0:
                avatarViejo[0].delete()
            avatar.save()
            return render(request, "RiverPlate/inicio.html", {"mensaje":f"Avatar agregado correctamente", "avatar":obtenerAvatar(request)})
        else:
            return render(request, "RiverPlate/agregarAvatar.html", {"form": form, "usuario": request.user, "mensaje":"Error al agregar el avatar"})
    else:
        form=AvatarForm()
        return render(request, "RiverPlate/agregarAvatar.html", {"form": form, "usuario": request.user, "avatar":obtenerAvatar(request)})

def acercaDeMi(request):
    avatar= obtenerAvatar(request)
    return render(request, 'RiverPlate/acercaDeMi.html', {"avatar":avatar})


@login_required
def nuevo_comentario(request):
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.autor = request.user
            comentario.save()
            return redirect('inicioApp')
    else:
        form = ComentarioForm()
    return render(request, 'RiverPlate/nuevo_comentario.html', {'form': form})