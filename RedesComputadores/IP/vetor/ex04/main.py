import random

QTD_PESSOAS = 10

frutas = [
    "abacate",
    "abacaxi",
    "acerola",
    "amora",
    "banana",
    "caja",
    "caju",
    "cereja",
    "coco",
    "goiaba",
    "laranja",
]

frutas_favoritas = [""] * QTD_PESSOAS

repetiou = False

for i in range(QTD_PESSOAS):
    frutas_favoritas[i] = random.choice(frutas)

for i in range(QTD_PESSOAS):
    fruta = frutas_favoritas[i]
    contador = 0
    for fruta_atual in frutas_favoritas:
        if fruta == fruta_atual:
            contador += 1
    if contador >= 2:
        repetiou = True
        break


print(repetiou)

# if len(frutas_favoritas) != len(set(frutas_favoritas)):
#     print("Repetiu")
# else:
#     print("Nao repetiu")
