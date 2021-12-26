class Conta:

    def __init__(self, numero, titular, saldo, limite=2000.0):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Olá {},\nSeu saldo é de R$: {}.\n".format(self.__titular, self.__saldo))

    def deposita(self, valor):
        print("Depósito de R$ {} para a conta {} realizado com sucesso!".format(valor, self.__numero))
        self.__saldo += valor
        print("Seu novo saldo é R$ {}.".format(self.__saldo))

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        valor_a_sacar <= (valor_disponivel_a_sacar)

    def saca(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
            print("Saque de R$ {} para a conta {} realizado com sucesso!".format(valor, self.__numero))
            print("Seu novo saldo é R$ {}.".format(self.__saldo))
        else:
            print("O valor R$ {} ultapassa seu limite permitido\n Transação cancelada".format(valor))


    def tranfere(self, valor, conta):
        self.saca(valor)
        conta.deposita(valor)
        print("Transferência de R$ {} para a conta número: {} realizado com sucesso!".format(valor, conta.__numero))

    @property
    def titual(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return "999"

    @staticmethod
    def codigos_dos_bancos():
        return {'BB':'001', 'Caixa':'104', 'Bradesco':'237'}