# Escreva um programa para ler vários números,
# calcule e exiba o maior número par.
# O programa deverá encerrar quando for digitado o número 0 (zero).

numero = 5
maior_par = 0

while numero != 0:
    numero = int(input("Digite um numero: "))
    if numero > maior_par and numero % 2 == 0:
        maior_par = numero
    print("O maior par é: ", maior_par)
