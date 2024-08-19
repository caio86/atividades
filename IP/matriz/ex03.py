from random import randint

QTD_LINHAS = 6
QTD_COLUNAS = 40

qtdAchados = 0
maior = 0
menor = 50

matriz = [[randint(1, 20) for _ in range(QTD_COLUNAS)] for _ in range(QTD_LINHAS)]

numUsuario = int(input("Valor a ser pesquisado: "))

for linha in range(QTD_LINHAS):
    for coluna in range(QTD_COLUNAS):
        valor = matriz[linha][coluna]

        if valor == numUsuario:
            qtdAchados += 1

        maior = max(maior, valor)
        menor = min(menor, valor)

print(f"O valor {numUsuario} foi encontrado {qtdAchados} vezes")
print(f"O maior valor e {maior}")
print(f"O menor valor e {menor}")
