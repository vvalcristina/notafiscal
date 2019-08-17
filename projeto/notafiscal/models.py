from django.contrib.auth.models import User
from django.db import models
from projeto.core.models import TimeStampedModels
from projeto.empresa.models import Empresa

class NotaFiscal(TimeStampedModels):
    empresa = models.CharField(max_length=80, null= True, blank =True, unique=True)
    serie =models.CharField(max_length=50, null= True, blank= True)
    numero =models.DecimalField(max_digits=8, decimal_places=4, null=False, blank=False)
    descricao =models.CharField(max_length=300)
    peso =models.DecimalField(max_digits=8,decimal_places=2, null=False, blank=False)
    cubagem = models.DecimalField(max_digits=8,decimal_places=2)

    class Meta:
        ordering =('-created',)

    def __str__(self):
        return str(self.pk)
