from django.urls import path
from .views import *

from django.contrib.auth.views import LogoutView


urlpatterns = [
    
    path("", inicioApp, name="inicioApp"),
    #path("crear_curso/", crear_curso),
    path("autoridades/", autoridades, name="autoridades"),
    path("profesionales/", profesionales, name="profesionales"),
    path("titulos/", titulos, name="titulos"),

    path("busquedaTitulos/", busquedaTitulos, name="busquedaTitulos"),
    path("buscar/", buscar, name="buscar"),

    path("eliminarAutoridad/<id>", eliminarAutoridad, name="eliminarAutoridad"),
    path("editarAutoridad/<id>", editarAutoridad, name="editarAutoridad"),

    path("autoridades/list/", AutoridadesList.as_view(), name="autoridades_list"),
    path('autoridades/nuevo/', AutoridadesCreacion.as_view(), name='autoridades_crear'),
    path('autoridades/<pk>', AutoridadesDetalle.as_view(), name='autoridades_detalle'),
    path('autoridades/editar/<pk>', AutoridadesUpdate.as_view(), name='autoridades_editar'),
    path('autoridades/borrar/<pk>', AutoridadesDelete.as_view(), name='autoridades_borrar'),

    path("profesionales/list/", ProfesionalesList.as_view(), name="profesional_list"),
    path('profesionales/nuevo/', ProfesionalesCreacion.as_view(), name='profesional_crear'),
    path('profesionales/<pk>', ProfesionalesDetalle.as_view(), name='profesional_detalle'),
    path('profesionales/editar/<pk>', ProfesionalesUpdate.as_view(), name='profesional_editar'),
    path('profesionales/borrar/<pk>', ProfesionalesDelete.as_view(), name='profesional_borrar'),



    path("login/", login_request, name="login"),
    path("register/", register, name="register"),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('editarPerfil/', editarPerfil, name='editarPerfil'),
    path('agregarAvatar/', agregarAvatar, name='agregarAvatar')
    
    
]