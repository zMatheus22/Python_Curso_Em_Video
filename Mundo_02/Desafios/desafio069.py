# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar
# se o usuário quer ou não continuar. No final, mostre:
# A) Quantas pessoas tem mais de 18 anos.
# B) Quantos homens foram cadastrados.
# C) Quantas mulheres tem menos de 20 anos.

print('\33[1:34:40m=\33[m'*23)
print('\33[1:34:40m{:^23}\33[m'.format('DESAFIO 069 - MUNDO 2 '))
print('\33[1:34:40m=\33[m'*23)
print('\33[1:34m-'*23)
print('{:^23}'.format('Cadastro de Usuário'))
print('\33[1:34m-\33[m'*23)

quantidadeHomem = quantidadeMulher = quantidadeAduto = 0
while True:
    sexo = str(input('\33[1:33mDigite o sexo: [M/F] ')).upper().strip()[0]
    while sexo not in ('M', 'F'):
        print('\33[1:31mDados inválidos!')
        sexo = str(input('\33[1:33mDigite o sexo: [M/F] ')).upper().strip()[0]
    idade = int(input('Digite a idade: '))
    if sexo in 'M':
        quantidadeHomem += 1
    elif sexo in 'F' and idade < 20:
        quantidadeMulher += 1
    if idade > 18:
        quantidadeAduto += 1

    continuar = str(input('Desseja continuar com o cadastro? [S/N] ')).upper().strip()[0]
    while continuar not in ('S', 'N'):
        continuar = str(input('Desseja continuar com o cadastro? [S/N] ')).upper().strip()[0]
    if continuar in 'N':
        break

print('\33[36m+'*23)
print(f'A quantidade de pessoas com mais de 18 anos é {quantidadeAduto}')
print(f'A quantidade de homens cadastrados é {quantidadeHomem}')
print(f'A quantidade de mulheres com menos de 20 anos é {quantidadeMulher}')
print('{:^23}'.format('Fim, até mais!'))
