# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random

print('===== Desafio 028 =====')
numeroComputador = random.randint(0, 5)
numeroUser = int(input('Qual é o número sorteado entre 0 à 5? '))
if numeroUser == numeroComputador & numeroUser <= 5:
    print('Parabéns! Você acertou, o número sorteado pelo computador foi {}'.format(numeroComputador))
elif numeroUser <= 5:
    print('Computador ganhou! O número sorteado pelo computador foi {} e você informou {}'
          .format(numeroComputador, numeroUser))
else:
    print('Você não digitou o número entre 0 à 5')
    print('ERRO!!!')
