import numpy

idades = [15, 18, 23, 45, 12, 43, 65 ,87]

# enumeração gambiarra
# for i in range(len(idades)):
#     print(i, idades[i])

# enumeração braba da braba
# print(f'forma range x lista: \n{list(range(len(idades)))}\n')
# print(f'forma enumerate: \n{list(enumerate(idades))}')

# for indice, valor in enumerate(idades): #usar o _ para indicar que só vou usar uma variável ao desempacotar
#     # print(valor)
#     print(indice)

# ordenação

# o método sorted() cria uma cópia da lista original já ordenada
print(sorted(idades, reverse=True))