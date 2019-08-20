from django.shortcuts import render
from .models import NotaFiscal

def notafiscal_list(request):
    template_name='notafiscal_list.html'
    objects=NotaFiscal.objects.all()
    context ={'object_list': objects}
    return render(request, template_name, context)

def notafiscal_detail(request):
    template_name='notafiscal_detail.html'
    obj=NotaFiscal.objects.get(pk=pk)
    context ={'object': obj}
    return render(request, template_name, context)
