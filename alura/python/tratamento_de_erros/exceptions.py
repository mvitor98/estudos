class OperacaoFinanceiraError(Exception):
    pass


class SaldoInsuficienteError(Exception):
    def __init__(self, message='', saldo=None, valor=None, *args):
        # breakpoint()
        self.saldo = saldo
        self.valor = valor
        msg = '\nSaldo insuficiente para efetuar a transação.\n' \
            f'Saldo atual: ***R$ {self.saldo:.2f}  |  Valor da transação: ***R$ {self.valor:.2f}'  
        self.msg = message or msg
        # ao aplicar o método super() como atributo, nós conseguimos cosntruir uma mensagem diretamente na chamada da exception
        super(SaldoInsuficienteError, self).__init__(self.msg)