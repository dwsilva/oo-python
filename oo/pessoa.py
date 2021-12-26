
class Pessoa:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        print("get")
        return self.__nome.title()

    @nome.setter
    def nome(self, nome):
        print("set")
        self.__nome = nome