# Faça um programa que tenha uma função chamada contador(), que receba três porâmetros: início, fim e passo e realize a
# contagem. Seu programa tem que realizar três contagens através da função criada:
# A) De 1 até 10, de 1 em 1
# B) De 10 até 0, de 2 em 2
# C) Uma contagem personalizada.

from time import sleep
def menu(desafio, texto):
    print('\33[1:34:40m=\33[m' * 23)
    print('\33[1:34:40m{:^23}\33[m'.format(f'DESAFIO {desafio} - MUNDO 3'))
    print('\33[1:34:40m=\33[m' * 23)
    print('\33[1:34m-' * 23)
    print('{:^23}'.format(texto.upper()))
    print('\33[1:34m-\33[m' * 23)


def contador(inicio, fim, passo):
    print('-='*15)
    print(f'Contagem de {inicio} até {fim} de ', end='')

    if inicio > fim:
        if passo == 0:
            passo = 1
            print(f'{passo} em {passo}')
            passo *= (-1)
        elif passo < 0:
            print(f'{passo * (-1)} em {passo * (-1)}')
        elif passo > 0:
            print(f'{passo} em {passo}')
            passo *= (-1)

    elif inicio < fim:
        if passo == 0:
            passo = 1
            print(f'{passo} em {passo}')
        elif passo < 0:
            passo *= (-1)
            print(f'{passo} em {passo}')
        elif passo > 0:
            print(f'{passo} em {passo}')

    for valores in range(inicio, fim + passo, passo):
        print(valores, end=' ')
        sleep(0.5)
    print('Fim!')


menu('098', 'contagem de valor')

contador(1, 10, 1)
contador(10, 0, -2)

print('-='*15)
inicioUser = int(input('Início: '))
fimUser = int(input('Fim:    '))
passoUser = int(input('Passo:  '))
contador(inicio=inicioUser, fim=fimUser, passo=passoUser)

