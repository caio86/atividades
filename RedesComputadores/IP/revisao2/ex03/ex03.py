QTD_LEITURAS = 20

maior = 0
segundo_maior = 0

for _ in range(QTD_LEITURAS):
    leitura = int(input("Digite um valor: "))

    if leitura > maior:
        segundo_maior = maior
        maior = leitura
    elif leitura > segundo_maior:
        segundo_maior = leitura

print("O segundo maior valor é:", segundo_maior)
