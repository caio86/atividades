from Gerente import Gerente


class Diretor(Gerente):
    def addBonificacao(self) -> float:
        bonificacao = self.salario * 0.3

        bonificacao += self.adicionalDeQualificacao()

        return bonificacao
