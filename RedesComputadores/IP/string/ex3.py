texto = input("Digite um texto: ")

temMinuscula = False

for palavra in texto:
    if palavra >= "a" and palavra <= "z":
        temMinuscula = True
        break

if temMinuscula:
    print("Tem minuscula")
else:
    print("Não tem minuscula")
