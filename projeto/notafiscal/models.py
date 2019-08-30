from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse_lazy
from projeto.empresa.models import Empresa

#Modelo de cadastro de notas fiscais
class NotaFiscal(models.Model):
    empresa =models.ForeignKey(Empresa, on_delete=models.PROTECT, null=True)#Nome da empresa
    serie =models.CharField('Série:',max_length=50, null= True, blank= True)#Numero de serie
    numero =models.IntegerField('Número:')#Numero da NF
    descricao =models.CharField('Descrição/Nome:', max_length= 200)#Nome/descricao do produto
    peso =models.DecimalField('Peso(Kg):', max_digits=8, decimal_places=2)#Peso em kg
    cubagem = models.DecimalField('Cubagem(m³):',max_digits=8,decimal_places=2)#Cubagem em m³

    class Meta:
        ordering =('empresa',)

    def __str__(self):
        return self.descricao

    def get_absolute_url(self):
        return reverse_lazy('notafiscal:notafiscal_detail', kwargs={'pk': self.pk})
