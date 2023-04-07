from livro import Livro
from editora import Editora
from autor import Autor

class Biblioteca:
    def __init__(self):
        self.__livros = []

    def incluir_livro(self, livro: Livro):
        if livro is not None and isinstance(livro,Livro):
            if livro not in self.__livros:
                self.__livros.append(livro)
      
        # Nao esqueca de garantir que o objeto recebido pertence a classe Livro...
        # Nao permitir insercao de Livros duplicados!
        

    def excluir_livro(self, livro: Livro):
        if livro is not None and isinstance(livro, Livro):
            if livro in self.__livros:
                self.__livros.remove(livro)

    @property
    def livros(self):
        return self.__livros

e1=Editora(1,'Abril')
a1=Autor(1,'JK Rowling')
l1=Livro(1,'HP',2002,e1,a1,2,'cap 2')
l1.incluir_autor()