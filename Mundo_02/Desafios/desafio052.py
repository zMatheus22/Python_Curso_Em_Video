# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

print('\33[1:34:40m=\33[m'*23)
print('\33[1:34:40m DESAFIO 052 - MUNDO 2 \33[m')
print('\33[1:34:40m=\33[m'*23)
print('\33[1:34m-'*23)
print('{:^23}'.format('Número primo'))
print('\33[1:34m-\33[m'*23)

numero = int(input('Informe o número: '))
contadorPrimo = 0
for i in range(1, numero + 1):
    if numero % i == 0:
        contadorPrimo += 1

if contadorPrimo == 2:
    print('\33[1:32m+'*23)
    print('{:^23}'.format('Número é Primo!'))
    print('{:^23}'.format(f'É divisível por 1 e {numero}'))
else:
    print('\33[1:31m+' * 23)
    print('{:^23}'.format('Número Não é Primo!'))
    print('{:^23}'.format(f'Tem {contadorPrimo} divisores'))
print('+'*23)
