from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, ListView
from .models import NotaFiscal
from .forms import NotaFiscalForm
from django.db.models import Q

def notafiscal_list(request,empresa):
    template_name='notafiscal_list.html'
    objects=NotaFiscal.objects.filter(empresa=empresa)
    search= request.GET.get('search')
    if search:
        objects = objects.filter(Q(descricao__icontains=search) | Q(numero__icontains=search))
    context ={'object_list': objects}
    return render(request, template_name, context)
class NotaFiscalList(ListView):
    model = NotaFiscal
    template_name = 'notafiscal_list.html'    

def notafiscal_detail(request, pk):
    template_name='notafiscal_detail.html'
    obj= NotaFiscal.objects.get(pk=pk)
    context ={'object': obj}
    return render(request, template_name, context)

def notafiscal_add(request):
    template_name='notafiscal_form.html'
    return render(request, template_name)
class NotaFiscalCreate(CreateView):
    model= NotaFiscal
    template_name='notafiscal_form.html'
    form_class=NotaFiscalForm
class NotaFiscalUpdate(UpdateView):
    model= NotaFiscal
    template_name= 'notafiscal_form.html'
    form_class=NotaFiscalForm