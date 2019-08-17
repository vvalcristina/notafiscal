from django.db import models

class TimeStampedModels(models.Model):
    #Atualiza a data apenas quando eu crio um arquivo
    created = models.DateTimeField(
        'criado em',
        auto_now_add=True,
        auto_now=False
    )
    #Atualiza a data apenas quando eu modifico um arquivo
    modified = models.DateTimeField(
        'modificado em',
        auto_now_add=False,
        auto_now=True
    )
    class Meta:
        #Posso utilizar em outros models como Herança de Classe
        abstract =True
