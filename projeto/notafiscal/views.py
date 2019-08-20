from django.shortcuts import render
from .models import NotaFiscal

def notafiscal_list(request):
    template_name='notafiscal_list.html'
    objects=NotaFiscal.objects.all()
    context ={'object_list': objects}
    return render(request, template_name, context)
