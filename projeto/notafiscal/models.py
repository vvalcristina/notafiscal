from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse_lazy
from projeto.core.models import TimeStampedModels
from projeto.empresa.models import Empresa


class NotaFiscal(TimeStampedModels):
    empresa = models.CharField(max_length=80, null= True, blank =True)
    serie =models.CharField(max_length=50, null= True, blank= True)
    numero =models.IntegerField(default=0)
    descricao =models.CharField(max_length=300)
    peso =models.DecimalField(max_digits=8,decimal_places=2, null=False, blank=False)
    cubagem = models.DecimalField(max_digits=8,decimal_places=2)

    class Meta:
        ordering =('-created',)

    def __str__(self):
        return '{}-{}'.format(self.pk, self.empresa)

    def get_absolute_url(self):
        return reverse_lazy('notafiscal:notafiscal_detail', kwargs={'pk': self.pk})

class NotaFiscalItens(models.Model):
    notafiscal=models.ForeignKey(NotaFiscal,on_delete=models.CASCADE, related_name='notasfiscais')
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

    class Meta:
        ordering= ('pk',)

    def __str__(self):
        return '{} - {} - {}'.format(self.pk, self.notafiscal.pk, self.empresa)
