from enum import Enum
from color import Color
from clinica import Clinica
from paciente import Paciente


class Opcoes(Enum):
    ObterSenha = (1, "Obter senha de atendimento")
    Cadastrar = (2, "Chamar paciente para cadastro")
    Chamar = (3, "Chamar paciente para o consultório")
    ConsultarPosicao = (4, "Consultar a posição atual")
    Painel = (5, "Painel de atendimento")
    Sair = (6, "Sair")


def printMenu():
    res = Color.BOLD + "Clinica Medica - Atendimento" + Color.END + "\n"

    res += "=" * 40 + "\n"

    for v in Opcoes:
        res += f"{v.value[0]}. {v.value[1]}\n"

    res += "\n\n"
    print(res)


sis = Clinica()

opcao = 0

while opcao != Opcoes.Sair.value[0]:
    printMenu()
    opcao = int(input("Digite uma opção: "))

    if opcao == Opcoes.ObterSenha.value[0]:
        senha = sis.obter_senha()
        print(f"\n\nSua senha é {Color.CYAN}{senha}{Color.END}\n\n")
    elif opcao == Opcoes.Cadastrar.value[0]:
        nome = input("Digite o nome do paciente: ").capitalize()
        sis.cadastrar_paciente(nome)
        sis.mostrar_painel()
    elif opcao == Opcoes.Chamar.value[0]:
        sis.chamada_consultorio()
        sis.mostrar_painel()
    elif opcao == Opcoes.ConsultarPosicao.value[0]:
        senha = input("Digite a senha do paciente: ").upper()
        sis.consultar_posicao(senha)
    elif opcao == Opcoes.Painel.value[0]:
        sis.mostrar_painel()
