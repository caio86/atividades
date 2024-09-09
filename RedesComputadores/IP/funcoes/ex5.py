def mediaArit(n1: int, n2: int, n3: int) -> float:
    soma = n1 + n2 + n3
    return soma / 3


def mediaPond(n1: int, n2: int, n3: int) -> float:
    pesos = [2, 4, 6]
    somaNotas = n1 * pesos[0] + n2 * pesos[1] + n3 * pesos[2]
    somaPesoas = sum(pesos)
    media = somaNotas / somaPesoas
    return media


def mediaFinal(n1: int, n2: int, n3: int) -> float:
    media_aritmetica = mediaArit(n1, n2, n3)
    media_ponderada = mediaPond(n1, n2, n3)

    if media_aritmetica > media_ponderada:
        resultado = media_aritmetica
    else:
        resultado = media_ponderada

    return resultado


def conceito(n1: int, n2: int, n3: int) -> str:
    media_final = mediaFinal(n1, n2, n3)

    if media_final <= 100 and media_final >= 80:
        return "A"
    elif media_final < 80 and media_final >= 60:
        return "B"
    elif media_final < 60 and media_final >= 40:
        return "C"
    elif media_final < 40 and media_final >= 0:
        return "D"
    else:
        return "D"


def main():
    print(conceito(100, 100, 100))
    print(conceito(0, 100, 100))
    print(conceito(100, 100, 0))
    print(conceito(0, 0, 100))
    print(conceito(0, 0, 0))


main()
