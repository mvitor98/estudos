from abc import ABCMeta, abstractmethod
from functools import total_ordering

@total_ordering
class Conta(metaclass=ABCMeta):

    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self) -> str:
        return f'*************\n>>Código: {self._codigo}   Saldo: R${self._saldo:.2f}\n<<'

    @abstractmethod
    def passa_o_mes(self):
        pass

    def __lt__(self, outro):
        if self._saldo != outro._saldo:
            return self._saldo < outro._saldo   
        return self._codigo < outro._codigo


class ContaCorrente(Conta):
    def passa_o_mes(self):
        self._saldo -= 2

class ContaPoupanca(Conta):
    def passa_o_mes(self):
        self._saldo *= 1.01
        self._saldo -= 3

class ContaInvestimento(Conta):
    pass

@total_ordering
class ContaSalario:
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def __eq__(self, outro):
        # return self._codigo == outro._codigo
        if type(outro) != ContaCorrente:
            return False 

    def __eq__(self, outro):
        return self._codigo == outro._codigo

    def __lt__(self, outro):
        if self._saldo != outro._saldo:
            return self._saldo < outro._saldo   
        return self._codigo < outro._codigo
    
    def deposita(self, valor):
        self._saldo += valor

    def __str__(self) -> str:
        return f'*************\n>>\nCódigo: {self._codigo}   Saldo: R${self._saldo:.2f}\n<<'

def verifica_tipo(obj1, classe):
    return print(f'{isinstance(obj1, classe)}')

# def deposita_em_todas(contas):
#     for conta in contas:
#         conta.deposita_cc(100)



# conta_marcio = ContaCorrente(123)
# conta_marcio.deposita_cc(500)
# # print(conta_marcio)

# conta_luiza = ContaCorrente(321)
# conta_luiza.deposita_cc(1000)
# # print(conta_luiza)

# # imprime os objetos da lista, não as informações desses objetos
# contas = [conta_marcio, conta_luiza]
# deposita_em_todas(contas)

# print(contas)

# for conta in contas:
#     print(conta)