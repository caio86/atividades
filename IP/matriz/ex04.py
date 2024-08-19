from random import randint


def printar_Matriz(m: list[list[int]]):
    for i in range(len(m)):
        for j in range(len(m[i])):
            print(f"{m[i][j]:2}", end=" ")
        print()


QTD_LINHAS = 5
QTD_COLUNAS = 3

matriz = [[randint(-9, 9) for _ in range(QTD_COLUNAS)] for _ in range(QTD_LINHAS)]

transposta = [[0] * QTD_LINHAS for _ in range(QTD_COLUNAS)]

for i in range(QTD_LINHAS):
    for j in range(QTD_COLUNAS):
        transposta[j][i] = matriz[i][j]

print("Matriz gerada:")
printar_Matriz(matriz)

print("Matriz transposta:")
printar_Matriz(transposta)
