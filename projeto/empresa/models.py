from django.db import models
from django.urls import reverse_lazy

#Modelo de cadastro de empresas
class Empresa(models.Model):
    nome = models.CharField('Empresa:',max_length=100, unique= True )#Associa a empresa a nota fiscal
    cnpj = models.CharField('CNPJ:',max_length=14, unique=True)

    class Meta:
        ordering = ('nome',)

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse_lazy('empresa:empresa_detail', kwargs={'pk': self.pk})
