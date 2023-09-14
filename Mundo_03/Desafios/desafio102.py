# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a
# calcular e o outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o
# processo de cálculo do fatorial.

def menu(desafio, texto):
    print('\33[1:34:40m=\33[m' * 23)
    print('\33[1:34:40m{:^23}\33[m'.format(f'DESAFIO {desafio} - MUNDO 3'))
    print('\33[1:34:40m=\33[m' * 23)
    print('\33[1:34m-' * 23)
    print('{:^23}'.format(texto.upper()))
    print('\33[1:34m-\33[m' * 23)


def fatorial(numero, show=False):
    '''
    -> Calcula o Fatorial de um número.
    :param numero: O número a ser calculado.
    :param show: (opcional) Mostrar ou não o calculo.
    :return: O valor do Fatorial de um número informado.
    '''

    fatoria = 1
    for contador in range(numero, 0, -1):
        if show:
            if contador == 1:
                print(f'{contador} =', end=' ')
            else:
                print(f'{contador} x', end=' ')
        fatoria *= contador
    return fatoria


menu('102', 'fatorial')
print(fatorial(7, True))
