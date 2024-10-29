from datetime import datetime


class BombaDeCombustivel:
    def __init__(self, numero: int) -> None:
        self.numero = numero
        self.abastecimentos: list[Abastecimento] = []
        self.combustiveis: list[Combustivel] = []

    def __str__(self) -> str:
        res = ""

        combustiveis = "[ "
        combustiveis += " | ".join(map(str, self.combustiveis))
        combustiveis += " ]"

        res += f"Numero: {self.numero}\n"
        res += f"Combustiveis: {combustiveis}\n"
        res += f"Abastecimentos: {self.abastecimentos}\n"

        return res

    def registrar_abastecimento(self, abastecimento):
        self.abastecimentos.append(abastecimento)

    def calcular_valor_acumulado(self) -> float:
        soma_total = 0
        for abastecimento in self.abastecimentos:
            soma_total += abastecimento.valor

        return soma_total


class Combustivel:
    def __init__(self, tipo: str, valor: float, litros_disponiveis: float) -> None:
        self.tipo = tipo
        self.valor = valor
        self.litros_disponiveis = litros_disponiveis

    def __str__(self) -> str:
        res = ""

        res += f"Tipo: {self.tipo}\t"
        res += f"Valor: R${self.valor}\t"
        res += f"Litros Restantes: {self.litros_disponiveis}L"

        return res


class Abastecimento:
    def __init__(
        self,
        litros: float,
        tipo: str,
        valor: float,
        cliente,
    ) -> None:
        self.datahora = datetime.now()
        self.litros = litros
        self.tipo = tipo
        self.valor = valor
        self.cliente = cliente
