from django.db import models
from django.urls import reverse_lazy

class Empresa(models.Model):
    nome = models.CharField('nome',max_length=100, unique= True )
    cnpj = models.CharField('cnpj',max_length=14, unique=True)

    class Meta:
        ordering = ('nome',)

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse_lazy('empresa:empresa_detail', kwargs={'pk': self.pk})
