from django.contrib import admin
from usuario.models import Usuarios

@admin.register(Usuarios)
class UsuarioAdmin(admin.ModelAdmin):
    readonly_fields = ('nome', 'email', 'senha')