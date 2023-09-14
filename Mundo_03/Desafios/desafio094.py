# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e
# todos os dicionários em uma lista. No final mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade do grupo.
# C) Uma lista com todas as mulheres. uma lista com todas as pessoas com idade acima da média.

print('\33[1:34:40m=\33[m'*23)
print('\33[1:34:40m{:^23}\33[m'.format('DESAFIO 094 - MUNDO 3'))
print('\33[1:34:40m=\33[m'*23)
print('\33[1:34m-'*23)
print('{:^23}'.format('Cadastro de Pessoas'))
print('\33[1:34m-\33[m'*23)

pessoas = list()
dados = dict()
somaIdade = quantidadeMulher = 0
print('\33[1:32m')
while True:
    dados['nome'] = str(input('Nome: ')).strip().capitalize()
    dados['sexo'] = ''
    while dados['sexo'] not in ('M', 'F'):
        dados['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
    dados['idade'] = int(input('Idade: '))
    somaIdade += dados['idade']
    if dados['sexo'] in 'F':
        quantidadeMulher = 1
    pessoas.append(dados.copy())
    continuar = ''
    while continuar not in ('S', 'N'):
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar in 'N':
        mediaIdade = somaIdade / len(pessoas)
        break

print('\33[35m+'*30)
print(f'- O grupo tem {len(pessoas)} pessoas.')

print(f'- A média de idade é de {mediaIdade} anos.')
if quantidadeMulher == 1:
    print('- A(s) mulhere(s) cadastrada(s) foram: ', end='')
    for pessoa in pessoas:
        if pessoa['sexo'] in 'F':
            print(pessoa['nome'], end=' ')

print('\n- Lista das pessoas que estão acima da média de idade: ')
for pessoa in pessoas:
    if pessoa['idade'] > mediaIdade:
        for key, valor in pessoa.items():
            print(f'    {key.capitalize()}: {valor}', end='')
        print()
print('<< ENCERRADO >>')
