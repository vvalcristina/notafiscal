from django.db import models

class Empresa(models.Model):
    nome = models.CharField('nome',max_length=100)
    cnpj = models.CharField('cnpj',max_length=80)

    class Meta:
        ordering = ('nome',)

    def __str__(self):
        return self.nome
