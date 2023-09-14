# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função
# vai sortear 5 números e vai colocálos dentro da lista e a segunda função vai mostrar a soma entre todos os valores
# PARES sorteados pela função anterior.

from random import randint
from time import sleep


def menu(desafio, texto):
    print('\33[1:34:40m=\33[m' * 23)
    print('\33[1:34:40m{:^23}\33[m'.format(f'DESAFIO {desafio} - MUNDO 3'))
    print('\33[1:34:40m=\33[m' * 23)
    print('\33[1:34m-' * 23)
    print('{:^23}'.format(texto.upper()))
    print('\33[1:34m-\33[m' * 23)


def somaPar(* numeroPar):
    soma = 0
    valores = numeroPar[0]
    for par in valores:
        if par % 2 == 0:
            soma += par
    print(f'Somando os valores pares de \33[36m{numeroPar[0]}\33[32m, temos \33[36m{soma}')


def sorteia(quantidadeSorteio):
    numerosSorteados = list()
    for quantidade in range(0, quantidadeSorteio):
        numero = randint(1, 10)
        numerosSorteados.append(numero)
        print(f'\33[36m{numero}', end=' ')
        sleep(0.4)
    print('\33[32mPRONTO!')
    somaPar(numerosSorteados)


menu('100', 'Sorteio de pares')
quantidadeSorteio = 5
print(f'\33[1:32mSorteando \33[36m{quantidadeSorteio}\33[32m valores da lista:', end=' ')
sorteia(quantidadeSorteio)
