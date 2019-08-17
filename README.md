# notafiscal
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
Paginação é bem vinda, mas não necessária para o teste. 
Você pode usar qualquer formato de Django views para este teste (CBV ou FBV)  

Para a apresentação cadastre ao menos 10 empresas com 20 notas fiscais cada uma.
O nome de cada empresa pode ser gerado com um lorem ipsum e os dados das notas fiscais podem ser randomicos, porém válidos. 
- Inclua o script de geração das empresas no anexo do projeto 
- Utilize arquivos externos para os dados de entrada 
- Inclua um CSS à página para uma aparência agradável (pode ser Bootstrap) 
- A listagem de notas fiscais deve ser feita em uma tabela (HTML)
