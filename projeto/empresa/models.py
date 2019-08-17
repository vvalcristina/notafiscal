from django.db import models

class Empresa(models.Model):
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=80, null= False)

    class Meta:
        ordering = ('nome',)

    def __str__(self):
        return self.nome
