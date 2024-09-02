texto = input("Digite um texto: ")

qtdVogais = 0

vogais = ["a", "e", "i", "o", "u"]

for letra in texto:
    if letra.lower() in vogais:
        qtdVogais += 1

print("Quantidade de vogais:", qtdVogais)
