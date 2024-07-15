# Idade, altura e nome de 20 pessoas
# Exibir:
# idade menor
# nome e idade da pessoa mais alta
# media das idades das pessoas acime de 165cm de altura

QTD_PESSOAS = 4

mais_nova = 999

nome_mais_alta = ""
idade_mais_alta = 0
altura_mais_alta = 0

qtd_altas = 0
soma_idades = 0
media: float = 0

for _ in range(QTD_PESSOAS):
    print("Digite o nome, a idade e a altura da pessoa:")
    nome, idade, altura = input("> ").split()
    nome, idade, altura = str(nome), int(idade), int(altura)

    if idade < mais_nova:
        qtd_altas += 1
        mais_nova = idade

    if altura > altura_mais_alta:
        altura_mais_alta = altura
        idade_mais_alta = idade
        nome_mais_alta = nome

    if altura > 165:
        soma_idades += idade

media = soma_idades / qtd_altas

print(f"Idade da pessoa mais nova: {mais_nova}")
print(f"Pessoa mais alta:")
print(
    f"\tNome: {nome_mais_alta}\n\tIdade: {idade_mais_alta}\n\tAltura: {altura_mais_alta}"
)
print(f"Medias das idades de pessoas acima de 165cm: {media}")
