# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e
# quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será
# guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

print('\33[1:34:40m=\33[m'*23)
print('\33[1:34:40m{:^23}\33[m'.format('DESAFIO 093 - MUNDO 3'))
print('\33[1:34:40m=\33[m'*23)
print('\33[1:34m-'*23)
print('{:^23}'.format('Campeonato de Futebol'))
print('\33[1:34m-\33[m'*23)

jogador = dict()
print('\33[1:32m')
jogador['nome'] = str(input('Nome: ')).strip().capitalize()
quantidadeJogos = int(input(f'Quantos partidas {jogador["nome"]} jogou? '))
gol = list()
soma = 0
for partidas in range(1, quantidadeJogos + 1):
    numeroGol = int(input(f'Quantos gols na partida {partidas}: '))
    soma += numeroGol
    gol.append(numeroGol)
jogador['gols'] = gol
jogador['total'] = soma
print('\33[34m+'*30)
print(jogador)
print('\33[35m+'*30)
for key, valor in jogador.items():
    print(f'O campo {key} tem o valor {valor}.')
print('\33[36m+'*30)
print(f'O jogador {jogador["nome"]} jogo {quantidadeJogos} partidas.')
for partida in range(0, quantidadeJogos):
    print(f'    => Na partida {partida+1}, fez {gol[partida]} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
