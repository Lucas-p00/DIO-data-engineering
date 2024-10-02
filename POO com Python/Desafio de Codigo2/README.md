## Descrição do desafio

Você está desenvolvendo um sistema para organizar vendas por categorias antes de gerar um relatório. O objetivo é criar uma classe Categoria que gerencie as vendas associadas a uma determinada categoria e calcule o total de vendas dessa categoria.

1. Tarefas:

    Método **adicionar_venda**: Na classe Categoria, crie um método chamado **adicionar_venda** que adiciona um objeto Venda à lista de vendas da categoria.

    Método **total_vendas**: Na classe Categoria, crie um método chamado **total_vendas** que calcula e retorna o total das vendas (soma do valor de todas as vendas) para essa categoria.

2. Função **main**:

- **Entrada de Dados:**

    Leia o nome das categorias e, para cada categoria, leia as vendas associadas.

    Adicione cada venda à categoria correspondente usando o método adicionar_venda.

- **Exibição dos Resultados:**

    Exiba o total de vendas para cada categoria.

    Utilize o método total_vendas para calcular e exibir o total das vendas.

### Entrada

A entrada consiste em:

- Nome da Categoria (string).
- Lista de Vendas (com as colunas Produto, Quantidade, Valor).
Atenção:
O valor será o TOTAL GERAL de todos os produtos. 

### Saída
A saída é o total de vendas por categoria.