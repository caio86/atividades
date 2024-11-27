from abc import ABC, abstractmethod
from enum import Enum


class GrausDeEscolaridade(Enum):
    MEDIO = "Ensino Médio Completo"
    SUPERIOR = "Ensino Superior Completo"
    ESPECIALISTA = "Especialização"
    MESTRE = "Mestrado"
    DOUTOR = "Doutorado"


class Funcionario(ABC):

    def __init__(
        self,
        nome: str,
        salarioBase: float,
        grau: GrausDeEscolaridade = GrausDeEscolaridade.MEDIO,
    ) -> None:
        self.nome = nome
        self.salario = salarioBase
        self.grau = grau

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome) -> None:
        assert type(nome) == str
        self.__nome = nome

    @property
    def salario(self) -> float:
        return self.__salario

    @salario.setter
    def salario(self, salario) -> None:
        assert type(salario) == float
        assert salario >= 0
        self.__salario = salario

    @property
    def grau(self) -> GrausDeEscolaridade:
        return self.__grau

    @grau.setter
    def grau(self, grau) -> None:
        assert isinstance(
            grau, GrausDeEscolaridade
        ), "grau deve ser parte do enum GrausDeEscolaridade"
        self.__grau: GrausDeEscolaridade = grau

    def adicionalDeQualificacao(self) -> float:
        # Além disso, acrescenta-se o adicional de qualificação: 15%
        # especialista, 25% mestre e 50% doutor;
        match self.grau:
            case GrausDeEscolaridade.DOUTOR:
                return self.salario * 0.5
            case GrausDeEscolaridade.MESTRE:
                return self.salario * 0.25
            case GrausDeEscolaridade.ESPECIALISTA:
                return self.salario * 0.15
            case _:
                return 0

    def contracheque(self):
        return self.salario + self.addBonificacao()

    @abstractmethod
    def addBonificacao(self) -> float:
        pass

    def __str__(self) -> str:
        return f"Objeto do tipo {self.__class__.__name__}: {self.nome}, salário R${self.contracheque():.2f}"
