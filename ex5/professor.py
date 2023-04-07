from funcionario import Funcionario

class Professor(Funcionario):
    def __init__(departamento, cpf):
        super().__init(departamento,cpf)

    def emprestar(self, titulo_livro:str):
        ...
    
    def devolver(self,titulo_livro: str):
        ...