# Escreva um programa para ler 20 números,
# calcule e exiba o segundo maior valor.
# Considere que os valores digitados são distintos (ou seja, não repetem).

qtd_numeros = 4

maior = 0
segundo_maior = 0

for i in range(qtd_numeros):
    numero = int(input("Digite um numero: "))

    if numero > maior:
        segundo_maior = maior
        maior = numero
    elif numero > segundo_maior and numero != maior:
        segundo_maior = numero

print("Maior valor: ", maior)
print("Segundo maior valor: ", segundo_maior)
