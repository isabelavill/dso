from abc import ABC,abstractmethod
from usuario_bu import UsuarioBU

class Funcionario(UsuarioBU):
    @abstractmethod
    def __init__(self,departamento:str, cpf:int, dias_de_emprestimo:int):
        super().__init__(cpf, dias_de_emprestimo)
        self.__departamento= departamento
    
    @property
    def departamento(self):
        return self.__departamento
    @departamento.setter
    def departamento(self, departamento):
        self.__departamento=departamento
    
    @abstractmethod
    def emprestar(self, titulo_livro:str):
        return f'do departamento "{self.__departamento}" pegou emprestado o livro: ' + titulo_livro+ f' com {str(super().dias_de_emprestimo)} dias de prazo'
    
    @abstractmethod
    def devolver(self,titulo_livro: str):
        return f'do departamento "{self.__departamento}" devolveu o livro: ' + titulo_livro