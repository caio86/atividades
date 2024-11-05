from datetime import datetime


class Videogame:
    _ultimo_numero_serie = 0

    def __init__(
        self,
        data_fabricacao: datetime = datetime.now(),
        marca="Sony",
        modelo="PS2",
    ):
        self.num_serie = self._new_numero_serie()
        self.data_de_fabricacao = data_fabricacao
        self.marca = marca
        self.modelo = modelo
        self.capacidade_hd = 500
        self.anos_garantia = 2
        self.jogos_instalados = []

    @classmethod
    def _new_numero_serie(cls) -> int:
        cls._ultimo_numero_serie += 1
        return cls._ultimo_numero_serie

    def __str__(self) -> str:
        res = "-=" * 25

        res += f"\nNumero serie:\t\t{self.num_serie}\n"
        res += f"Marca:\t\t\t{self.marca}\n"
        res += f"Modelo:\t\t\t{self.modelo}\n"
        res += f"Data de fabricação:\t{self.data_de_fabricacao}\n"

        if len(self.jogos_instalados) > 0:
            res += "\njogos: {\n"
            for jogo in self.jogos_instalados:
                res += f"\t{jogo},\n"
            res += "}\n"

        return res
