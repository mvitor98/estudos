
class Conta:

    def __init__(self, numero, titular, saldo, limite):
        self.__numero = str(numero)
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print(f'\nExtrato:\n'
              f'saldo = {self.__saldo}\n'
              f'limite = {self.__limite}\n'
              )

    def deposita(self, valor):
        self.__saldo += valor
        
    def saca(self, valor):
        self.__saldo -= valor
        
    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)
        self.extrato() 
    
    @property
    def conta(self):
        return self.__numero
    
    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.saldo

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, valor):
        self.__limite = valor

    @staticmethod
    def conta_banco():
        return '001'

if __name__ == '__main__':
    conta1 = Conta('001', 'Marcio', 400.0, 2500.0)
    conta2 = Conta('002', 'Maria', 200.0, 1500.0)
    conta3 = Conta('003', 'Sarah', 100.0, 3500.0)

    print(
          f'\nConta:\n'
          f'numero da conta = {conta1.numero}\n'
          f'titular = {conta1.titular}\n'
          f'saldo = {conta1.saldo}\n'
          f'limite = {conta1.limite}'
          )

    Conta.extrato(conta1)
    Conta.deposita(conta1, 200)
    Conta.extrato(conta1)
    Conta.saca(conta1, 300)
    Conta.extrato(conta1)
