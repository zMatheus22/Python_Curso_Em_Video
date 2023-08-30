# Faça um programa que leia um número qualquer e mostre o seu fatorial.

print('\33[1:34:40m=\33[m'*23)
print('\33[1:34:40m{:^23}\33[m'.format('DESAFIO 060 - MUNDO 2 '))
print('\33[1:34:40m=\33[m'*23)
print('\33[1:34m-'*23)
print('{:^23}'.format('Fatorial'))
print('\33[1:34m-\33[m'*23)

numero = int(input('\33[1:33mDigite o número: '))
fat = 1
op = numero
while op != 0:
    fat *= op
    op -= 1
    if numero in (0, 1):
        fat = 1
print('\33[36m+'*23)
print('{:^23}'.format(f'O fatorial do número {numero}! é {fat}'))
