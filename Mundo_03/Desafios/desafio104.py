# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input() do Python, só
# que fazendo a validação para aceitar apenas um valor númerico.


def menu(desafio, texto):
    print('\33[1:34:40m=\33[m' * 23)
    print('\33[1:34:40m{:^23}\33[m'.format(f'DESAFIO {desafio} - MUNDO 3'))
    print('\33[1:34:40m=\33[m' * 23)
    print('\33[1:34m-' * 23)
    print('{:^23}'.format(texto.upper()))
    print('\33[1:34m-\33[m' * 23)


def leiaInt(texto):
    digito = input(texto)
    while not digito.isnumeric():
        print('\33[31mERRO! Digite um número inteiro válido')
        digito = input(texto)
    return digito


menu('104', 'Lendo valor')
n = leiaInt('\33[1:32mDigite um número: ')
print(f'\33[35mVocê acabou de digitar o número {n}')
