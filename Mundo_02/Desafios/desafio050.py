# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor
# digitado for impar, desconsidere-o.

print('\33[1:34:40m=\33[m'*23)
print('\33[1:34:40m DESAFIO 050 - MUNDO 2 \33[m')
print('\33[1:34:40m=\33[m'*23)
print('\33[1:34m-'*23)
print('{:^23}'.format('Soma Par'))
print('\33[1:34m-\33[m'*23)

soma = 0
for i in range(1, 7):
    numeroUser = int(input(f'\33[1:33mDigite o {i}° valor: '))
    if numeroUser % 2 == 0:
        soma = soma + numeroUser
print(f'\33[1:36mA Soma dos pares informado é {soma}')

