from django.db import models
from django.contrib.auth.models import User

class Autoridades(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    puesto=models.CharField(max_length=50)
    email= models.EmailField()
    fecha_designacion=models.DateField()   
    def __str__(self):
        return f"{self.nombre} - {self.apellido}"    

class Profesional(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email= models.EmailField()
    edad=models.IntegerField()   
    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - Edad: {self.edad}"

class Reserva(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email= models.EmailField()
    edad=models.IntegerField()   
    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - Edad: {self.edad}"

class Femenino(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email= models.EmailField()
    edad=models.IntegerField()   
    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - Edad: {self.edad}"

class Titulos(models.Model):
    titulo=models.CharField(max_length=50)
    ano_obtencion=models.IntegerField()   
    def __str__(self):
        return f"Título: {self.nombre} - Año obtención: {self.ano_obtencion}"


class Avatar(models.Model):
    imagen= models.ImageField(upload_to="avatars")
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    