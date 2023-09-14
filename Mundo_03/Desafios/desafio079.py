# Crie um programa onde o usuário possa digita vários valores numéricos e cadastre-os em uma lista. Caso o número já
# existe lá dentro, ele não será adicionado.
# No final, serão exibido todos os valores únicos digitados, em ordem crescente.

print('\33[1:34:40m=\33[m'*23)
print('\33[1:34:40m{:^23}\33[m'.format('DESAFIO 079 - MUNDO 3 '))
print('\33[1:34:40m=\33[m'*23)
print('\33[1:34m-'*23)
print('{:^23}'.format('Cadastro de números'))
print('\33[1:34m-\33[m'*23)

numeros = []
while True:
    numeros.append(int(input('\33[1:33mDigite o valor: ')))
    continuar = ' '
    if len(numeros) > 1:
        numeros = sorted(numeros)
        for cont, valor in enumerate(numeros):
            if numeros[cont - 1] == numeros[cont]:
                numeros.remove(valor)
                print('\33[31mValor duplicado, não adicionado!')
    while continuar not in ('S', 'N'):
        continuar = str(input('\33[36mDeseja continuar? [S/N]')).upper().strip()[0]
    if continuar in 'N':
        break
print('\33[32m+'*23)
print(f'Os valores cadastrados foram: {numeros}')
