from color import Color

from fila import Fila, FilaException
from paciente import Paciente
from painel import ItemPainel, Painel


class Clinica:
    __contador = 0

    def __init__(self) -> None:
        self.__fila_chamada = Fila()
        self.__fila_atendimento = Fila()

        self.__painel_cadastro = Painel("Cadastro")
        self.__painel_consultorio = Painel("Consultório Médico")

    @classmethod
    def incrementar_contador(cls):
        cls.__contador += 1

        if cls.__contador >= 1000:
            cls.__contador = 1

    def obter_senha(self):
        self.incrementar_contador()

        senha = f"N{self.__contador:03}"
        self.__fila_chamada.enfileirar(senha)
        return senha

    def cadastrar_paciente(self):
        try:
            senha = self.__fila_chamada.desenfileirar()
            self.__painel_cadastro.chamar(ItemPainel(senha))
            nome = input("Digite o nome do paciente: ").capitalize()
            self.__fila_atendimento.enfileirar(Paciente(nome, senha))
        except FilaException:
            print("Não há pacientes na fila de Cadastro\n\n")

    def chamada_consultorio(self):
        try:
            paciente = self.__fila_atendimento.desenfileirar()
            self.__painel_consultorio.chamar(ItemPainel(paciente.senha, paciente.nome))
        except FilaException:
            print("Não há pacientes na fila de Atendimento\n\n")

    def consultar_posicao(self, senha: str) -> tuple[int, bool]:
        try:
            return (self.__fila_chamada.busca(senha), True)
        except FilaException:
            try:
                tam = self.__fila_atendimento.tamanho()
                for i in range(1, tam + 1):
                    paciente = self.__fila_atendimento.elemento(i)
                    if paciente.senha == senha:
                        return (i, False)
                return (-1, False)
            except FilaException:
                return (-1, False)

    def mostrar_painel(self):
        print(f"\t\t{Color.BOLD}Painel de Atendimento{Color.END}")
        self.__painel_cadastro.exibir()
        print()
        self.__painel_consultorio.exibir()
        print()
