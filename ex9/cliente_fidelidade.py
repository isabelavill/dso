from cliente import Cliente


class ClienteFidelidade(Cliente):
    def __init__(self,codigo_fidelidade,desconto,cpf,nome,endereco,telefone):
        super().__init__(cpf,nome,endereco,telefone)
        self.__codigo_fidelidade=codigo_fidelidade
        self.__desconto=desconto

    @property
    def codigo_fidelidade(self):
        return self.__codigo_fidelidade
    
    @codigo_fidelidade.setter
    def codigo_fidelidade(self,codigo_fidelidade):
        self.__codigo_fidelidade=codigo_fidelidade

    @property
    def desconto(self):
        return self.__desconto
    
    @desconto.setter
    def desconto(self,desconto):
        self.__desconto=desconto

