from enum import Enum
from color import Color
from clinica import Clinica

import os


class Opcoes(Enum):
    ObterSenha = (1, "Obter senha de atendimento")
    Cadastrar = (2, "Chamar paciente para cadastro")
    Chamar = (3, "Chamar paciente para o consultório")
    ConsultarPosicao = (4, "Consultar a posição atual")
    Painel = (5, "Painel de atendimento")
    Sair = (6, "Sair")


def limpaTela():
    os.system("cls" if os.name == "nt" else "clear")


def printMenu():
    limpaTela()
    res = Color.BOLD + "Clinica Medica - Atendimento" + Color.END + "\n"

    res += "=" * 40 + "\n"

    for v in Opcoes:
        res += f"{v.value[0]}. {v.value[1]}\n"

    res += "\n\n"
    print(res)


sis = Clinica()

opcao = 0

printMenu()
while opcao != Opcoes.Sair.value[0]:
    opcao = int(input("Digite uma opção: "))
    printMenu()

    if opcao == Opcoes.ObterSenha.value[0]:
        senha = sis.obter_senha()
        print(f"Sua senha é {Color.CYAN}{senha}{Color.END}\n\n")
    elif opcao == Opcoes.Cadastrar.value[0]:
        sis.cadastrar_paciente()
        sis.mostrar_painel()
    elif opcao == Opcoes.Chamar.value[0]:
        sis.chamada_consultorio()
        sis.mostrar_painel()
    elif opcao == Opcoes.ConsultarPosicao.value[0]:
        senha = input(f"{Color.BOLD}Identificação de Senha: {Color.END}").upper()
        pos = sis.consultar_posicao(senha)
        if pos == -1:
            print(
                f"{Color.BOLD}{Color.RED}A senha, {Color.DARKCYAN}{senha}{Color.RED}, já foi chamada ou não existe{Color.END}\n\n"
            )
        else:
            print(f"{Color.BOLD}{Color.CYAN}{Color.END}")
    elif opcao == Opcoes.Painel.value[0]:
        sis.mostrar_painel()
