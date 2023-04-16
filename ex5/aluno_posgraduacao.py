from aluno import Aluno

class AlunoPosGraduacao(Aluno):
    def __init__(self, elaborando_tese: bool, cpf, dias_de_emprestimo, matricula):
        super().__init__(cpf, dias_de_emprestimo, matricula)
        self.__elaborando_tese= elaborando_tese
    
    @property
    def elaborando_tese(self):
        return self.__elaborando_tese
    @elaborando_tese.setter
    def elaborando_tese(self,elaborando_tese):
        self.__elaborando_tese=elaborando_tese

    def emprestar(self, titulo_livro:str):
        prazo=super().dias_de_emprestimo
        if self.__elaborando_tese==True:
            prazo=prazo*2
        return f' {super().emprestar(titulo_livro)} {str(prazo)} dias de prazo'
    
    def devolver(self,titulo_livro: str):
        return super().devolver(titulo_livro)