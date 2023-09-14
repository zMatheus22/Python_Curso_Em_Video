# Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.

print('\33[1:34:40m=\33[m'*23)
print('\33[1:34:40m{:^23}\33[m'.format('DESAFIO 086 - MUNDO 3 '))
print('\33[1:34:40m=\33[m'*23)
print('\33[1:34m-'*23)
print('{:^23}'.format('Matriz'))
print('\33[1:34m-\33[m'*23)

matriz = list()
linha = list()
tamanhoMatriz = 3
for eixoX in range(0, tamanhoMatriz):
    for eixoY in range(0, tamanhoMatriz):
        numero = int(input(f'\33[1:33mDigite o valor da possição [{eixoX}, {eixoY}]: '))
        linha.append(numero)
    matriz.append(linha[:])
    linha.clear()

print('\33[36m-=-'*10)
for eixoX in range(len(matriz)):
    for eixoY in range(len(matriz)):
        print(f'[ {matriz[eixoX][eixoY]:^5} ]', end='')
    print()
