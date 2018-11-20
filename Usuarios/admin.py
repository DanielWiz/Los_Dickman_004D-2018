from django.contrib import admin,auth
from Usuarios.models import PerfilUsuario, PerrosRescatados

# Register your models here.
admin.site.register(PerfilUsuario)
admin.site.register(PerrosRescatados)