# Faça um programa que tenha uma função, que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele
# marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado
# corretamente.

def menu(desafio, texto):
    print('\33[1:34:40m=\33[m' * 23)
    print('\33[1:34:40m{:^23}\33[m'.format(f'DESAFIO {desafio} - MUNDO 3'))
    print('\33[1:34:40m=\33[m' * 23)
    print('\33[1:34m-' * 23)
    print('{:^23}'.format(texto.upper()))
    print('\33[1:34m-\33[m' * 23)


def jogador(nome='<desconhecido>', gol=''):
    if nome == '':
        nome = '<desconhecido>'
    if gol.isnumeric():
        int(gol)
    else:
        gol = 0
    return f'O jogador {nome} fez {gol} gol(s) no campeonato.'


menu('103', 'Ficha do jogador')
nomeJogador = str(input('\33[1:32mNome: ')).strip().capitalize()
golsJogador = str(input('Gols: ')).strip()
print('\33[36m-'*30)
print(jogador(nome=nomeJogador, gol=golsJogador))
