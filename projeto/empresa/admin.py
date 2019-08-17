from django.contrib import admin
from .models import Empresa

@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'cnpj',
        )
    search_fields=('cnpj',)
    list_filter=('nome',)
