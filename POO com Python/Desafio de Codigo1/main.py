class Venda:
    def __init__(self, produto, quantidade, valor):
        self.produto = produto
        self.quantidade = quantidade
        self.valor = valor

class Relatorio:
    def __init__(self):
        self.vendas = []

    def adicionar_venda(self, venda):
      if isinstance(venda, Venda):
        self.vendas.append(venda)
      else:
        print("Erro: O objeto adicionado não é uma instância válida de Venda.")
        
    def calcular_total_vendas(self):
        total = 0
        for venda in self.vendas:
          total += venda.quantidade * venda.valor
        return total


def main():
    relatorio = Relatorio()
    
    for i in range(3):
        produto = input()
        quantidade = int(input())
        valor = float(input())
        venda = Venda(produto, quantidade, valor)
        relatorio.adicionar_venda(venda)
    
    total = relatorio.calcular_total_vendas()
    print(f"Total de Vendas: {total}")

if __name__ == "__main__":
    main()