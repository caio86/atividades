from Funcionario import Funcionario


class Gerente(Funcionario):
    def addBonificacao(self) -> float:
        return self.adicionalDeQualificacao()
