from django.db import models
from django.urls import reverse_lazy

#Modelo de cadastro de empresas
class Empresa(models.Model):
    empresa = models.CharField('Empresa:',max_length=44, null=True, unique=True)
    cnpj = models.CharField('CNPJ:',max_length=14)

    class Meta:
         ordering =('empresa',)

    def __str__(self):
        return self.empresa

    def get_absolute_url(self):
        return reverse_lazy('empresa:empresa_detail', kwargs={'pk': self.pk})
