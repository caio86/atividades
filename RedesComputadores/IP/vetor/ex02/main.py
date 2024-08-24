notas_validas = []

while len(notas_validas) < 10:
    nota = float(input("Digite uma nota: "))
    if 0 <= nota <= 100:
        notas_validas.append(nota)
    else:
        print("Nota inválida. Tente novamente.")

print(notas_validas)
