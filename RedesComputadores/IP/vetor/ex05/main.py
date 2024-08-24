from random import randint, sample

QTD_PESSOAS = 10

media_idades = 0.0
nome_de_pessoas = [
    "Eloá Tereza Gabrielly Carvalho",
    "Aline Vitória Lopes",
    "Enrico Tomás Barbosa",
    "Mariah Eliane Rocha",
    "Stella Luna Rafaela Drumond",
    "Eloá Yasmin Fernanda Cavalcanti",
    "Emilly Gabrielly da Conceição",
    "Nair Emily dos Santos",
    "Cauã Yuri Bernardo da Silva",
    "Guilherme Antonio Nicolas Assis",
]

nomes = sample(nome_de_pessoas, QTD_PESSOAS)
idades = [randint(0, 99) for _ in range(QTD_PESSOAS)]

media_idades = sum(idades) / QTD_PESSOAS

print(media_idades)

for i in range(QTD_PESSOAS):
    if idades[i] > media_idades:
        print(nomes[i])
