# Faça um programa que tenha uma função chamado escreva(), que receba um texto qualquer como parâmetro e mostre uma
# mensagem com tamanho adaptável.

def menu(desafio, texto):
    print('\33[1:34:40m=\33[m' * 23)
    print('\33[1:34:40m{:^23}\33[m'.format(f'DESAFIO {desafio} - MUNDO 3'))
    print('\33[1:34:40m=\33[m' * 23)
    print('\33[1:34m-' * 23)
    print('{:^23}'.format(texto.upper()))
    print('\33[1:34m-\33[m' * 23)


def escreva(texto):
    tamanho = len(texto) + 2
    print('~' * tamanho)
    print(f' {texto.upper()} ')
    print('~' * tamanho)


menu('097', 'texto adaptável')
escreva('Matheus vinicyus strada')
