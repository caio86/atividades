from color import Color


class ItemPainel:
    def __init__(self, senha: str, nome: str = "") -> None:
        self.__senha = senha
        self.__nome = nome

    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def senha(self) -> str:
        return self.__senha


class Painel:
    def __init__(self, titulo: str, max=3) -> None:
        self.__titulo = titulo
        self.__historico = []
        self.__max_historico = max

    def chamar(self, item: ItemPainel):
        if len(self.__historico) >= self.__max_historico:
            self.__historico.pop(0)
        self.__historico.append(item)

    def exibir(self):
        valores = map(lambda i: [i.nome], self.__historico)
        res = Color.BOLD + self.__titulo + Color.END + "\n"
        res += "=" * (len(self.__titulo) + 4) + "\n" + Color.RED + ">  " + Color.END
        for v in valores:
            res += str(v[0]) + "\n   "

        print(res)
