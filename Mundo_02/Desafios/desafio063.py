# Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequência
# Fibonacci.

print('\33[1:34:40m=\33[m'*23)
print('\33[1:34:40m{:^23}\33[m'.format('DESAFIO 063 - MUNDO 2 '))
print('\33[1:34:40m=\33[m'*23)
print('\33[1:34m-'*23)
print('{:^23}'.format('Fibonacci'))
print('\33[1:34m-\33[m'*23)

numeroUser = int(input('Quantas termos? '))
a = 0
b = 1
indece = 0
print('\33[36m+'*23)
while indece < numeroUser:
    if indece == 0:
        print('{:^23}'.format(f'{a}'))
    elif indece == 1:
        print('{:^23}'.format(f'{b}'))
    else:
        fibonacci = a + b
        print('{:^23}'.format(f'{fibonacci}'))
        a = b
        b = fibonacci
    indece += 1
print('+'*23)







