from django.contrib import admin
from .models import Autoridades, Profesional, Titulos, Avatar

# Register your models here.
admin.site.register(Autoridades)
admin.site.register(Profesional)
admin.site.register(Titulos)
admin.site.register(Avatar)

