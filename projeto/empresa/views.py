from django.shortcuts import render
from django.views.generic import CreateView
from .models import Empresa
from .forms import EmpresaForm

def empresa_list(request):
    template_name ='empresa_list.html'
    objects = Empresa.objects.all()
    context ={'object_list' : objects}
    return render(request, template_name,context)

def empresa_detail(request, pk):
    template_name ='empresa_detail.html'
    obj = Empresa.objects.get(pk=pk)
    context ={'object' : obj}
    return render(request, template_name,context)

def empresa_add(request):
    template_name='empresa_form.html'
    return render(request,template_name)

class EmpresaCreate(CreateView):
    model = Empresa
    template_name='empresa_form.html'
    form_class=EmpresaForm
