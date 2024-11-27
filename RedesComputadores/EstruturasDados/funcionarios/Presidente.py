from Funcionario import Funcionario, GrausDeEscolaridade


class Presidente(Funcionario):
    def contracheque(self):
        return self.addBonificacao()

    def addBonificacao(self) -> float:
        bonificacao = self.salario * 3

        if self.grau == GrausDeEscolaridade.DOUTOR:
            bonificacao += self.salario * 5

        return bonificacao
