from faker import Faker

Faker.seed(0)
fake = Faker('pt_br')

with open('empresas.csv', 'w', encoding='utf-8') as arquivo:
    arquivo.write('empresa,cnpj\n')
    for item in range(10):
        arquivo.write(f'{fake.bs()},{fake.cnpj()}\n')
