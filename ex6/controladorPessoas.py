from abstractControladorPessoas import AbstractControladorPessoas
from cliente import Cliente
from tecnico import Tecnico


class ControladorPessoas(AbstractControladorPessoas):
    def __init__(self):
        self.__clientes=[]
        self.__tecnicos=[]

    def clientes(self) -> list:
        return self.__clientes
    
    def tecnicos(self) -> list:
        return self.__tecnicos
    
    def inclui_cliente(self, codigo: int, nome: str) -> Cliente:
        novo_cliente=Cliente(codigo, nome)
        self.__clientes.append(novo_cliente)
        return novo_cliente
    
    def inclui_tecnico(self, codigo: int, nome: str) -> Tecnico:
        novo_tecnico=Tecnico(codigo,nome)
        self.__tecnicos.append(novo_tecnico)
        return novo_tecnico