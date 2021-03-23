# Nota Fiscal

###  Objetivo

Este projeto tem por objetivo criar uma API em Python para gerenciamento de notas fiscais utilizando o framework [Django](https://docs.djangoproject.com/en/3.1/).

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

- [ ] O cadastro das notas fiscais deve ser feito via Django Admin, assim como o cadastro de empresa. As únicas informações necessárias à empresa são: 
- Nome
- CNPJ.

- [ ] Crie uma página para exibir a listagem de empresas. Ao abrir os detalhes da empresa deve ser aberta a listagem de notas fiscais daquela empresa.

- [ ] Adicione à listagem de notas fiscais um campo de busca por número ou nome do produto. A busca deve funcionar via GET.

- [ ] Paginação é bem vinda, mas não necessária para o teste.
Você pode usar qualquer formato de Django views para este teste (CBV ou FBV)

Para a apresentação cadastre ao menos 10 empresas com 20 notas fiscais cada uma. O nome de cada empresa pode ser gerado com um lorem ipsum e os dados das notas fiscais podem ser randomicos, porém válidos.

- [ ] Inclua o script de geração das empresas no anexo do projeto
- [ ] Utilize arquivos externos para os dados de entrada
- [ ] Inclua um CSS à página para uma aparencia agradável (pode ser Bootstrap)
- [ ] A listagem de notas fiscais deve ser feita em uma tabela (HTML)

### Instruções de uso:

- Faça o fork do repositório e o git clone para sua máquina. Uma vez dentro do projeto crie uma virtualenv e a ative:

```
    python3 -m venv env3
    source env3/bin/activate
```

Uma vez dentro da virtualenv (env3) vamos instalar as bibliotecas necessárias para execução do nosso código:
```
    pip3 install -r requirements.txt
```

##Links:

[decouple
]https://github.com/henriquebastos/python-decouple

[Template Base]
https://getbootstrap.com/docs/4.0/getting-started/introduction/#starter-template

[Template Nav]
https://github.com/JTruax/bootstrap-starter-template/blob/master/template/start.html

[Django widget_tweaks]
https://github.com/jazzband/django-widget-tweaks

[Class Based Views-> Formato de visualização do projeto ]
https://docs.djangoproject.com/en/2.2/topics/class-based-views/intro/
https://ccbv.co.uk/

[Django Bootstrap Form]
https://django-bootstrap-form.readthedocs.io/en/latest/

[Paginação]
https://getbootstrap.com.br/docs/4.1/components/pagination/
