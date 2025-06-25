<h1 align="center">📊 AutoLCPR</h1>
## Descrição
Projeto de automação criado para construir relatorios de receitas e despesas dos produtores rurais cadastrados no MS. O sistema deve:
</br> [ ] Construir uma tabela com receitas e despesas mensais;
</br> [ ] Plotar um grafico geral informando receitas e despesas anuais;
</br> [ ] Deve ser possivel tambem a inserção de registros manuais;
</br> [ ] Fornecer um relatorio com entradas, saidas, nascimentos e consumo/mortes do rebanho, para cada inscrição e total do produtor;

## Tecnologias Utilizadas
Utilizaremos para este projeto as seguintes bibliotecas:

- Python
- Pytest
- CustomTinker
- Selenium

## Demonstrações

## Testes
⚠️ É necessário a biblioteca Pytest para execucação dos testes.
<ol>CREATE
<li> Criar novo item com dados validos </li>
<li> Criar novo item com dados invalidos (falha)</li>
<li> Criar novo item sem campos obrigatórios (falha)</li>
<li> Criar novo item com dados duplicados (falha)</li>
</ol>
<ol>READ
<li> Buscar item existente</li>
<li> Buscar item inexistente (falha)</li>
<li> Listar todos os itens</li>
<li> Listar itens filtrados por atributo</li>
</ol>
<ol>UPDATE
<li> Atualizar item existente com dados validos</li>
<li> Atualizar item existente com dados invalidos (falha)</li>
<li> Atualizar item inexistente (falha)</li>
<li> Atualizar campos fixos (como ID) (falha)</li>
</ol>
<ol>DELETE
<li> Remover item existente</li>
<li> Remover item inexistente (falha)</li>
<li> Garantia de que o item foi removido</li>
</ol>