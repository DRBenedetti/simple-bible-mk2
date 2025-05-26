from django.contrib import admin
from .models import Usuario

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    search_fields = ('nome', 'sobrenome', 'email', 'telefone')
    list_display = ('nome', 'sobrenome', 'email')
    readonly_fields = ('nome', 'sobrenome', 'email', 'telefone', 'senha', 'nascimento')

    