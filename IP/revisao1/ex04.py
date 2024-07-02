import random

VALOR_CUPOM: float = 30.00
MAX_CUPONS: int = 1000
TOTAL_CLIENTES: int = 200


def calcularCupons(valor_compra: float) -> tuple[int, float, float]:
    qtd_cupons: int = 0

    qtd_cupons += int(valor_compra // VALOR_CUPOM)
    saldo = round((valor_compra % VALOR_CUPOM), 2)
    resta = abs(VALOR_CUPOM - saldo)

    return qtd_cupons, saldo, resta


if __name__ == "__main__":
    cupons_distribuidos = 0
    cupons_nao_distribuidos = 0
    maior_venda = 0
    total_vendido = 0
    ultimo_cliente = False
    qtd_clientes_receberam_max_cupons = 0

    entradas = [random.uniform(0.01, 1000.00) for _ in range(TOTAL_CLIENTES)]

    for entrada in entradas:
        cupons, saldo, falta = calcularCupons(entrada)
        cupons_restantes = MAX_CUPONS - cupons_distribuidos

        if cupons == 0:
            cupons = "Sem"
            qtd_clientes_receberam_max_cupons += 1
        elif cupons + cupons_distribuidos >= MAX_CUPONS:
            ultimo_cliente = True
            cupons_distribuidos += cupons_restantes
            cupons_nao_distribuidos = cupons - cupons_restantes
        else:
            qtd_clientes_receberam_max_cupons += 1
            cupons_distribuidos += cupons

        maior_venda = max(maior_venda, entrada)
        total_vendido += entrada

        print(f"\nValor gasto: R$ {entrada:.2f}")
        print(f"Cupons restantes: {cupons_restantes}")
        print(f"{cupons} cupons")
        print(f"R$ {saldo:.2f} de saldo")
        print(f"R$ {falta:.2f} para novo cupom")
        print(f"{cupons_distribuidos} cupons distribuidos")

        if ultimo_cliente:
            break

    cupons_maior_venda, _, _ = calcularCupons(maior_venda)

    print("-=" * 7 + "Resultado" + "-=" * 7)
    print(f"Total vendido: R${total_vendido:.2f}")
    print(f"Cupons distribuidos: {cupons_distribuidos}")
    print(f"Maior venda: R${maior_venda:.2f} {cupons_maior_venda} cupons")
    print(f"Qtd clientes que receberam max cupons: {qtd_clientes_receberam_max_cupons}")
    print(f"Cupons nao distribuidos: {cupons_nao_distribuidos}")
