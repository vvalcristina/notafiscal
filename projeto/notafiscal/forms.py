from django import forms
from .models import NotaFiscal, NotaFiscalItens

class NotaFiscalForm(forms.ModelForm):

    class Meta:
        model= NotaFiscal
        fields= '__all__'


class NotaFiscalItensForm(forms.ModelForm):

    class Meta:
        model= NotaFiscalItens
        fields= '__all__'
