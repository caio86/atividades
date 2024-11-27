from abc import ABC, abstractmethod
from enum import Enum


class GrausDeEscolaridade(Enum):
    MEDIO = "Ensino Médio Completo"
    SUPERIOR = "Ensino Superior Completo"
    ESPECIALISTA = "Especialização"
    MESTRE = "Mestrado"
    DOUTOR = "Doutorado"


class Funcionario(ABC):

    def __init__(self, nome, salarioBase) -> None:
        self.nome = nome
        self.salario = salarioBase

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
        self.__salario = salario

    @property
    def grau(self) -> GrausDeEscolaridade:
        return self.__grau

    @grau.setter
    def grau(self, grau) -> None:
        assert isinstance(grau, GrausDeEscolaridade), "grau deve ser parte do enum GrausDeEscolaridade"
        self.__grau: GrausDeEscolaridade = grau

    @abstractmethod
    def addBonificacao():
        pass

    def __str__(self) -> str:
        return f"Objeto do tipo {self.__class__.__name__}: {self.nome}, salário R${self.salario:.2f}"

