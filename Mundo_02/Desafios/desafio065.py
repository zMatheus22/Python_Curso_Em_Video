# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os
# valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar
# a digitar valores.

print('\33[1:34:40m=\33[m'*23)
print('\33[1:34:40m{:^23}\33[m'.format('DESAFIO 065 - MUNDO 2 '))
print('\33[1:34:40m=\33[m'*23)
print('\33[1:34m-'*23)
print('{:^23}'.format('Média'))
print('\33[1:34m-\33[m'*23)

continuar = 'S'
soma = 0
contador = 0
while continuar not in ('N', 'NAO', 'NÃO', 'NOT', 'NO'):
    numero = int(input('\33[1:33mDigite o valor: '))
    if contador == 0:
        maior = numero
        menor = numero
    else:
        if maior > numero:
            maior = numero
        elif menor < numero:
            menor = numero
    soma += numero
    contador += 1
    continuar = str(input('\33[1:35mVocê quer continuar? [S/N]')).strip().upper()

media = soma / contador
media = '{:.2f}'.format(media)
print('\33[32m+'*23)
print('{:^23}'.format(f'A média do valores digitados é de {media}'))
print('{:^23}'.format(f'O maior número digitado é o {maior}'))
print('{:^23}'.format(f'O menor número digitado é o {menor}'))
print('+'*23)
