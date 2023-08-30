# Crie um programa que leia o ano de nascimento de sete pessoas. No final mostre quantas pessoas ainda não atingiram a
# maioridade e quantas já são maiores.

from datetime import date

print('\33[1:34:40m=\33[m'*23)
print('\33[1:34:40m{:^23}\33[m'.format('DESAFIO 054 - MUNDO 2 '))
print('\33[1:34:40m=\33[m'*23)
print('\33[1:34m-'*23)
print('{:^23}'.format('Maioridade'))
print('\33[1:34m-\33[m'*23)

anoAtual = date.today().year
maioridade = ''
menoridade = ''
contMaior = 0
contMenor = 0
for i in range(1, 8):
    nascimento = int(input(f'\33[1:33mData de nascimento da {i}° pessoas: '))
    idade = anoAtual - nascimento
    if idade < 21:
        menoridade += str(i)
        contMenor += 1
    else:
        maioridade += str(i)
        contMaior += 1

print('\33[1:34m-\33[m'*23)
print(f'\33[1:32mA quantidade de pessoas de maiores de idade é {contMaior}, são as pessoas {list(maioridade)}')
print(f'\33[1:35mA quantidade de pessoas de menores de idade é {contMenor}, são as pessoas {list(menoridade)}')

