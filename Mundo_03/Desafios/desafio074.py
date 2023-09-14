# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

print('\33[1:34:40m=\33[m'*23)
print('\33[1:34:40m{:^23}\33[m'.format('DESAFIO 074 - MUNDO 3 '))
print('\33[1:34:40m=\33[m'*23)
print('\33[1:34m-'*23)
print('{:^23}'.format('Sorteio de números'))
print('\33[1:34m-\33[m'*23)

numero = (randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9))

print('Os valores sorteados são:', end=' ')
for possition in range(len(numero)):
    print(numero[possition], end=' ')
    if possition == 0:
        maior = menor = numero[possition]
    else:
        if numero[possition] < menor:
            menor = numero[possition]
        if numero[possition] > maior:
            maior = numero[possition]
print(f'\nO maior número sorteado foi o {maior}')
print(f'O menor número sorteado foi o {menor}')
