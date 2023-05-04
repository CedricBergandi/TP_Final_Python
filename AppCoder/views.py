from django.shortcuts import render
from .models import Autoridades, Profesional, Titulos, Avatar, Mensaje
from .forms import AutoridadesForm, RegistroUsuarioForm, UserEditForm, AvatarForm, FormularioMensaje
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy

from django.contrib.auth.forms import  UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

   
def profesionales(request):
    avatar= obtenerAvatar(request)
    return render(request, "AppCoder/profesionales.html",{"avatar":avatar})


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
    
    return render(request, "AppCoder/autoridades.html", {"autoridades": autoridades, "form" : form, "avatar":avatar})

@login_required
def busquedaTitulos(request):
    
    return render(request, "AppCoder/busquedaTitulos.html", {"avatar":obtenerAvatar(request)})

def obtenerAvatar(request):

    avatares=Avatar.objects.filter(user=request.user.id)
    if len(avatares)!=0:
        return avatares[0].imagen.url
    else:
        return "/media/avatars/avatarpordefecto.png"



@login_required
def buscar(request):
    
    ano_obtencion= int(request.GET["ano_obtencion"])
    if ano_obtencion!="":
        titulos= Titulos.objects.filter(ano_obtencion__icontains=ano_obtencion)
        return render(request, "AppCoder/resultadosBusqueda.html", {"titulos": titulos})
    return render(request, "AppCoder/busquedaTitulos.html", {"mensaje": "Aún no hay títulos en la base de datos", "avatar":obtenerAvatar(request)})

@login_required
def eliminarAutoridad(request, id):
    autoridad=Autoridades.objects.get(id=id)
    print(autoridad)
    autoridad.delete()
    autoridades=Autoridades.objects.all()
    form = AutoridadesForm()
    return render(request, "AppCoder/Autoridades.html", {"autoridades": autoridades, "mensaje": "Autoridad eliminado correctamente", "form": form})


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
            return render(request, "AppCoder/Autoridades.html" ,{"autoridades":autoridades, "mensaje": "Autoridad editada correctamente", "form": form})
        pass
    else:
        formulario= AutoridadesForm(initial={"nombre":autoridad.nombre, "apellido":autoridad.apellido, "email":autoridad.email, "puesto":autoridad.puesto, "fecha de designación":autoridad.fecha_designacion})
        return render(request, "AppCoder/editarAutoridad.html", {"form": formulario, "autoridad": autoridad})

@login_required
def titulos(request):
    avatar= obtenerAvatar(request)
    return render(request, "AppCoder/titulos.html",{"avatar":avatar})

def inicio(request):
    return HttpResponse("Bienvenido a la pagina principal del Club Atlético River Plate")


def inicioApp(request):

    return render(request, "AppCoder/inicio.html", {"avatar":obtenerAvatar(request)})


class AutoridadesList(LoginRequiredMixin, ListView):
    model= Autoridades
    template_name= "AppCoder/autoridades.html"

class AutoridadesCreacion(LoginRequiredMixin, CreateView):
    model= Autoridades
    success_url= reverse_lazy("autoridades_list")
    fields=['nombre', 'apellido', 'email', 'puesto', 'fecha_designacion']

class AutoridadesDetalle(LoginRequiredMixin, DetailView):
    model=Autoridades
    template_name="Appcoder/autoridades_detalle.html"

class AutoridadesDelete(LoginRequiredMixin, DeleteView):
    model=Autoridades
    success_url= reverse_lazy("autoridades_list")

class AutoridadesUpdate(LoginRequiredMixin, UpdateView):
    model = Autoridades
    success_url = reverse_lazy('autoridades_list')
    fields=['nombre', 'apellido', 'email', 'puesto', 'fecha_designacion']

class ProfesionalesList(LoginRequiredMixin, ListView):
    model= Profesional
    template_name= "AppCoder/profesionales.html"

class ProfesionalesCreacion(LoginRequiredMixin, CreateView):
    model= Profesional
    success_url= reverse_lazy("profesional_list")
    fields=['nombre', 'apellido', 'email', 'edad', 'puesto']

class ProfesionalesDetalle(LoginRequiredMixin, DetailView):
    model=Profesional
    template_name="Appcoder/profesionales_detalle.html"

class ProfesionalesDelete(LoginRequiredMixin, DeleteView):
    model=Profesional
    success_url= reverse_lazy("profesional_list")

class ProfesionalesUpdate(LoginRequiredMixin, UpdateView):
    model = Profesional
    success_url = reverse_lazy('profesional_list')
    fields=['titulo', 'ano_obtencion']

class TitulosList(LoginRequiredMixin, ListView):
    model= Titulos
    template_name= "AppCoder/titulos.html"

class TitulosCreacion(LoginRequiredMixin, CreateView):
    model= Titulos
    success_url= reverse_lazy("titulos_list")
    fields=['titulo', 'ano_obtencion']

class TitulosDetalle(LoginRequiredMixin, DetailView):
    model=Titulos
    template_name="Appcoder/titulos_detalle.html"

class TitulosDelete(LoginRequiredMixin, DeleteView):
    model=Titulos
    success_url= reverse_lazy("titulos_list")

class TitulosUpdate(LoginRequiredMixin, UpdateView):
    model = Titulos
    success_url = reverse_lazy('titulos_list')
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
                return render(request, "AppCoder/inicio.html", {"mensaje":f"Usuario {usu} logueado correctamente"})
            else:
                return render(request, "AppCoder/login.html", {"form": form, "mensaje":"Usuario o contraseña incorrectos"})
        else:
            return render(request, "AppCoder/login.html", {"form": form, "mensaje":"Usuario o contraseña incorrectos"})
    else:
        form=AuthenticationForm()
        return render(request, "AppCoder/login.html", {"form": form})




def register(request):
    if request.method=="POST":
        form= RegistroUsuarioForm(request.POST)
        if form.is_valid():
            username= form.cleaned_data.get("username")
            form.save()
            return render(request, "AppCoder/inicio.html", {"mensaje":f"Usuario {username} creado correctamente"})
        else:
            return render(request, "AppCoder/register.html", {"form": form, "mensaje":"Error al crear el usuario"})
    else:
        form= RegistroUsuarioForm()
        return render(request, "AppCoder/register.html", {"form": form})

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
            usuario.first_name=info["first_name"]
            usuario.last_name=info["last_name"]
            usuario.save()
            return render(request, "AppCoder/inicio.html", {"mensaje":f"Usuario {usuario.username} editado correctamente"})
        else:
            return render(request, "AppCoder/editarPerfil.html", {"form": form, "nombreusuario":usuario.username})
    else:
        form=UserEditForm(instance=usuario)
        return render(request, "AppCoder/editarPerfil.html", {"form": form, "nombreusuario":usuario.username})

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
            return render(request, "AppCoder/inicio.html", {"mensaje":f"Avatar agregado correctamente", "avatar":obtenerAvatar(request)})
        else:
            return render(request, "AppCoder/agregarAvatar.html", {"form": form, "usuario": request.user, "mensaje":"Error al agregar el avatar"})
    else:
        form=AvatarForm()
        return render(request, "AppCoder/agregarAvatar.html", {"form": form, "usuario": request.user, "avatar":obtenerAvatar(request)})

def acercaDeMi(request):
    avatar= obtenerAvatar(request)
    return render(request, 'AppCoder/acercaDeMi.html', {"avatar":avatar})

class MensajePagina(LoginRequiredMixin, CreateView):
    model = Mensaje
    form_class = FormularioMensaje
    template_name = 'AppCoder/mensajeria.html'
    success_url = reverse_lazy('padre')

    def form_valid(self, form):
        form.instance.mensajeria_id = self.kwargs['pk']
        return super(Mensaje, self).form_valid(form)