# Crie um programa que leia vária números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o
# valor 999, que é a condição de parada. Na final, mostre quantos números foram digitados e qual foi a soma entre eles
# (desconsiderando o flag).

print('\33[1:34:40m=\33[m'*23)
print('\33[1:34:40m{:^23}\33[m'.format('DESAFIO 064 - MUNDO 2 '))
print('\33[1:34:40m=\33[m'*23)
print('\33[1:34m-'*23)
print('{:^23}'.format('Números'))
print('\33[1:34m-\33[m'*23)

soma = 0
contador_numero = 0
numero = 0
print('{:^23}'.format('Para sair digite 999'))
while numero != 999:
    numero = int(input('\33[33mDigite o valor: '))
    if numero != 999:
        contador_numero += 1
        soma += numero
print('\33[32m+'*23)
print('{:^23}'.format(f'A quantidade de números digitados é de {contador_numero}'))
print('{:^23}'.format(f'A soma de todos os números é de {soma}'))
