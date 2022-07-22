from operator import attrgetter
from conta import ContaCorrente, ContaPoupanca, ContaInvestimento, ContaSalario, verifica_tipo

# conta_corrente = ContaCorrente(123)
# conta_corrente.deposita(1000)
# conta_corrente.passa_o_mes()
# # print(conta_corrente)

# conta_poupanca = ContaPoupanca(321)
# conta_poupanca.deposita(1000)
# conta_poupanca.passa_o_mes()
# print(conta_poupanca)

# contas = [conta_poupanca, conta_corrente]

# conta_investimento = ContaInvestimento(213)

# for conta in contas:
#     conta.passa_o_mes() #duck typing definindo o método nas duas classes filhas
#     print(conta)

conta1 = ContaSalario(321)
conta1.deposita(4000)
conta2 = ContaPoupanca(155)
conta2.deposita(500)
conta3 = ContaCorrente(235)
conta3.deposita(500)

# verifica_tipo(conta_poupanca, ContaPoupanca)

contas = [conta1, conta2, conta3]

# for conta in sorted(contas, key=attrgetter("_saldo")): #também pode-se usar funções que extraem os atributos do objeto para usar como chave do ordenamento
#     print(conta)

# for conta in sorted(contas):
#     print(conta)

print(conta1 <= conta1)