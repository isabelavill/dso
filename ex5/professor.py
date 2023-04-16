from funcionario import Funcionario
#20 dias
class Professor(Funcionario):
    def __init__(departamento, cpf):
        super().__init__(departamento,cpf)

    def emprestar(self, titulo_livro:str):
        return f'Professor {super().emprestar(titulo_livro)}'
    
    def devolver(self,titulo_livro: str):
        return f'Professor {super().emprestar(titulo_livro)}'