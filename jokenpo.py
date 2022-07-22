import random
import os
from time import sleep

os.system('cls')

def pede_jogada():
    os.system('cls')
    jogada = int(input("""Escolha um número:
    1 - Pedra
    2 - Papel
    3 - Tesoura

    .  """))
    return jogada

def jogadas(lista):
    jogada = pede_jogada()
    jogada = lista[jogada-1]
    jogada_pc = random.choice(lista)

    return jogada, jogada_pc

def comeca_jogo():
    os.system('cls')
    print('\nPedra!')
    sleep(0.5)
    os.system('cls')
    print('\nPapel!')
    sleep(0.5)
    os.system('cls')
    print(f'\nTesoura!')
    sleep(0.5)
    os.system('cls')
    # condicoes: 1 (pedra) > 3 (tesoura), 3 (tesoura) > 2 (Papel), 2 (Papel) > 1 (Pedra)

def jogar():
    lista = ['Pedra', 'Papel', 'Tesoura']
    jogada, jogada_pc = jogadas(lista)
    
    comeca_jogo()
    
    print(f'Jogada do PC: {jogada_pc}\nSua Jogada: {jogada}')

    if jogada_pc == lista[0] and jogada == lista[2]:
        print(f'\nVocê perdeu...')
        pontos('derrota')

    elif jogada_pc == lista[1] and jogada == lista[0]:
        print(f'\nVocê perdeu...')
        pontos('derrota')

    elif jogada_pc == lista[2] and jogada == lista[1]:
        print(f'\nVocê perdeu...')
        pontos('derrota')

    elif jogada_pc == jogada:
        print(f'\nEmpate.')
        pontos('empate')

    else:
        print('\nVocê ganhou!')
        pontos('vitoria')
    
def jogar_novamente():
    sleep(3)
    os.system('cls')
    jogar_novamente = input('Deseja jogar novamente (S/N)? ')
    while jogar_novamente not in ['s', 'n']:
        jogar_novamente = input('Digite apenas "S" ou "N".')
    if jogar_novamente.lower().strip() == 's':
        return True

def pontos(entrada):
    vitoria = 0
    derrota = 0
    empate = 0

    if entrada == 'vitoria':
        vitoria += 1
    elif entrada == 'derrota':
        derrota += 1
    elif entrada == 'empate':
        empate += 1

    print(f"""
Vitórias: {vitoria}
Derrotas: {derrota}
Empates: {empate}
""")

if __name__ == '__main__':
    jogar()
    while jogar_novamente():
        jogar()