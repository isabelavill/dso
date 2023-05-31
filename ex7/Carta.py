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
        soma=self.personagem.__energia + self.personagem.__habilidade + self.personagem.__velocidade + self.personagem.__resistencia
        return soma
    @property
    def personagem(self) -> Personagem:
        return self.__personagem