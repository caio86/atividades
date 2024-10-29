class Televisao:
    def __init__(self, can: int, vol: int, ligada=False) -> None:
        self.ligada = ligada
        self.canal = can
        self.volume = vol

    def sintonizar_canal(self, canal: int) -> None:
        self.canal = canal

    def aumentar_volume(self, nivel: int = 1) -> None:
        self.volume += nivel

    def diminuir_volume(self, nivel: int = 1) -> None:
        self.volume -= nivel

    def alternar_ligado(self):
        self.ligada = not self.ligada
