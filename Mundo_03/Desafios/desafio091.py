# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aletórios. Guarde esses resultados em um
# dicionário. No final, coloque esse dicionário em ordem sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep

print('\33[1:34:40m=\33[m'*23)
print('\33[1:34:40m{:^23}\33[m'.format('DESAFIO 091 - MUNDO 3'))
print('\33[1:34:40m=\33[m'*23)
print('\33[1:34m-'*23)
print('{:^23}'.format('Game de dados'))
print('\33[1:34m-\33[m'*23)

jogadores = dict()
print('\33[1:35mSorteio de números: ')
for sorteio in range(1, 5):
    jogadores[sorteio] = randint(1, 9)
    print(f'  O Jogador{sorteio} tirou o número: {jogadores[sorteio]}')
    sleep(1)

posicao = 1
print('\33[36mRank dos Jogadores: ')
for indece in sorted(jogadores, key=jogadores.get, reverse=True):
    print(f'  A posição {posicao}° ficou com o Jogador{indece}: {jogadores[indece]}')
    posicao += 1
