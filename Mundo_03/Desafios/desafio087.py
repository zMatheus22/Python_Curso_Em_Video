# Aprimore o desafio 086, mostrando no final:
# A) A soma de todos os valores pares, digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

print('\33[1:34:40m=\33[m'*23)
print('\33[1:34:40m{:^23}\33[m'.format('DESAFIO 087 - MUNDO 3 '))
print('\33[1:34:40m=\33[m'*23)
print('\33[1:34m-'*23)
print('{:^23}'.format('Operação com Matriz'))
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

par = 0
somaTerceiraColuna = 0
maiorValorSegundaLinha = 0
print('\33[32m-'*23)
print('A matriz digitada: ')
for eixoX in range(len(matriz)):
    for eixoY in range(len(matriz)):
        print(f'[{matriz[eixoX][eixoY]:^5}]', end='')
        # Soma dos valores pares
        if matriz[eixoX][eixoY] % 2 == 0:
            par += matriz[eixoX][eixoY]
        # Soma dos valores da terceira coluna da matriz
        if eixoY == 2:
            somaTerceiraColuna += matriz[eixoX][eixoY]
        # Maior valor digitado que esta na segunda linha da matriz
        if eixoX == 1:
            if eixoY == 0 or maiorValorSegundaLinha < matriz[eixoX][eixoY]:
                maiorValorSegundaLinha = matriz[eixoX][eixoY]
    print()

print('\33[36m+'*23)
print(f'A soma dos valores pares é {par}')
print(f'A soma da terceiora coluna é {somaTerceiraColuna}')
print(f'O maior valor da segunda linha é {maiorValorSegundaLinha}')
