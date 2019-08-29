from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView, UpdateView, ListView
from .models import Empresa
from .forms import EmpresaForm
from projeto.notafiscal.models import NotaFiscal

def empresa_list(request):
    template_name ='empresa_list.html'
    objects = Empresa.objects.all()
    context ={'object_list' : objects}
    return render(request, template_name,context)

class EmpresaList(ListView):
    #Paginação das Empresas
    model = Empresa
    template_name = 'empresa_list.html'
    paginate_by = 5

def notafiscal_list2(request, empresa):
    template_name ='notafiscal_list2.html'
    obj = Empresa.objects.filter(empresa = empresa)
    context ={'object' : obj}
    return render(request, template_name,context)

def empresa_add(request):
    template_name='empresa_form.html'
    return render(request,template_name)

class EmpresaCreate(CreateView):
    #Criar empresa
    model = Empresa
    template_name='empresa_form.html'
    form_class=EmpresaForm


class EmpresaUpdate(UpdateView):
    #Editar empresa
    model = Empresa
    template_name='empresa_form.html'
    form_class=EmpresaForm
