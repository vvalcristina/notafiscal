from django.shortcuts import render
from .models import Empresa

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
# Create your views here.


# Create your views here.
