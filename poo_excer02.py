"""
Exercícios 2
### 🛒 **Exercício 2 – Classe `Produto`**

Crie uma classe `Produto` que represente um item de mercado.

- Atributos: `nome`, `preco`, `quantidade_estoque`
    
- Método: `vender(qtd)` que reduz o estoque
    
- Método: `repor(qtd)` que aumenta o estoque
    
- Imprima o estoque antes e depois das operações.

"""

class Produto:
    def __init__(self, nome, preco, quantidade_estoque):
        self.nome = nome
        self.preco = preco
        self.quantidade_estoque = quantidade_estoque

    def vender(self, qtd):
        if self.quantidade_estoque < qtd:
            print("Nós não temos a quantidade suficiente para a venda")
        else:
            print(f"Venda de {qtd} realizada")
            self.quantidade_estoque -= qtd

    def repor(self):
        qtd = int(input("quantos produtos serão depositados?"))
        self.quantidade_estoque += qtd
        print(f"Quantidade atualizada do produto é: {self.quantidade_estoque}")

    def exibir_infos(self):
        print(f"Nome do produto {self.nome}, preço é de {self.preco} reais e quantidade disponível {self.quantidade_estoque}")

produto01 = Produto("Sabão macaco", 2.90, 50)
produto01.vender(35)
produto01.vender(20)
produto01.exibir_infos()
produto01.repor()
produto01.vender(85)
produto01.exibir_infos()