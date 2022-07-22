from conta import Conta

# marcio = ('Marcio', 23, 1998)
# luiza = ('Luiza', 59, 1963)

# usuarios = (marcio, luiza) 

# print(usuarios)

# for user in usuarios:
#     print(user)

conta_marcio = Conta(123)
conta_luiza = Conta(321)

contas = (conta_marcio, conta_luiza)

contas[0].deposita_cc(2500)

for conta in contas:
    print(conta)




# print(contas)