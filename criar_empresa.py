#Arquivo gerador de empresas e cnpjs
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "projeto.settings")
django.setup()

import lorem
import string
import random
from projeto.empresa.models import Empresa

class Num_CNPJ:
    @staticmethod
    def cnpj(self, punctuation = False):
        n = [random.randrange(10) for i in range(8)] + [0, 0, 0, 1]
        v = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5, 6]
        # calcula dígito 1 e acrescenta ao total
        s = sum(x * y for x, y in zip(reversed(n), v))
        d1 = 11 - s % 11
        if d1 >= 10:
          d1 = 0
        n.append(d1)
        # idem para o dígito 2
        s = sum(x * y for x, y in zip(reversed(n), v))
        d2 = 11 - s % 11
        if d2 >= 10:
          d2 = 0
        n.append(d2)
        if punctuation:
          return "%d%d.%d%d%d.%d%d%d/%d%d%d%d-%d%d" % tuple(n)
        else:
          return "%d%d%d%d%d%d%d%d%d%d%d%d%d%d" % tuple(n)

class EmpresaClass:
    @staticmethod
    def criar_empresas(empresa):
        Empresa.objects.all().delete()
        aux = []
        for empresa in range(10):
            data = dict(
                    empresa= lorem.sentence(),
                    cnpj= Num_CNPJ.cnpj(0),
            )
            obj = Empresa(**data)
            aux.append(obj)
            Empresa.objects.bulk_create(aux)

EmpresaClass.criar_empresas(empresa)
