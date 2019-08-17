from django.contrib import admin
from .models import NotaFiscal

@admin.register(NotaFiscal)
class NotaFiscalAdmin(admin.ModelAdmin):
    list_display=(
        '__str__',
        'empresa',
        'serie',
        'numero',
        'descricao',
        'peso',
        'cubagem',
        )
    search_fields = ('notafiscal',)
    list_filter = ('empresa',)
# Register your models here.
