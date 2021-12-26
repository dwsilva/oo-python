from programa import Programa

class Serie(Programa):
    def __init__(self, nome, ano, temporada):
        super().__init__(nome, ano)
        self.__temporada = temporada

    def __str__(self):
        return "\n***************************************\nSérie: {}\nAno: {}\nTemporadas: {}\nCurtidas: {}\n***************************************".format(self.nome, self.ano, self.temporada, self.likes)

    @property
    def temporada(self):
        return self.__temporada

