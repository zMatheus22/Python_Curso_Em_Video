# Faça um programa que tenha uma função chamada maior(), que receba vários porâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

from time import sleep


def menu(desafio, texto):
    print('\33[1:34:40m=\33[m' * 23)
    print('\33[1:34:40m{:^23}\33[m'.format(f'DESAFIO {desafio} - MUNDO 3'))
    print('\33[1:34:40m=\33[m' * 23)
    print('\33[1:34m-' * 23)
    print('{:^23}'.format(texto.upper()))
    print('\33[1:34m-\33[m' * 23)


def maior(* valor):
    maiorValor = 0
    if len(valor) > 0:
        maiorValor = sorted(valor, reverse=True)[0]
    print('\33[1:32m-='*30)
    print(f'Analisando os valores passados...')
    for numero in valor:
        print(f'\33[36m{numero}', end=' ')
    print(f'\33[32mForam informados \33[36m{len(valor)}\33[32m valores ao todo.')
    print(f'O maior valor informado foi \33[36m{maiorValor}\33[32m.')
    sleep(1)


menu('099', 'Maior número')
maior(2, 9, 4, 5, 7, 1)
maior(-2, -3, -8, -10, -6, -4)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
