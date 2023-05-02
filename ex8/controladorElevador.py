from abstractControladorElevador import AbstractControladorElevador
from comandoInvalidoException import ComandoInvalidoException
from elevador import Elevador


class ControladorElevador(AbstractControladorElevador):
    def __init__(self):
        self.__elevador = None

    """
    Faz o elevador subir um andar. Se jah estiver no ultimo andar, dispara excecao
    @return Mensagem informando o que ocorreu com o elevador 
    @throws ElevadorJahNoUltimoAndarException 
    """

    def subir(self) -> str:
        self.__elevador.subir()
        return "Subiu um andar"

    """
    Faz o elevador descer um andar. Se jah estiver no terreo, dispara excecao
    @return Mensagem informando o que ocorreu com o elevador
    @throws ElevadorJahNoTerreoException
    """

    def descer(self) -> str:
        self.__elevador.descer()
        return "Desceu um andar"

    """
    Entra uma pessoa no Elevador. Se nao for possivel permitir a entrada da pessoa, dispara excecao
    @return Mensagem informando o que ocorreu com o elevador
    @throws ElevadorCheioException
    """

    def entra_pessoa(self) -> str:
        self.__elevador.entra_pessoa()
        return "Entrou uma pessoa"

    """
    Sai uma pessoa no Elevador. Se nao for possivel permitir a saida de uma pessoa, dispara excecao
    @return Mensagem informando o que ocorreu com o elevador
    @throws ElevadorJahVazioException
    """

    def sai_pessoa(self) -> str:
        self.__elevador.sai_pessoa()
        return "Saiu uma pessoa"

    """
    @return Elevador
    """

    @property
    def elevador(self) -> Elevador:
        return self.__elevador

    """
    @param andar_atual andar atual do elevador
    @param total_andares_predio total de andares do predio
    @param capacidade capacidade maxima do elevador
    @param total_pessoas total de pessoas atual do elevador
    """

    def inicializar_elevador(
        self,
        andar_atual: int,
        total_andares_predio: int,
        capacidade: int,
        total_pessoas: int,
    ):
        if not isinstance(andar_atual, int):
            raise ComandoInvalidoException
        if not isinstance(total_andares_predio, int):
            raise ComandoInvalidoException
        if not isinstance(capacidade, int):
            raise ComandoInvalidoException
        if not isinstance(total_pessoas, int):
            raise ComandoInvalidoException
        if andar_atual < 0:
            raise ComandoInvalidoException
        if total_andares_predio < 0:
            raise ComandoInvalidoException
        if capacidade < 0:
            raise ComandoInvalidoException
        if total_pessoas < 0:
            raise ComandoInvalidoException
        if total_andares_predio < andar_atual:
            raise ComandoInvalidoException
        if capacidade < total_pessoas:
            raise ComandoInvalidoException

        self.__elevador = Elevador(
            andar_atual, total_andares_predio, capacidade, total_pessoas
        )
