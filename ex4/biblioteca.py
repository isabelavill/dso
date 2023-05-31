from livro import Livro
from editora import Editora
from autor import Autor

class Biblioteca:
    def __init__(self):
        self.__livros = []

    def incluir_livro(self, livro: Livro):
        if livro is not None and isinstance(livro, Livro):
            if livro not in self.__livros:
                self.__livros.append(livro)

    def excluir_livro(self, livro: Livro):
        if livro is not None and isinstance(livro, Livro):
            if livro in self.__livros:
                self.__livros.remove(livro)
    
    def listar(self):
        if len(self.__livros)==0:
            print('Nennum livro cadastrado')
        else:
            for i in range(len(self.__livros)):
                print(f'Livro {i+1}: {self.__livros[i].titulo}')

    @property
    def livros(self):
        return self.__livros

autor=Autor(1,'J.K. Rowling')
editora=Editora(1,'Abril')
livro1=Livro(1,'Harry Potter e A Câmara Secreta',2003,editora,autor,1,'Inicio')
livro2=Livro(2,'Harry Potter e A Ordem da Fênix',2003,editora,autor,1,'Inicio')
biblioteca=Biblioteca()
biblioteca.incluir_livro(livro1)
biblioteca.incluir_livro(livro2)
biblioteca.listar()
biblioteca.excluir_livro(livro1)
biblioteca.excluir_livro(livro2)
biblioteca.listar()
