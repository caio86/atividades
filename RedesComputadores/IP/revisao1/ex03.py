import random

VALOR_CUPOM: float = 30.00


def calcularCupons(valor_compra: float) -> tuple[int, float, float]:
    qtd_cupons: int = 0

    qtd_cupons += int(valor_compra // VALOR_CUPOM)
    saldo = round((valor_compra % VALOR_CUPOM), 2)
    resta = abs(VALOR_CUPOM - saldo)

    return qtd_cupons, saldo, resta


if __name__ == "__main__":
    cupons_distribuidos = 0
    maior_venda = 0
    total_vendido = 0

    entradas = [random.uniform(0.01, 1000.00) for _ in range(200)]

    print(f"Deseja usar valores aleatorios S/N")
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
        else:
            cupons_distribuidos += cupons

        maior_venda = max(maior_venda, entrada)
        total_vendido += entrada

        print(f"\nValor gasto: R$ {entrada:.2f}")
        print(f"{cupons} cupons")
        print(f"R$ {saldo:.2f} de saldo")
        print(f"R$ {resta:.2f} para novo cupom")

    cupons_maior_venda, _, _ = calcularCupons(maior_venda)

    print("-=" * 7 + "Resultado" + "-=" * 7)
    print(f"Total vendido: R${total_vendido:.2f}")
    print(f"Cupons distribuidos: {cupons_distribuidos}")
    print(f"Maior venda: R${maior_venda:.2f} {cupons_maior_venda} cupons")
