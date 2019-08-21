# notafiscal

##Como rodar esse projeto?
* Clone esse repositório
* Crie um virtualenv com Python 3
* Ative o virtualenv.
* Instale as dependências.
* Rode as migrações

## Instruções:
git clone https://github.com/vvalcristina/notafiscal.git
cd notafiscal
python -m venv .venv
source .venv\Scripts\activate
pip install requirements.txt
python contrib/env_gen.py
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

##Projeto:
Crie um projeto Django para gerenciar notas fiscais.

Os campos das notas são:  

- Empresa (deve ter uma entidade própria)
- Série (alfanumerico)
- Número (numérico)
- Nome/Descrição
- Peso (em quilos)
- Cubagem (em metros cúbicos)
- Data  

O cadastro das notas fiscais deve ser feito via Django Admin, assim como o cadastro de empresa.
As únicas informações necessárias à empresa são:  
- Nome
- CNPJ.  

Crie uma página para exibir a listagem de empresas.
Ao abrir os detalhes da empresa deve ser aberta a listagem de notas fiscais daquela empresa.  
Adicione à listagem de notas fiscais um campo de busca por número ou nome do produto.
A busca deve funcionar via GET.

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
