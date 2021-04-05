from django.shortcuts import render

from django.views.generic import CreateView, UpdateView, ListView
from .models import Empresa
from .forms import EmpresaForm
from notafiscal.models import NotaFiscal

def empresa_list(request):
    template_name ='empresa_list.html'
    objects = Empresa.objects.all()
    context ={'object_list' : objects}
    return render(request, template_name,context)

def notafiscal_list2(request, empresa):
    template_name ='notafiscal_list.html'
    obj = Empresa.objects.filter(empresa = empresa)
    context ={'object' : obj}
    return render(request, template_name,context)

def empresa_add(request):
    template_name='empresa_form.html'
    return render(request,template_name)
class EmpresaCreate(CreateView):
    model = Empresa
    template_name='empresa_form.html'
    form_class=EmpresaForm

class EmpresaList(ListView):
    model = Empresa
    template_name = 'empresa_list.html'
    paginate_by = 10

class EmpresaUpdate(UpdateView):
    model = Empresa
    template_name='empresa_form.html'
    form_class=EmpresaForm