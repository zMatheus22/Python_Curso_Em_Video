# Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai
# aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará.

def menu(desafio, texto):
    print('\33[1:34:40m=\33[m' * 23)
    print('\33[1:34:40m{:^23}\33[m'.format(f'DESAFIO {desafio} - MUNDO 3'))
    print('\33[1:34:40m=\33[m' * 23)
    print('\33[1:34m-' * 23)
    print('{:^23}'.format(texto.upper()))
    print('\33[1:34m-\33[m' * 23)


def sistemHELP():
    while True:
        command = str(input('\33[mFunção ou Biblioteca > ')).strip().lower()
        if command in 'fim':
            fim = f' Até Logo! '
            print('\33[1:41m~' * len(fim))
            print(f'{fim.upper()}')
            print('~' * len(fim))
            break
        else:
            textoComando = f" Acessando o manual do comando '{command}' "
            print('\33[1:46m~' * len(textoComando))
            print(f'{textoComando}')
            print('~' * len(textoComando))
            print('\33[1:40m')
            print(help(command))


menu('106', 'Sitema help Python')
sistemHELP()
