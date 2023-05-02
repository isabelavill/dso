from AbstractCarta import *
from ex7.Personagem import *


class Carta(AbstractCarta):

    def __init__(self, personagem: Personagem):
        self.__personagem=personagem

    '''
    Soma e retorna todos os valores dos atributos do personagem da Carta
    @return Retorna o somatorio de todos os atributos do personagem da Carta
    '''
    def valor_total_carta(self) -> int:
        soma=self.__energia + self.__habilidade + self.__velocidade + self.__resistencia
        return soma
    @property
    def personagem(self) -> Personagem:
        return self.__personagem