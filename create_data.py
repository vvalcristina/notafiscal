#Arquivo gerador de empresas e cnpjs
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "projeto.settings")
django.setup()

import lorem
import string
import timeit
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
    def criar_empresas(nome):
        Empresa.objects.all().delete()
        aux = []
        for nome in nomes:
            data = dict(
                    nome= nome,
                    cnpj= Num_CNPJ.cnpj(0),
            )
            obj = Empresa(**data)
            aux.append(obj)
            Empresa.objects.bulk_create(aux)

nomes= (
        'Adipisci quisquam sed dolor labore est',
        'Est sit dolorem ut etincidunt sed modi.',
        'Quiquia dolore aliquam sed porro consectetur quaerat sed.',
        'Quisquam quisquam porro porro dolorem adipisci aliquam.',
        'Amet aliquam numquam labore aliquam numquam velit.',
        'Dolore quaerat ut tempora modi sed sed.',
        'Amet labore est dolore adipisci.',
        'Dolore numquam amet sed velit tempora quisquam.',
        'Numquam aliquam adipisci modi ipsum amet.',
        'Sed ipsum ipsum modi non.',
        'Labore consectetur adipisci quaerat non porro.',

)
tic = timeit.default_timer()

EmpresaClass.criar_empresas(nomes)

toc = timeit.default_timer()

print('Tempo', toc - tic)
