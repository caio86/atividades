texto = input("Digite um texto: ")

letrasDoTexto = []

for letra in texto:
    letraLower = letra.lower()
    if letraLower.isalpha() and letraLower not in letrasDoTexto:
        letrasDoTexto.append(letraLower)

print(letrasDoTexto)
