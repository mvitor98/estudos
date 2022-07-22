humano        = 'AGTAATATTCTTTATGACAATTCATTTGATTA'
chimpanze     = 'AATAATATTCTTTATGACAATTCATTTGATTT'

sequencias = [humano, chimpanze]

def cria_matriz(lista):
    matriz = {}
    tamanho_sequecia = len(lista[0])
    for base in 'ACTG':
        matriz[base] = [0] * tamanho_sequecia
    return matriz

# matriz_zeros = cria_matriz(sequencias)

def preenche_matriz(lista, matriz):
    tamanho_sequencia = len(lista[0])
    for seq in lista:
        for pos in range(tamanho_sequencia):
            base = seq[pos]
            matriz[base][pos] += 1
    return matriz

def sequencia_ancestral(matriz):
    seq_ancestral = ""
    maior_valor = 0
    tamanho_sequencia = len(matriz["A"])
    for pos in range(tamanho_sequencia):
        for base in 'ACTG':
            valor_atual = matriz[base][pos]
            if valor_atual > maior_valor:
                maior_valor = valor_atual
                base_mais_frequente = base
        seq_ancestral += base_mais_frequente
        maior_valor = 0

    return seq_ancestral
# matriz = preenche_matriz(sequencias, matriz_zeros)
# for linha in matriz.items():
#     print(linha)

# aqui dá um empate na posilçao (matriz[A][1], matriz[G][1]) e (matriz[A][-1], matriz[T][-1])
# para resolver, é necessário pegar um outro ancestral da mesma família

grupo_externo = 'GATAATAGTCTATATCGCAACTCATTTGATTA'
sequencias.append(grupo_externo)

matriz_zeros = cria_matriz(sequencias)
matriz = preenche_matriz(sequencias, matriz_zeros)
for linha in matriz.items():
    print(linha)

ancestral = sequencia_ancestral(matriz)
print('humano:        ',humano)
print('chimpanze:     ',chimpanze)
print('grupo_externo: ',grupo_externo)
print('ancestral:     ',ancestral)
