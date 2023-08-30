# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o
# valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles
# (desconsiderando o flag).

print('\33[1:34:40m=\33[m'*23)
print('\33[1:34:40m{:^23}\33[m'.format('DESAFIO 066 - MUNDO 2 '))
print('\33[1:34:40m=\33[m'*23)
print('\33[1:34m-'*23)
print('{:^23}'.format('Análise de números'))
print('\33[1:34m-\33[m'*23)

soma = contador = 0
while True:
    numero = int(input('\33[1:33mDigite o valor, [999, para sair]: '))
    if numero == 999:
        break
    soma += numero
    contador += 1
print('\33[35m+'*23)
print('{:^23}'.format(f'A soma dos valores é {soma}'))
print('{:^23}'.format(f'A quantidade de valores informados {contador}'))
print('+'*23)
