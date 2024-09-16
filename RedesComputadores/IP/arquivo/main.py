import csv


def tipos_grau_escolaridade(registros: list[list[str]]) -> list[str]:
    index_of_escolaridade = registros[0].index("DS_GRAU_ESCOLARIDADE")

    escolaridades = []
    for registro in registros[1:]:
        escolaridade = registro[index_of_escolaridade]
        if escolaridade not in escolaridades:
            escolaridades.append(escolaridade)

    return escolaridades


def codigo_tipo_grau_escolaridade(
    registros: list[list[str]],
    grau_escolaridade: str,
) -> int:
    index_of_cod_escolaridade = registros[0].index("CD_GRAU_ESCOLARIDADE")

    for registro in registros[1:]:
        if registro[index_of_cod_escolaridade + 1] == grau_escolaridade:
            return int(registro[index_of_cod_escolaridade])

    return -1


def distribuicao_grau_escolaridade(
    registros: list[list[str]],
    codigo_escolaridade: int,
) -> int:
    index_of_cod_escolaridade = registros[0].index("CD_GRAU_ESCOLARIDADE")

    soma = 0
    for registro in registros[1:]:
        codigo = registro[index_of_cod_escolaridade]
        if int(codigo) == codigo_escolaridade:
            soma += 1
    return soma


def cidades_de_escolaridade(
    registros: list[list[str]],
    codigo_escolaridade: int,
) -> set:
    index_of_cod_escolaridade = registros[0].index("CD_GRAU_ESCOLARIDADE")
    index_of_municipio = registros[0].index("NM_MUNICIPIO")

    municipios = set()
    for registro in registros[1:]:
        codigo_esc = registro[index_of_cod_escolaridade]
        if int(codigo_esc) == codigo_escolaridade:
            municipios.add(registro[index_of_municipio])

    return municipios


with open("./convocacao_mesarios_2024_BRASIL.csv", "r", encoding="latin 1") as arq:
    reader = csv.reader(arq, delimiter=";", quotechar='"')

    registros = list(reader)

    escolaridades: list[str] = tipos_grau_escolaridade(registros)
    for escolaridade in escolaridades:
        codigo = codigo_tipo_grau_escolaridade(registros, escolaridade)
        cidades = cidades_de_escolaridade(registros, codigo)
        qtd = distribuicao_grau_escolaridade(registros, codigo)
        print("Escolaridade:", escolaridade)
        print("CIDADES:", cidades)
        print("Codigo:", codigo)
        print("QTD:", qtd)
        print()

    arq.close()
