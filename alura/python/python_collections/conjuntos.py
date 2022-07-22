from collections import defaultdict

# conjuntos são representados por {}
# pode-se criar conjuntos através do método set()

# alunos_data_science = [15, 23, 45, 31]
# alunos_machine_learning = [52, 44, 23, 15]

# alunos_data_sciente.add(13)
# frozenset(alunos_data_sciente)

# print(set(alunos_data_science))
# print(set(alunos_machine_learning))

# # união
# print(f'União:\n{set(alunos_data_science) | set(alunos_machine_learning)}\n')

# # intersecção
# print(f'Intersecção:\n{set(alunos_data_science) & set(alunos_machine_learning)}\n')

# # exclusão
# print(f'Exclusão C1 x C2:\n{set(alunos_data_science) - set(alunos_machine_learning)}\n')
# print(f'Exclusão C2 x C1:\n{set(alunos_machine_learning) - set(alunos_data_science)}\n')

from collections import defaultdict, Counter
from copy import copy


meu_texto = 'abacate banana banana maca manga manga maca melancia abacaxi acerola abacaxi abacate'


# dicionarios


# list_meu_texto = meu_texto.split()
# frutas = set(list_meu_texto)

# for fruta in frutas:
#     count = 0
#     for item in list_meu_texto:
#         if item == fruta:
#             count += 1
#     dict_frutas[fruta] = count

# for fruta in list_meu_texto:
#     count_frutas = dict_frutas.get(fruta, 0)
#     dict_frutas[fruta] = count_frutas + 1

# for fruta in list_meu_texto:
#     dict_frutas[fruta] += 1

# print(dict_frutas)

# iterando dicionários:

# reduz para uma linha as iterações sobre o dicionario
dict_frutas = Counter(meu_texto.split())
dict = copy(dict_frutas)

print(dict)
# coletando as chaves: 
# for chave in dict:
#     print(chave)
# for k in dict.keys():
#     print(k)

# coletando os valores:
# for chave in dict:
#     print(dict[chave])
# for valor in dict.values():
#     print(valor)

# coletando chave e valor:
# for chave, valor in dict.items():
#     print(chave, '-', valor)
# for chave_valor in dict.items():
#     print(chave_valor)


# exemplo de uso do defaultdict:
# class Conta:
#     def __init__(self):
#         print('Construindo uma conta')

# contas = defaultdict(Conta)
# print(contas[12])
