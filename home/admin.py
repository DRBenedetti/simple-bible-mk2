from django.contrib import admin
from .models import Tema, Versiculo

@admin.register(Tema)
class TemaAdmin(admin.ModelAdmin):
    search_fields = ('nome',)


@admin.register(Versiculo)
class VersiculoAdmin(admin.ModelAdmin):
    search_fields = ('referencia',)
    