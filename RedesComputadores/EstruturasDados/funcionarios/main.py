from pytablewriter import RstSimpleTableWriter as TableWriter

from Diretor import Diretor
from Funcionario import GrausDeEscolaridade
from Gerente import Gerente
from Presidente import Presidente


def main():

    funcionarios = [
        Presidente("jose", 2000.0, GrausDeEscolaridade.DOUTOR),
        Presidente("ricardo", 2000.0, GrausDeEscolaridade.MEDIO),
        Gerente("Ana Karina", 2000.0, GrausDeEscolaridade.ESPECIALISTA),
        Diretor("João Silva", 2000.0, GrausDeEscolaridade.MESTRE),
    ]

    valorTabela = map(
        lambda func: [
            func.__class__.__name__,
            func.nome,
            func.grau.value,
            func.contracheque(),
        ],
        funcionarios,
    )

    writer = TableWriter(
        table_name="Funcionários",
        headers=[
            "Objeto",
            "Funcionário",
            "Grau de Instrução",
            "Salário",
        ],
        value_matrix=valorTabela,
    )

    writer.write_table()


if __name__ == "__main__":
    main()
