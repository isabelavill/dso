from funcionario import Funcionario
#20 dias
class Professor(Funcionario):
    def __init__(self, departamento, cpf):
        super().__init__(departamento,cpf,20)

    def emprestar(self, titulo_livro:str):
        return f'Professor {super().emprestar(titulo_livro)}'
    
    def devolver(self,titulo_livro: str):
        return f'Professor {super().devolver(titulo_livro)}'