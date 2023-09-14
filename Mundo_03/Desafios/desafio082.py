# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão
# conter apenas os valores pares e os valores impares digitados, respectivamente.
# Ao final, mostre o conceúdo dos três listas geradas.

print('\33[1:34:40m=\33[m'*23)
print('\33[1:34:40m{:^23}\33[m'.format('DESAFIO 082 - MUNDO 3 '))
print('\33[1:34:40m=\33[m'*23)
print('\33[1:34m-'*23)
print('{:^23}'.format('Pares e Impares'))
print('\33[1:34m-\33[m'*23)

numeros = []
while True:
    numeros.append(int(input('\33[1:33mDigite o valor: ')))
    continuar = ' '
    while continuar not in ('S', 'N'):
        continuar = str(input('\33[32mDeseja continuar? [S/N] ')).upper().split()[0]
    if continuar in 'N':
        break
print('\33[35m+'*23)
pares = numeros[:]
impares = numeros[:]
for valor in numeros:
    if valor % 2 == 0:
        impares.remove(valor)
    elif valor % 2 == 1:
        pares.remove(valor)
print(f'Os valores digitados: {numeros}')
print(f'Os valores Pares {pares}')
print(f'Os valores Impares {impares}')
print('\33[35m+'*23)
