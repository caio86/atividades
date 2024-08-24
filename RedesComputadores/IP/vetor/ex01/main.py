MESES = 12
ANO = 2023

precos_anteriores = []
atual = 0.0
atual_mais_barato = 0

for mes in range(MESES):
    preco = float(input(f"Qual o preço do produto no mes {mes+1:02}/{ANO}: "))
    precos_anteriores.append(preco)

atual = float(input("Digite o preço atual do produto: "))

for preco in precos_anteriores:
    if atual < preco:
        atual_mais_barato += 1

print(f"O preço atual é menor em {atual_mais_barato} meses")
