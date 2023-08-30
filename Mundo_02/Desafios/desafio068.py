# Faça um programa que jogue par ou impar com o computador. O jogo só será interrompido quando o jogador PERDER,
# mostrando o total de vitporias consecutivas que ele conquistou no final do jogo.

from random import randint

print('\33[1:34:40m=\33[m'*23)
print('\33[1:34:40m{:^23}\33[m'.format('DESAFIO 068 - MUNDO 2 '))
print('\33[1:34:40m=\33[m'*23)
print('\33[1:34m-'*23)
print('{:^23}'.format('GAME - PAR x IMPAR'))
print('\33[1:34m-\33[m'*23)

quantidadeVitoria = 0
while True:
    numeroComputador = randint(1, 10)
    numeroJogador = int(input('\33[1:33mDigite o valor: '))
    opcao = ' '
    while opcao not in ('P', 'I'):
        opcao = str(input('Qual é a sua escolha, Par ou Impar? [P/I] ')).upper().split()[0]
    soma = numeroJogador + numeroComputador
    print('\33[34m_'*23)
    print('{:^23}'.format(f'Jogador {numeroJogador} x {numeroComputador} Computador'))
    print('{:^23}'.format(f'Soma dos valores: {soma}'))
    print('+'*23)
    if soma % 2 == 0:
        resultado = 'P'
    else:
        resultado = 'I'
    if opcao == resultado:
        print('{:^23}'.format('\33[32mVocê ganhou!'))
        quantidadeVitoria += 1
    else:
        break
print('{:^23}'.format('\33[31mGAME OVER!'))
print('{:^23}'.format(f'\33[36mVocê ganhou {quantidadeVitoria}x'))
