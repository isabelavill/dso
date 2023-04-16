from funcionario import Funcionario
#10 dias
class Administrativo(Funcionario):
    def __init__(departamento, cpf):
        super().__init(departamento,cpf)

    def emprestar(self, titulo_livro:str):
        return f'Funcionario administrativo {super().emprestar(titulo_livro)}'
    def devolver(self,titulo_livro: str):
        return f'Funcionario administrativo {super().devolver(titulo_livro)}'