# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifícios, indo de 10 até 0,
# com uma pause de 1 segundo entre eles.

from time import sleep

print('\33[1:34:40m=\33[m'*23)
print('\33[1:34:40m DESAFIO 046 - MUNDO 2 \33[m')
print('\33[1:34:40m=\33[m'*23)
print('\33[1:34m-'*23)
print('       Ano Novo')
print('\33[1:34m-\33[m'*23)

for c in range(10, 0, -1):
    print('\33[1:36m{:^23}'.format(c))
    sleep(1)
    if c == 1:
        print('{:^1}'.format('💥')*10)
        print('{:^2}'.format('🎇🎆')*5)
