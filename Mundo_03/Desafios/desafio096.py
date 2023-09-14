# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e
# comprimento) e mostre a área do terreno.

def menu(desafio, texto):
    print('\33[1:34:40m=\33[m' * 23)
    print('\33[1:34:40m{:^23}\33[m'.format(f'DESAFIO {desafio} - MUNDO 3'))
    print('\33[1:34:40m=\33[m' * 23)
    print('\33[1:34m-' * 23)
    print('{:^23}'.format(texto))
    print('\33[1:34m-\33[m' * 23)


def area(largura, comprimento):
    areaTerreno = largura * comprimento
    print(f'A área de um terreno {largura}x{comprimento} é de {areaTerreno:.2f}m²')


menu('096', 'Controle de terrenos')
larguara = float(input('largura (m): '))
comprimento = float(input('comprimento (m): '))
area(larguara, comprimento)
