import traceback
from exceptions import SaldoInsuficienteError, OperacaoFinanceiraError


class Cliente:
    def __init__(self, nome, cpf, profissao):
        self.nome = nome
        self.cpf = cpf
        self.profissao = profissao


class ContaCorrente:
    total_contas_criadas = 0
    taxa_operacao = None

    def __init__(self, cliente, agencia, numero):
        self.__saldo = 0
        self.__agencia = 0
        self.__numero = 0
        self.saques_nao_permitidos = 0
        self.transferencias_nao_permitidas = 0
        self.cliente = cliente
        self.__set_agencia(agencia)
        self.__set_numero(numero)
        ContaCorrente.total_contas_criadas += 1
        ContaCorrente.taxa_operacao = 30 / ContaCorrente.total_contas_criadas

    @property
    def agencia(self):
        return self.__agencia

    def __set_agencia(self, value):
        if not isinstance(value, int):
            raise ValueError('O atributo "agencia" deve ser um número inteiro - ', value) 
        if value <= 0:
            raise ValueError('O atributo "agencia" deve ser maior que 0.')
            
        self.__agencia = value
        

    @property
    def numero(self):
        return self.__numero

    def __set_numero(self, value):
        if not isinstance(value, int):
            raise ValueError('O atributo "numero" deve ser um número inteiro.') 
        if value <= 0:
            raise ValueError('O atributo "numero" deve ser maior que 0.')
        self.__numero = value
        

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, value):
        if not isinstance(value, int):
            raise ValueError('O atributo "saldo" deve ser um número inteiro.')  
        self.__saldo = value

    def transferir(self, valor, favorecido):
        if valor < 0:
            raise ValueError('O atributo "saldo" deve ser maior que 0.') 
        try:
            self.sacar(valor)
        except SaldoInsuficienteError as E:
            # traceback.print_exc()
            # print(E.args)
            E.args = ()
            raise OperacaoFinanceiraError('Operação não finalizada.') from E
        favorecido.depositar(valor)

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        # breakpoint()
        if self.saldo < valor:
            self.saques_nao_permitidos += 1
            raise SaldoInsuficienteError('', saldo = self.saldo, valor = valor)
        if valor < 0:   
            raise ValueError('O atributo "saldo" deve ser maior que 0.')
        
        self.saldo -= valor
            

# tava dando problema pq não tinha construido o atributo quando implementou o setter de agencia e número


# contas = []

# def main():
#     import sys

#     while True:
#         try:
#             nome = input('Nome do cliente:\n')
#             agencia = (input('Numero da agencia:\n'))
#             breakpoint()
#             numero = int(input('Numero da conta corrente:\n'))
#             cliente = Cliente(nome, None, None)
#             conta_corrente = ContaCorrente(nome, agencia, numero)
#             contas.append(conta_corrente)
#         except ValueError as E:
#             print(E.args)
#             sys.exit()
#         except KeyboardInterrupt:
#             print(f'\n\nForam criadas {len(contas)} contas.')
#             sys.exit()


# if __name__ == '__main__':
#     main()

try:
    conta1 = ContaCorrente('Marcio', 123, 101)
    conta2 = ContaCorrente('Marcio', 223, 201)
    conta1.depositar(100)
    conta2.depositar(200)
    conta2.transferir(300, conta1)
    print(f'Conta1 - {conta1.saldo}\nConta2 - {conta2.saldo}')
except OperacaoFinanceiraError as E:
    breakpoint()
    pass
    
    # print('Erro do tipo: ', E.__class__.__name__)
    # traceback.print_exc()

