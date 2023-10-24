from decimal import Decimal

class Produto:
    """_summary_
    """
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor


produtos = {
    "1": Produto(nome="Maça", valor=10),
    "2": Produto(nome="Melancia", valor=20)
}

print("Olá cliente, boas vindas à quitanda!")
print("Estes são os produtos disponíveis:")
for codigo, produto in produtos.items():
    print(f"{codigo} -> {produto.nome} - R$ {produto.valor}")


class Compra:
    """_summary_
    """
    def __init__(self, cliente, items):
        self.cliente = cliente
        self.items = items

    def calcula_total(self):
        """Calcula o total da compra"""
        total = 0
        for cod_produto, quantidade in self.items:
            produto = produtos[cod_produto]
            total += produto.valor * quantidade
        return Decimal(total)


compra = Compra(cliente=input("Qual o seu nome: "), items=[])

while True:
    cod_produto = input("Código do produto: [enter para sair]").strip()
    if not cod_produto:
        break
    if cod_produto not in produtos:
        print("Codigo inválido tente novamente.")
        continue
    quantidade = int(input("Quantas Unidades?:").strip())
    compra.items.append([cod_produto, quantidade])

print(f"Olá, {compra.cliente}")
print(f"No seu carringo de compras tem {len(compra.items)} item")
print(f"O total da compra é {Compra.calcula_total(compra):.2f}")



