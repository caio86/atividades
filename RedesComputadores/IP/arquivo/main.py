import csv

ARQUIVO = "./convocacao_mesarios_2024_BRASIL.csv"


def tipos_grau_escolaridade(registros: list[list[str]]) -> set[str]:
    index_of_escolaridade = registros[0].index("DS_GRAU_ESCOLARIDADE")

    return {registro[index_of_escolaridade] for registro in registros[1:]}


def codigo_tipo_grau_escolaridade(
    registros: list[list[str]],
    grau_escolaridade: str,
) -> int:
    index_of_cod_escolaridade = registros[0].index("CD_GRAU_ESCOLARIDADE")
    index_of_escolaridade = index_of_cod_escolaridade + 1

    for registro in registros[1:]:
        if registro[index_of_escolaridade] == grau_escolaridade:
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
) -> set[str]:
    index_of_cod_escolaridade = registros[0].index("CD_GRAU_ESCOLARIDADE")
    index_of_municipio = registros[0].index("NM_MUNICIPIO")

    municipios = set()
    for registro in registros[1:]:
        codigo_esc = registro[index_of_cod_escolaridade]
        if int(codigo_esc) == codigo_escolaridade:
            municipios.add(registro[index_of_municipio])

    return municipios




def get_escolaridade_data(
    registros: list[list[str]],
) -> dict[str, dict]:
    result: dict[str, dict] = {}
    for escolaridade in tipos_grau_escolaridade(registros):
        codigo = codigo_tipo_grau_escolaridade(registros, escolaridade)
        cidades = cidades_de_escolaridade(registros, codigo)
        qtd = distribuicao_grau_escolaridade(registros, codigo)

        result[escolaridade] = {
            "cidades": cidades,
            "codigo": codigo,
            "qtd": qtd,
        }
    return result


with open(ARQUIVO, "r", encoding="latin 1") as arq:
    reader = csv.reader(arq, delimiter=";", quotechar='"')

    registros = list(reader)

    data = sorted(
        get_escolaridade_data(registros).items(),
        key=lambda item: item[1]["codigo"],  # vi em um sonho
        reverse=True,
    )

    for escolaridade, escolaridade_data in data:
        print(f"{escolaridade}:")
        for col, val in escolaridade_data.items():

            if col == "cidades" and len(val) >= 10:
                print("\t", f"{col}: {len(val)} cidades")
                continue

            print("\t", f"{col}: {val}")

        print()

    arq.close()
