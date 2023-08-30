# Melhore o jogo do desafio 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai
# tentar adivinar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint

print('\33[1:34:40m=\33[m'*23)
print('\33[1:34:40m{:^23}\33[m'.format('DESAFIO 058 - MUNDO 2 '))
print('\33[1:34:40m=\33[m'*23)
print('\33[1:34m-'*23)
print('{:^23}'.format('Adivina v2.0'))
print('\33[1:34m-\33[m'*23)

numeroComputador = randint(1, 10)
numeroJogador = 0
contagemPalpite = 0
print('\33[1:36m+'*23)
print('{:^23}'.format('Vamos jogar!!'))
print('{:^23}'.format('Eu pensei em um número.'))
print('{:^23}'.format('Vamos ver se você acerta.'))
while numeroJogador != numeroComputador:
    if numeroJogador != 0:
        if numeroJogador < numeroComputador:
            print('\33[35m{:^23}'.format('Número maior!'))
        else:
            print('\33[35m{:^23}'.format('Números menor!'))
    numeroJogador = int(input('\33[33mDigite o seu palpite: '))
    contagemPalpite += 1
print('\33[1:36m+'*23)
print('\33[32m{:^23}'.format(f'Você acertou!'))
print('{:^23}'.format(f'O número foi o {numeroComputador}'))
print('{:^23}'.format(f'A quantidade de palpite: {contagemPalpite}'))

