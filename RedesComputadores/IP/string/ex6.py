numero = input("Digite um numero: ")


cont = 0

while True:
    if cont == len(numero):
        break

    print(numero[cont])

    if ord(numero[cont]) < 48 or ord(numero[cont]) > 57:
        print("Numero inválido")
        numero = input("Digite um digito novamente: ")
        cont = -1

    cont += 1
