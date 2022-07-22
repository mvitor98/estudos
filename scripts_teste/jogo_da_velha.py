from site import check_enableusersite


import random

n = 3
matriz = [['   ' for r in range(3)] for r in range(3)]

for r in matriz:
    print(r)

x = 'x'
l = int(input('digite a linha: ')) - 1
c = int(input('digite a coluna: ')) - 1

matriz[l][c] = x

for r in matriz:
    print (r)

for r in matriz:
    for c in r:
        if c == x:
            r[r.index(c) + 1] = 'o'

for r in matriz:
    print(r)