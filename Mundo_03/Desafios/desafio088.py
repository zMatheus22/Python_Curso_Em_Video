# Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão
# gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
from time import sleep

print('\33[1:34:40m=\33[m'*23)
print('\33[1:34:40m{:^23}\33[m'.format('DESAFIO 088 - MUNDO 3 '))
print('\33[1:34:40m=\33[m'*23)
print('\33[1:34m-'*23)
print('{:^23}'.format('Mega Sena'))
print('\33[1:34m-\33[m'*23)

numerosJogos = 1
quantidadeJogos = int(input('\33[1:33mQuantos jogos você gostaria de fazer? '))
games = list()
for numerosJogos in range(0, quantidadeJogos):
    for i in range(0, 6):
        numero = randint(1, 60)
        while numero in games:
            numero = randint(1, 60)
        games.append(numero)
    games.sort()
    print(f'\33[36mO {numerosJogos + 1}° game: {games}')
    games.clear()
    numerosJogos += 1
    sleep(1.2)
print('\33[32m+'*23)
print('{:^23}'.format('Boa Sorte :)'))
