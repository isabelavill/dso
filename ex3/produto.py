from cliente import Cliente
from categoria_produto import CategoriaProduto

class Produto:
    def __init__(self,codigo,descricao,categoria_produto:CategoriaProduto):
        self.__codigo=codigo
        self.__descricao=descricao
        self.__categoria_produto=categoria_produto


    def preco_total(self, quantidade, preco_unitario):
        self.__quantidade=quantidade
        self.__preco_unitario=preco_unitario
        preco=(self.__quantidade * self.__preco_unitario)
        return preco

    @property
    def codigo(self):
        return self.__codigo
    @codigo.setter
    def codigo(self, codigo):
        self.__codigo=codigo

    @property
    def descricao(self):
        return self.__descricao
    @descricao.setter
    def descricao(self,descricao):
        self.__descricao=descricao

    @property
    def categoria_produto(self):
        return self.__categoria_produto
    @categoria_produto.setter
    def categoria_produto(self,categoria_produto):
        self.__categoria_produto=categoria_produto

    @property
    def quantidade(self):
        return self.__quantidade
    @quantidade.setter
    def quantidade(self,quantidade):
        self.__quantidade=quantidade

    @property
    def preco_unitario(self):
        return self.__preco_unitario
    @preco_unitario.setter
    def preco_unitario(self, preco_unitario):
        self.__preco_unitario=preco_unitario




cliente1=Cliente('Isabela','98835-1707')
categoria1=CategoriaProduto('Calça')
produto1=Produto(1,'Pequeno',categoria1)
print(produto1.preco_total(2,100))


'''
class Produto:
    def __init__(self, codigo,descricao,categoria_produto):
        self.__codigo=codigo
        self.__descricao=descricao
        self.__categoria_produto=categoria_produto
        self.__quantidade=None
        self.__preco_unitario=None



    @property
    def codigo(self):
        return self.__codigo
    @codigo.setter
    def codigo(self,codigo):
        self.__codigo=codigo


    @property
    def descricao(self):
        return self.__descricao
    @descricao.setter
    def descricao(self,descricao):
        self.__descricao=descricao


    @property
    def categoria_produto(self):
        return self.CategoriaProduto
    @categoria_produto.setter
    def categoria_produto(self,categoria_produto):
        self.categoria_produto=produto
    
    
    @property
    def quantidade(self):
        return self.__quantidade
    @quantidade.setter
    def quantidade(self,quantidade):
        self.__quantidade=quantidade


    @property
    def preco_unitario(self):
        return self.__preco_unitario
    @preco_unitario.setter
    def preco_unitario(self,preco_unitario):
        self.__preco_unitario=preco_unitario
    
    
    @property
    def cliente(self):
        return self.__cliente
    @cliente.setter
    def cliente(self,cliente):
        self.__cliente=cliente

    def preco_total(self):
        return self.__quantidade*self.__preco_unitario
'''