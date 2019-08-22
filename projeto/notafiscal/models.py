from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse_lazy

from projeto.empresa.models import Empresa

#Modelo de cadastro de notas fiscais
class NotaFiscal(models.Model):
    empresa = models.CharField('Empresa:',max_length=80, null= True, blank =True)#Nome da empresa
    serie =models.CharField('Série:',max_length=50, null= True, blank= True)#Numero de serie
    numero =models.CharField('Número:',max_length=44, null=True, unique=True)#Numero da NF
    descricao =models.TextField('Descrição/Nome:')#Nome/descricao do produto
    peso =models.IntegerField('Peso(Kg):')#Peso em kg
    cubagem = models.DecimalField('Cubagem(m³):',max_digits=8,decimal_places=2)#Cubagem em m³

    class Meta:
        ordering =('empresa',)

    def __str__(self):
        return self.empresa

    def get_absolute_url(self):
        return reverse_lazy('notafiscal:notafiscal_detail', kwargs={'pk': self.pk})
