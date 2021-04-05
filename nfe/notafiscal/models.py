from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse_lazy
from empresa.models import Empresa
class NotaFiscal(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, null=True)
    serie = models.CharField('Série:',max_length=50, null= True, blank= True)
    numero = models.IntegerField('Número:')
    descricao = models.CharField('Descrição/Nome:', max_length= 200)
    peso = models.DecimalField('Peso(Kg):', max_digits=8, decimal_places=2)
    cubagem = models.DecimalField('Cubagem(m³):',max_digits=8,decimal_places=2)
    class Meta:
        ordering =('empresa',)

    def __str__(self):
        return self.descricao

    def get_absolute_url(self):
        return reverse_lazy('notafiscal:notafiscal_detail', kwargs={'pk': self.pk})