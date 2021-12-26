from conta import Conta

pessoa1 = Conta(1, "David", 1000.0)
pessoa2 = Conta(2, "Lais", 2000.0)
pessoa3 = Conta(3, "Paula", 3000.0)


def imprime_teste():
    print(pessoa1)
    print(pessoa2)
    print(pessoa3)

    print("*****")
    pessoa1.extrato()
    pessoa2.extrato()
    pessoa3.extrato()
    print("*****")
    pessoa1.deposita(1000.0)
    print("*****")
    pessoa1.saca(2560.0)
    print("*****")
    pessoa1.tranfere(250, pessoa3)
    print("*****")
    pessoa1.extrato()
    pessoa2.extrato()
    pessoa3.extrato()


imprime_teste()
