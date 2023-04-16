from usuario_bu import UsuarioBU
from abc import ABC, abstractmethod


class Aluno(UsuarioBU):
    @abstractmethod
    def __init__(self, cpf, dias_de_emprestimo, matricula:int):
        super().__init__(cpf, dias_de_emprestimo)
        self.__matricula= matricula
    
    @property
    def matricula(self):
        return self.__matricula
    @matricula.setter
    def matricula(self, matricula):
        self.__matricula=matricula
    

    def emprestar(self, titulo_livro:str):
        return f'Aluno de matricula {self.__matricula} pegou emprestado o livro: {titulo_livro} com '
    
    def devolver(self,titulo_livro: str):
        return f'Aluno de matricula {self.__matricula} devolveu o livro: {titulo_livro}'