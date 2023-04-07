from usuario_bu import UsuarioBU

class Aluno(UsuarioBU):
    def __init__(self, cpf, dias_de_emprestimo, matricula):
        super().__init__(cpf, dias_de_emprestimo)
        self.__matricula= matricula
    
    @property
    def matricula(self):
        return self.__matricula
    @matricula.setter
    def matricula(self, matricula):
        self.__matricula=matricula
    

    def emprestar(self, titulo_livro:str):
        ...
    
    def devolver(self,titulo_livro: str):
        ...