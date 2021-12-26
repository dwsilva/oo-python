
class Playlist:
    def __init__(self, nome, programa):
        self.nome = nome.title()
        self.__programa = programa

    def __getitem__(self, item):
        return self.__programa[item]

    @property
    def listagem(self):
        return self.__programa

    @property
    def tamanho(self):
        return len(self.__programa)

    def __len__(self):
        return len(self.__programa)