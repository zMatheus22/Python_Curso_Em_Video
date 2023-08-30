# Faça um programa que calcule a soma entre todos os números impares que são múltiplos de três e que se encontram no
# intervalo de 1 até 500

print('\33[1:34:40m=\33[m'*23)
print('\33[1:34:40m DESAFIO 048 - MUNDO 2 \33[m')
print('\33[1:34:40m=\33[m'*23)
print('\33[1:34m-'*23)
print('{:^23}'.format('Números 1 à 500'))
print('{:^23}'.format('Impares'))
print('{:^23}'.format('Múltiplos de 3'))
print('\33[1:34m-\33[m'*23)

soma = 0
for numero in range(1, 501):
    if numero % 2 == 1:
        if numero % 3 == 0:
            soma = soma + numero
print('\33[1:32m{:^23}'.format(f'Soma: {soma}'))
