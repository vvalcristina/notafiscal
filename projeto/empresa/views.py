from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView, UpdateView, ListView
from .models import Empresa
from .forms import EmpresaForm


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

def empresa_detail(request, pk):
    template_name ='empresa_detail.html'
    obj = Empresa.objects.get(pk=pk)
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
