from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render, resolve_url
from .models import NotaFiscal,NotaFiscalItens
from .forms import NotaFiscalForm, NotaFiscalItensForm

def notafiscal_list(request):
    template_name='notafiscal_list.html'
    objects=NotaFiscal.objects.all()
    context ={'object_list': objects}
    return render(request, template_name, context)

def notafiscal_detail(request,pk):
    template_name='notafiscal_detail.html'
    obj=NotaFiscal.objects.get(pk=pk)
    context ={'object': obj}
    return render(request, template_name, context)

def notafiscal_add(request):
    template_name='notafiscal_form.html'
    notafiscal_form=NotaFiscal()
    item_notafiscal_formset= inlineformset_factory(
        NotaFiscal,
        NotaFiscalItens,
        form= NotaFiscalItensForm,
        extra=0,
        min_num=1,
        validate_min=True,
    )
    if request.method == 'POST':
        form= NotaFiscalForm(request.POST, instance=notafiscal_form, prefix='main')
        formset=item_notafiscal_formset(
            request.POST,
            instance=notafiscal_form,
            prefix='notafiscal',
        )
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            url='notafiscal:notafiscal_detail'
            return HttpResponseRedirect(resolve_url(url, form.pk))
    else:
        form=NotaFiscalForm(instance=notafiscal_form, prefix='main')
        formset=item_notafiscal_formset(instance=notafiscal_form, prefix='notafiscal')

    context = {'form':form, 'formset':formset}
    return render(request, template_name, context)
