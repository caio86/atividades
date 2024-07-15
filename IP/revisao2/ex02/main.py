maior = 0

while True:
    num = int(input("Digite um número: "))

    if num % 2 == 0 and num > maior:
        maior = num

    if num == 0:
        break

print("O maior número par digitado foi:", maior)
