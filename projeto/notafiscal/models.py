from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse_lazy

from projeto.empresa.models import Empresa


class NotaFiscal(models.Model):
    empresa = models.CharField(max_length=80, null= True, blank =True)
    serie =models.CharField(max_length=50, null= True, blank= True)
    numero =models.IntegerField(default=0)
    descricao =models.CharField(max_length=300)
    peso =models.DecimalField(max_digits=8,decimal_places=2, null=False, blank=False)
    cubagem = models.DecimalField(max_digits=8,decimal_places=2)

    class Meta:
        ordering =('empresa',)

    def __str__(self):
        return self.empresa

    def get_absolute_url(self):
        return reverse_lazy('notafiscal:notafiscal_detail', kwargs={'pk': self.pk})
