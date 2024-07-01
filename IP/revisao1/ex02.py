VALOR_CUPOM: float = 30.00


def calcularCupons(valor_compra: float) -> tuple[int, float, float]:
    qtd_cupons: int = 0

    qtd_cupons += int(valor_compra // VALOR_CUPOM)
    saldo = round((valor_compra % VALOR_CUPOM), 2)
    resta = abs(VALOR_CUPOM - saldo)

    return qtd_cupons, saldo, resta


if __name__ == "__main__":
    entradas = [120.00, 29.99]

    print(f"Deseja usar os valores de teste? {entradas} S/N")
    if input().lower() == "n":
        print("Digite os valores separados por um espaço:")
        while True:
            try:
                entradas = input().split(" ")
                entradas = [float(x) for x in entradas]
            except Exception as e:
                print("Ocorreu um erro: {}".format(e))
                continue
            break

    for entrada in entradas:
        cupons, saldo, resta = calcularCupons(entrada)

        if cupons == 0:
            cupons = "Sem"

        print(f"\nValor gasto: R$ {entrada:.2f}")
        print(f"{cupons} cupons")
        print(f"R$ {saldo:.2f} de saldo")
        print(f"R$ {resta:.2f} para novo cupom")
