verba = 1000.00

valor_compras: list[float] = []
descricao_compras: list[str] = []

while verba > 0:
    valor = float(input("Valor da compra: "))
    descricao = input("Descrição da compra: ")

    if verba - valor < 0:
        print("Sua verba de gastos acabou!")
        break

    verba -= valor
    valor_compras.append(valor)
    descricao_compras.append(descricao)

print("-=" * 20)

qtd_compras = len(descricao_compras)

for i in range(qtd_compras):
    print("Descrição: ", descricao_compras[i])
    print("Valor: ", valor_compras[i])

print(f"O total de suas compras foi de {qtd_compras} itens.")
