# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor pesso lidos.

print('\33[1:34:40m=\33[m'*23)
print('\33[1:34:40m{:^23}\33[m'.format('DESAFIO 055 - MUNDO 2 '))
print('\33[1:34:40m=\33[m'*23)
print('\33[1:34m-'*23)
print('{:^23}'.format('Balança'))
print('\33[1:34m-\33[m'*23)

maiorPeso = 0
menorPeso = 0
for i in range(1, 6):
    peso = float(input(f'\33[1:33mInforme o peso da {i}° pessoa (Kg): '))
    if i == 1:
        maiorPeso = peso
        menorPeso = peso
    else:
        if peso > maiorPeso:
            maiorPeso = peso
            pessoaMaior = i
        elif peso < menorPeso:
            menorPeso = peso
            pessoaMenor = i
print('\33[1:36m+'*23)
print(f'O maior peso foi da {pessoaMaior}° pessoa, com o peso de {maiorPeso :.2f} Kg')
print(f'O menor peso foi da {pessoaMenor}° pessoa, com o peso de {menorPeso :.2f} Kg')
print('+'*23)

