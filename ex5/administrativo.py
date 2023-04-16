from funcionario import Funcionario
#10 dias
class Administrativo(Funcionario):
    def __init__(self,departamento, cpf):
        super().__init__(departamento,cpf,10)

    def emprestar(self, titulo_livro:str):
        return f'Funcionario administrativo {super().emprestar(titulo_livro)}'
    def devolver(self,titulo_livro: str):
        return f'Funcionario administrativo {super().devolver(titulo_livro)}'