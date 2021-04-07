from django.db import models
from django.urls import reverse_lazy

class Empresa(models.Model):
    empresa = models.CharField('Empresa:',max_length = 44, null = True)
    cnpj = models.CharField('CNPJ:',max_length = 14, unique=True)
    class Meta:
         ordering =('empresa',)

    def __str__(self):
        return self.empresa
