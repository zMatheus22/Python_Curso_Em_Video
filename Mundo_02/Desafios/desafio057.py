# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a
# digitação novamente até ter um valor correto.

print('\33[1:34:40m=\33[m'*23)
print('\33[1:34:40m{:^23}\33[m'.format('DESAFIO 057 - MUNDO 2 '))
print('\33[1:34:40m=\33[m'*23)
print('\33[1:34m-'*23)
print('{:^23}'.format('Sexo'))
print('\33[1:34m-\33[m'*23)

sexo = str(input('\33[1:33mInforme o sexo: ')).upper().strip()[0]
while sexo not in 'MF':
    print('\33[31mVocê informou um sexo diferente de (M/F)')
    sexo = str(input('\33[33mInforme o sexo: ')).upper().strip()
print('\33[32m{:^23}'.format(f'Sexo {sexo} cadastrado!'))
