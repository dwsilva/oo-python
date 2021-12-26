from programa import Programa

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.__duracao = duracao

    def __str__(self):
        return "\n***************************************\nFilme: {}\nAno: {}\nDuração: {}\nCurtidas: {}\n***************************************".format(self.nome, self.ano, self.duracao, self.likes)

    @property
    def duracao(self):
        return self.__duracao


