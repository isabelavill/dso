from usuario_bu import UsuarioBU

class Funcionario(UsuarioBU):
    def __init__(self,departamento, cpf, dias_de_emprestimo):
        super().__init__(cpf, dias_de_emprestimo)
        self.__departamento= departamento
    
    @property
    def departamento(self):
        return self.__departamento
    @departamento.setter
    def departamento(self, departamento):
        self.__departamento=departamento
    

    def emprestar(self, titulo_livro:str):
        ...
    
    def devolver(self,titulo_livro: str):
        ...