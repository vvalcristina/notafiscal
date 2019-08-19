from django.contrib import admin
from .models import NotaFiscal


@admin.register(NotaFiscal)
class NotaFiscalAdmin(admin.ModelAdmin):
    list_display = ('__str__',
            'empresa',
            'serie',
            'numero',
            'descricao',
            'peso',
            'cubagem'
    )
    search_fields =('empresa',)
    list_filter =('numero', 'descricao',)
    date_hierarchy= 'created'
# Register your models here.