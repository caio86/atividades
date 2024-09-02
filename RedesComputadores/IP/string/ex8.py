texto = input("Digite um texto: ")

palavras = []
frequencia = []

# palavras = {}

for palavra in texto.split():
    aux = palavra.lower()

    # if aux not in palavras.keys():
    #     palavras[aux] = 1
    # else:
    #     palavras[aux] += 1

    indice = -1
    for i, palavra in enumerate(palavras):
        if palavra == aux:
            indice = i
            break

    if indice == -1:
        palavras.append(aux)
        frequencia.append(1)
    else:
        frequencia[indice] += 1


for i in range(len(palavras)):
    print(i, palavras[i], frequencia[i])
