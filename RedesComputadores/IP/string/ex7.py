texto = input("Digite um texto: ")

contemMinusculas = False

for letra in texto:
    if letra >= "a" and letra <= "z":
        contemMinusculas = True
        break

if not contemMinusculas:
    print("O texto só tem letra maiúsculas")
else:
    print("O texto não só tem letra maiúsculas")
