from AbstractControladorJogo import *
import random


class ControladorJogo(AbstractControladorJogo):
    def __init__(self):
        self.__baralho=[]
        self.__personagems=[]
    '''
    Retorna o baralho
    @return o baralho
    '''
    @property
    def baralho(self) -> list:
        return self.__baralho
    '''
    Retorna a lista de personagems
    @return a lista de personagems
    '''
    @property
    def personagems(self) -> list:
        return self.__personagems
   
    def inclui_personagem_na_lista(self,
                                   energia: int,
                                   habilidade: int,
                                   velocidade: int,
                                   resistencia: int,
                                   tipo: Tipo) -> Personagem:
        self.__energia=energia
        self.__habilidade=habilidade
        self.__velocidade=velocidade
        self.__resistencia=resistencia
        self.__tipo=tipo

    
    def inclui_carta_no_baralho(self, personagem: Personagem) -> Carta:
        nova_carta=Carta(personagem)
        self.__baralho.append(nova_carta)

    def jogada(self, mesa: Mesa) -> Jogador:
        pass#implementar
