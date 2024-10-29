class Lampada:
    def __init__(self, cor: int, potencia: int, ligada=False) -> None:
        self.ligada = ligada
        self.cor = cor
        self.potencia = potencia

    def ligar(self) -> None:
        self.ligada = True

    def desligar(self) -> None:
        self.ligada = False

    def alternar_ligada(self) -> None:
        self.ligada = not self.ligada
