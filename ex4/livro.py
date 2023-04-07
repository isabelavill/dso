from editora import Editora
from autor import Autor
from capitulo import Capitulo

class Livro:
    def __init__(self, codigo: int, titulo: str, ano: int, editora: Editora, 
    autor: Autor, numero_capitulo: int, titulo_capitulo: str):
        
        self.__codigo=codigo
        self.__titulo=titulo
        self.__ano=ano
        self.__editora=editora
        self.__autor=autor
        self.__numero_capitulo=numero_capitulo
        self.__titulo_capitulo=titulo_capitulo
        
        self.__autores=[Autor]
        
        self.__capitulos= [Capitulo(numero_capitulo,titulo_capitulo)]
        
        # Criar todos os atributos, incluindo as listas
        # Incluir o primeiro autor e o primeiro capitulo nas respectivas listas
    

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo   

    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, ano):
        self.__ano = ano

    @property
    def editora(self):
        return self.__editora

    @editora.setter
    def editora(self, codigo):
        self.__editora = Editora

    @property
    def autor(self):
        return self.__autor

    @autor.setter
    def autor(self, autor):
        self.__autor = autor

    @property
    def numero_capitulo(self):
        return self.__numero_capitulo

    @numero_capitulo.setter
    def numero_capitulo(self, numero_capitulo):
        self.__numero_capitulo = numero_capitulo
        
    @property
    def titulo_capitulo(self):
        return self.__titulo_capitulo

    @titulo_capitulo.setter
    def titulo_capitulo(self, titulo_capitulo):
        self.__titulo_capitulo = titulo_capitulo

    @property
    def autores(self):
        return self.__autores

    @autores.setter
    def autores(self, autores):
        self.__autores = autores

    @property
    def capitulos(self):
        return self.__capitulos

    @capitulos.setter
    def capitulos(self, capitulos):
        self.__capitulos = capitulos
    

    def incluir_autor(self, autor: Autor):
        if autor is not None and isinstance(autor, Autor):
            if autor not in self.__autores:
                self.__autores.append(autor)

        #Nao esqueca de garantir que o objeto recebido pertence a classe Autor...
        # Nao permitir insercao de Autores duplicados!
        

    def excluir_autor(self, autor: Autor):
        if autor is not None and isinstance(autor, Autor):
            if autor in self.__autores:
                self.__autores.remove(autor)

    def incluir_capitulo(self, numero: int, titulo: str):
        if (Capitulo(numero,titulo)) not in self.__capitulos:
            self.__capitulos.append(Capitulo(numero, titulo))
        
        #Nao permitir insercao de Capitulos duplicados!

    def excluir_capitulo(self, titulo: str):
        if (Capitulo(titulo)) in self.__capitulos:
            self.__capitulos.remove(Capitulo(titulo))

    def find_capitulo_by_titulo(self, titulo: str):
        if (Capitulo(titulo)) in self.__capitulos:
            return Capitulo(titulo)
        # Procura na lista de capitulos se existe um Capitulo com este titulo 
        # Se encontrar, retorna o Capitulo encontrado
