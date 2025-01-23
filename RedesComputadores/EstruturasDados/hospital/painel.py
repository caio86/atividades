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
        valores = list(map(lambda i: [i.senha, i.nome], self.__historico))
        if len(valores) == 0:
            proximo = ["", ""]
        else:
            proximo = valores[len(valores) - 1]

        res = Color.BOLD + self.__titulo + Color.END + "\n"
        res += "=" * (len(self.__titulo) + 4) + "\n"
        res += Color.BOLD + Color.RED + ">  " + Color.END
        res += f"{Color.BOLD}{proximo[0]}  {proximo[1]}{Color.END}\n   "

        for i in range(len(valores) - 2, -1, -1):
            res += f"{valores[i][0]}    {valores[i][1]}\n   "

        print(res)
