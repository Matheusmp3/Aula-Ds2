class Funcionários:
    def __init__(self, nome, salário):
        self.nome = nome
        self.salário = salário
    def exibir_conta(self):
        return f"Nome: {self.nome}, Salário: R$ {self.salário}"
    
class Gerente(Funcionários):
    def __init__(self, nome, salário, bônus):
        super().__init__(nome, salário)
        self.bônus = bônus

    def exibir_conta(self):
        info = super().exibir_conta()
        return f"{info}, Bônus: R${self.bônus}"

class Programador(Funcionários):
    def __init__(self, nome, salário, linguagem):
        super().__init__(nome, salário)
        self.linguagem = linguagem

    def exibir_conta(self):
        info = super().exibir_conta()
        return f"{info}, Linguagem: {self.linguagem}"

funcionário = Funcionários("Matheus", 0)
gerente = Gerente("Petterson", 1902, 0)
programador = Programador("Igor", 69, "C#")
    
print(funcionário.exibir_conta())
print(gerente.exibir_conta())
print(programador.exibir_conta())