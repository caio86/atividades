VALOR_CUPOM: float = 30.00


def calcularCupons(valor_compra: float) -> int:
    qtd_cupons: int = 0
    qtd_cupons += int(valor_compra // VALOR_CUPOM)
    return qtd_cupons


if __name__ == "__main__":
    print("{} cupons".format(calcularCupons(120.00)))
    print("{} cupons".format(calcularCupons(320.00)))
    print("{} cupons".format(calcularCupons(29.99)))
