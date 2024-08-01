# Escreva um programa para ler o nome, a idade e a altura de 20 (vinte) pessoas. Calcule e exiba:
# Idade da pessoa mais nova;
# Nome e a idade da pessoa mais alta;
# Média das idades das pessoas com altura acima de 165 cm.

qtd_pessoas = 20

idade_mais_nova = float("inf")

altura_mais_alta = 0
idade_mais_alta = 0
nome_mais_alta = ""

soma_altura = 0

for i in range(qtd_pessoas):

    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    altura = int(input("Digite sua altura [cm]: "))

    if idade < idade_mais_nova:
        idade_mais_nova = idade

    if altura > altura_mais_alta:
        altura_mais_alta = altura
        nome_mais_alta = nome
        idade_mais_alta = idade

    if altura > 165:
        soma_altura += altura

media_altura_mais_alta = soma_altura / qtd_pessoas

print("Idade pessoa mais nova: ", idade_mais_nova)
print(f"{nome_mais_alta} é a pessoa mais alta com {idade_mais_alta} anos")
print("Media altura das pessoas mais altas: ", media_altura_mais_alta)
