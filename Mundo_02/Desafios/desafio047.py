# Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

print('\33[1:34:40m=\33[m'*23)
print('\33[1:34:40m DESAFIO 047 - MUNDO 2 \33[m')
print('\33[1:34:40m=\33[m'*23)
print('\33[1:34m-'*23)
print('{:^23}'.format('Números Pares de 1 à 50'))
print('\33[1:34m-\33[m'*23)

print('\33[1:35m+'*23)
for par in range(1, 51):
    if par % 2 == 0:
        if par < 10:
            print('\33[1:35m{:^23}'.format(f'Número Par: 0{par}'))
        else:
            print('\33[1:35m{:^23}'.format(f'Número Par: {par}'))
print('+'*23)
