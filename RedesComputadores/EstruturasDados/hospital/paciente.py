class Paciente:
    def __init__(self, nome, senha) -> None:
        self.__nome: str = nome
        self.__senha = senha

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome) -> None:
        self.__nome = nome

    @property
    def senha(self) -> str:
        return self.__senha

    @senha.setter
    def senha(self, senha) -> None:
        self.__senha = senha

    def __str__(self) -> str:
        return f"{self.senha} {self.nome}"
