import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "projeto.settings")
django.setup()

import string
import timeit
from random import choice, random
from projeto.empresa.models import Empresa

class Utils:
    #Métodos genericos
    @staticmethod
    def gen_digits(max_length):
        return str(''.join(choice(string.digits) for i in range(max_length)))

class EmpresaClass:
    @staticmethod
    def criar_empresas(nomes):
        Empresa.objects.all().delete()
        aux =[]
        for nome in nomes:
            data = dict(
                nome = nome,
                cnpj = 'cnpj',
            )
            obj = Empresa(**data) #
            aux.append(obj)
        Empresa.objects.bulk_create(aux)

nomes=(
        'Empresa 1',
        'Empresa 2',
        'Empresa 3',
        'Empresa 4',
        'Empresa 5',
        'Empresa 6',
        'Empresa 7',
        'Empresa 8',
        'Empresa 9',
        'Empresa 10',
)

tic = timeit.default_timer()

EmpresaClass.criar_empresas(nomes)

toc = timeit.default_timer()

print('Tempo', toc - tic)
