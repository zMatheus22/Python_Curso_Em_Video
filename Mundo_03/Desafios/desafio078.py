# Faça um programa que leia 5 valores numéricos e guardeos em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

print('\33[1:34:40m=\33[m'*23)
print('\33[1:34:40m{:^23}\33[m'.format('DESAFIO 078 - MUNDO 3 '))
print('\33[1:34:40m=\33[m'*23)
print('\33[1:34m-'*23)
print('{:^23}'.format('Analise de números'))
print('\33[1:34m-\33[m'*23)

valores = []
for i in range(0, 5):
    valores.append(int(input('Digite o valor: ')))

print('+'*23)
print(f'Os valores digitaodos foram {valores}')
maior = sorted(valores, reverse=True)[0]

print(f'O maior valor foi {maior}, na posição ', end='')
for cont, valor in enumerate(valores):
    if maior == valor:
        print(f'{cont+1}°...', end='')

menor = sorted(valores)[0]
print(f'\nO menor valor foi {menor}, na posição ', end='')
for cont, valor in enumerate(valores):
    if menor == valor:
        print(f'{cont + 1}°...', end='')
