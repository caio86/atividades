import csv

ARQUIVO = "./convocacao_mesarios_2024_BRASIL.csv"
INDEX_COD_ESCOLARIDADE = 14
INDEX_ESCOLARIDADE = 15
INDEX_MUNICIPIO = 6
INDEX_SG_UF = 4


def tipos_grau_escolaridade(registros: list[list[str]]) -> set[str]:
    return {registro[INDEX_ESCOLARIDADE] for registro in registros[1:]}


def codigo_tipo_grau_escolaridade(
    registros: list[list[str]],
    grau_escolaridade: str,
) -> int:
    for registro in registros[1:]:
        if registro[INDEX_ESCOLARIDADE] == grau_escolaridade:
            return int(registro[INDEX_COD_ESCOLARIDADE])

    return -1


def distribuicao_grau_escolaridade(
    registros: list[list[str]],
    codigo_escolaridade: int,
) -> int:
    soma = 0
    for registro in registros[1:]:
        codigo = registro[INDEX_COD_ESCOLARIDADE]
        if int(codigo) == codigo_escolaridade:
            soma += 1
    return soma


def cidades_de_escolaridade(
    registros: list[list[str]],
    codigo_escolaridade: int,
) -> set[str]:
    municipios = set()
    for registro in registros[1:]:
        codigo_esc = registro[INDEX_COD_ESCOLARIDADE]
        if int(codigo_esc) == codigo_escolaridade:
            municipios.add(registro[INDEX_MUNICIPIO])

    return municipios


def get_estados(
    registros: list[list[str]],
) -> set[str]:
    estados = set()
    for registro in registros[1:]:
        estados.add(registro[INDEX_SG_UF])
    return estados


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


def get_escolaridade_data_by_estado(
    registros: list[list[str]],
    estados: set[str],
) -> dict[str, dict[str, dict]]:
    resultado = {}
    for estado in estados:
        tmp = []
        for registro in registros[1:]:
            if registro[INDEX_SG_UF] == estado:
                tmp.append(registro)
        resultado[estado] = get_escolaridade_data(tmp)

    return resultado


def print_escolaridade_data(data):
    for escolaridade, escolaridade_data in data:
        print(f"{escolaridade}:")
        for col, val in escolaridade_data.items():
            if col == "cidades" and len(val) >= 10:
                print("\t", f"{col}: {len(val)} cidades")
                continue

            print("\t", f"{col}: {val}")
        print()


def print_escolaridade_data_com_estados(data):
    for estado, estado_data in data.items():
        print(f"{estado}:")
        for escolaridade, escolaridade_data in estado_data:
            print(f"  {escolaridade}:")
            for col, val in escolaridade_data.items():
                if col == "cidades" and len(val) >= 10:
                    print("\t", f"{col}: {len(val)} cidades")
                    continue

                print("\t", f"{col}: {val}")
            print()
        print()


with open(ARQUIVO, "r", encoding="latin 1") as arq:
    input = input("Printar separado por estado? [s/N] ")

    reader = csv.reader(arq, delimiter=";", quotechar='"')

    registros = list(reader)

    if input.lower() == "s":
        data = {}

        # Ordenar pelo codigo da escolariade
        for key, items in get_escolaridade_data_by_estado(
            registros,
            get_estados(registros),
        ).items():
            data[key] = sorted(
                items.items(),
                key=lambda item: item[1]["codigo"],  # vi em um sonho
                reverse=True,
            )

        print_escolaridade_data_com_estados(data)
    else:
        data = sorted(
            get_escolaridade_data(registros).items(),
            key=lambda item: item[1]["codigo"],  # vi em um sonho
            reverse=True,
        )

        print_escolaridade_data(data)

    arq.close()
