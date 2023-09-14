# Aprimore o Desafio 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do
# aproveitamento de cada jogador.

print('\33[1:34:40m=\33[m'*23)
print('\33[1:34:40m{:^23}\33[m'.format('DESAFIO 094 - MUNDO 3'))
print('\33[1:34:40m=\33[m'*23)
print('\33[1:34m-'*23)
print('{:^23}'.format('Interclasse'))
print('\33[1:34m-\33[m'*23)

jogador = dict()
gol = list()
dadosJogadores = list()
somaGol = 0
while True:
    print('\33[1:32m')
    jogador['nome'] = str(input('Nome: ')).strip().capitalize()
    quantidadeJogos = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for quantidade in range(1, quantidadeJogos+1):
        numeroGol = int(input(f'Número de gol do {jogador["nome"]} na partida {quantidade}: '))
        gol.append(numeroGol)
        somaGol += numeroGol
    jogador['gols'] = gol.copy()
    gol.clear()
    jogador['total'] = somaGol
    somaGol = 0
    dadosJogadores.append(jogador.copy())
    continuar = ' '
    while continuar not in ('S', 'N'):
        continuar = str(input('\33[33mDeseja continuar? [S/N] ')).strip().upper()
    if continuar in 'N':
        break
    print('-'*30)

print('\33[36m-='*30)
print(f'{"Cod":<4}', end='')
for key in jogador.keys():
    print(f'{key:<15}', end='')
print()
print('-'*40)

for indece, player in enumerate(dadosJogadores):
    print(f'{indece:>4} ', end='')
    for valor in player.values():
        print(f'{str(valor):<15}', end='')
    print()
print('-'*40)

while True:
    opcao = int(input('\33[32mDigite o código do jogador: (999 - Sair) '))
    if opcao == 999:
        break
    while opcao > len(dadosJogadores):
        print('\33[31mCódigo invalido, tente novamente!')
        break
    for jogador in range(len(dadosJogadores)):
        if opcao == jogador:
            print(f'\33[34mLevantamento do jogador {dadosJogadores[jogador]["nome"]}: ')
            for partidas in range(len(dadosJogadores[jogador]["gols"])):
                print(f' => Na {partidas + 1}° partida teve {dadosJogadores[jogador]["gols"][partidas]} gols')
            print('-' * 40)

print('{:^30}'.format('<<< Volte sempre! >>>'))
