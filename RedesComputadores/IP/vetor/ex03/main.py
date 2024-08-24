from random import randint

QTD_NUMEROS = 6

numeros = [randint(1, 20) for _ in range(QTD_NUMEROS)]

chutes_dentro = 0

chute = int(input("Digite um numero entre 1 e 20: "))

for i in range(QTD_NUMEROS):
    if numeros[i] == chute:
        chutes_dentro += 1

print(numeros)
if chutes_dentro > 0:
    print("Voce acertou!")
    print(f"{chute} se repete {chutes_dentro} vezes.")
else:
    print("Voce errou!")
