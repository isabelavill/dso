from abstractControladorChamados import AbstractControladorChamados
from tipoChamado import TipoChamado
from chamado import Chamado
from datetime import date as Date
from cliente import Cliente
from tecnico import Tecnico
from collections import defaultdict


class ControladorChamados(AbstractControladorChamados):
    def __init__(self):
        self.__chamados=[]
        self.__tipos_de_chamados=[]

    def total_chamados_por_tipo(self, tipo: TipoChamado) -> int:
        c=0
        for i in self.__tipos_de_chamados:
            if i.tipo.codigo==tipo.codigo:
                c+=1

        return c
    
    def inclui_chamado(self, data: Date, cliente: Cliente, tecnico: Tecnico, titulo: str, descricao: str, prioridade: int, tipo: TipoChamado) -> Chamado:
        if not isinstance(cliente,Cliente) or not isinstance(tecnico,Tecnico) or not isinstance(tipo,TipoChamado):
            return
        novo_chamado=Chamado(data, cliente, tecnico, titulo, descricao, prioridade, tipo)
        self.__chamados.append(novo_chamado)
        return novo_chamado
    
    def inclui_tipochamado(self, codigo: int, nome: str, descricao: str) -> TipoChamado:
        novo_tipo_chamado=TipoChamado(codigo, nome, descricao)
        self.__tipos_de_chamados.append(novo_tipo_chamado)
        return novo_tipo_chamado

    def tipos_chamados(self):
        return self.__tipos_de_chamados