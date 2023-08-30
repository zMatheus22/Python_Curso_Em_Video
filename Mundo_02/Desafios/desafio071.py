# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor
# a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: Considere que o caixa possui cédulas de R$ 50, R$ 20, R$ 10 e R$1

print('\33[1:34:40m=\33[m'*23)
print('\33[1:34:40m{:^23}\33[m'.format('DESAFIO 071 - MUNDO 2 '))
print('\33[1:34:40m=\33[m'*23)
print('\33[1:34m-'*23)
print('{:^23}'.format('Caixa eletrônico'))
print('\33[1:34m-\33[m'*23)

valor50 = valor20 = valor10 = valor1 = 0

while True:
    sacar = int(input('\33[1:33mQual o valor que você deseja sacar? '))
    # R$ 50, R$ 20, R$ 10 e R$1
    while sacar >= 50:
        valor50 += 1
        sacar -= 50
    while sacar >= 20:
        valor20 += 1
        sacar -= 20
    while sacar >= 10:
        valor10 += 1
        sacar -= 10
    while sacar >= 1:
        valor1 += 1
        sacar -= 1
    if sacar == 0:
        break

print('\33[36m+'*23)
print('{:^23}'.format('Quantidade de modas'))
if valor50 > 0:
    print('{:^23}'.format(f'Notas de R$ 50,00: {valor50}'))
if valor20 > 0:
    print('{:^23}'.format(f'Notas de R$ 20,00: {valor20}'))
if valor10 > 0:
    print('{:^23}'.format(f'Notas de R$ 10,00: {valor10}'))
if valor1 > 0:
    print('{:^23}'.format(f'Notas de R$ 1,00: {valor1}'))
