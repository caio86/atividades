from paciente import Paciente

from pilha import Pilha
from fila import Fila
from painel import ItemPainel, Painel


class Clinica:
    def __init__(self) -> None:
        self.__contador = 0
        self.__fila_chamada = Fila()
        self.__fila_atendimento = Fila()
        self.__pilha_atendidos = Pilha()

        self.__painel_cadastro = Painel("Cadastro")
        self.__painel_consultorio = Painel("Consultório Médico")

    def obter_senha(self):
        self.__contador += 1
        senha = f"N{self.__contador:03}"
        self.__fila_chamada.enfileirar(Paciente(senha))
        return senha

    def cadastrar_paciente(self, nome: str):
        paciente = self.__fila_chamada.desenfileirar()
        self.__painel_cadastro.chamar(ItemPainel(paciente.senha))
        paciente.nome = nome
        self.__fila_atendimento.enfileirar(paciente)

    def chamada_consultorio(self):
        pass

    def consultar_posicao(self, senha: str):
        pass

    def mostrar_painel(self):
        print()
        self.__painel_cadastro.exibir()
        print()
        self.__painel_consultorio.exibir()
        print()
