from django.shortcuts import render
from django.views.generic import CreateView, UpdateView
from .models import NotaFiscal
from .forms import NotaFiscalForm

def notafiscal_list(request):
    template_name='notafiscal_list.html'
    objects=NotaFiscal.objects.all()
    context ={'object_list': objects}
    return render(request, template_name, context)

def notafiscal_detail(request, pk):
    template_name='notafiscal_detail.html'
    obj= NotaFiscal.objects.get(pk=pk)
    context ={'object': obj}
    return render(request, template_name, context)

def notafiscal_add(request):
    template_name='notafiscal_form.html'
    notafiscal_form=NotaFiscal()
    return render(request, template_name)

class NotaFiscalCreate(CreateView):
    #Criar Nota Fiscal
    model= NotaFiscal
    template_name='notafiscal_form.html'
    form_class=NotaFiscalForm

class NotaFiscalUpdate(UpdateView):
    #Editar a Nota Fiscal
    model= NotaFiscal
    template_name= 'notafiscal_form.html'
    form_class=NotaFiscalForm
