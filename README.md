# Nota Fiscal

###  Objetivo

Este projeto tem por objetivo criar uma API em Python para gerenciamento de notas fiscais utilizando o framework [Django].

**Django**
Django é um framework para desenvolvimento rápido para web, escrito em Python, que utiliza o padrão model-template-view. 

### Regras de negócio

Esta API tem o objetivo de prover o gerenciamento de notas fiscais de uma empresa.

**Campos da Nota Fiscal**

- Empresa (deve ter uma entidade própria)
- Série (alfanumerico)
- Número (numérico)
- Nome/Descrição
- Peso (em quilos)
- Cubagem (em metros cúbicos)
- Data

**Tarefas**

- [x] O cadastro das notas fiscais deve ser feito via Django Admin, assim como o cadastro de empresa. As únicas informações necessárias à empresa são: 
  - Nome
  - CNPJ

- [x] Crie uma página para exibir a listagem de empresas. Ao abrir os detalhes da empresa deve ser aberta a listagem de notas fiscais daquela empresa.

- [x] Adicione à listagem de notas fiscais um campo de busca por número ou nome do produto. A busca deve funcionar via GET.

- [x] Paginação é bem vinda, mas não necessária para o teste.
Você pode usar qualquer formato de Django views para este teste (CBV ou FBV)

Para a apresentação cadastre ao menos 10 empresas com 20 notas fiscais cada uma. O nome de cada empresa pode ser gerado com um lorem ipsum e os dados das notas fiscais podem ser randomicos, porém válidos.

- [x] Inclua o script de geração das empresas no anexo do projeto
- [x] Utilize arquivos externos para os dados de entrada
- [x] Inclua um CSS à página para uma aparencia agradável (pode ser Bootstrap)
- [x] A listagem de notas fiscais deve ser feita em uma tabela (HTML)

Para popular o banco de dados da aplicação utilizamos a biblioteca [Faker]. Os scripts de geração das empresas se encontram no diretório scripts.
### Instruções de uso:

1.  Faça o fork do repositório e o git clone para sua máquina. Uma vez dentro do projeto crie uma virtualenv e a ative:

```bash
    python3 -m venv env3
    source env3/bin/activate
```

2. Uma vez dentro da virtualenv (env3) vamos instalar as bibliotecas necessárias para execução do nosso código:

```bash
    pip3 install -r requirements.txt
```

3. Execute o CLI do Django para criar tabelas e o banco de dados automaticamente:

* makemigrations: Verifica as alterações das tabelas dos bancos de dados da aplicação.
* migrations: Aplica as mudanças na API.
  
```bash
    cd notafiscal/nfe/
    python3 manage.py makemigrations
    python3 manage.py migrations
```

1. Crie um super usuário para executar atividades de Django Admin na aplicação:

```bash
    python3 manage.py createsuperuser
```

5.  Para startar o servidor execute:

```bash
    python3 manage.py runserver
```


[Django]: https://docs.djangoproject.com/en/3.1/
[Faker]: https://faker.readthedocs.io/en/master/index.html#
