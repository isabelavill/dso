from abstractElevador import AbstractElevador
from elevadorCheioException import ElevadorCheioException
from elevadorJahNoTerreoException import ElevadorJahNoTerreoException
from elevadorJahNoUltimoAndarException import ElevadorJahNoUltimoAndarException
from elevadorJahVazioException import ElevadorJahVazioException


class Elevador(AbstractElevador):
    def __init__(self, andar_atual, total_andares_predio, capacidade, total_pessoas):
        self.__andar_atual = andar_atual
        self.__total_andares_predio = total_andares_predio
        self.__capacidade = capacidade
        self.__total_pessoas = total_pessoas

    def descer(self) -> str:
        if self.__andar_atual != 0:
            self.__andar_atual -= 1
        else:
            raise ElevadorJahNoTerreoException
        return self.__andar_atual

    # ElevadorCheioException

    def entra_pessoa(self) -> str:
        if self.__total_pessoas + 1 < self.__capacidade:
            self.__total_pessoas += 1
        else:
            raise ElevadorCheioException
        return self.__total_pessoas

    # ElevadorJahVazioException

    def sai_pessoa(self) -> str:
        if self.__total_pessoas != 0:
            self.__total_pessoas -= 1
        else:
            raise ElevadorJahVazioException
        return self.__total_pessoas

    # ElevadorJahNoUltimoAndarException

    def subir(self) -> str:
        if self.__andar_atual != self.__total_andares_predio:
            self.__andar_atual += 1
        else:
            raise ElevadorJahNoUltimoAndarException
        return self.__andar_atual

    @property
    def capacidade(self) -> int:
        return self.__capacidade

    @property
    def total_pessoas(self) -> int:
        return self.__total_pessoas

    @property
    def total_andares_predio(self) -> int:
        return self.__total_andares_predio

    @property
    def andar_atual(self) -> int:
        return self.__andar_atual

    @total_andares_predio.setter
    def total_andares_predio(self, total_andares_predio: int):
        self.__total_andares_predio = total_andares_predio
