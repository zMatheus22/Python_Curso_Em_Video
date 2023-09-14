# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final mostre o
# conteúdo da estrutura na tela

print('\33[1:34:40m=\33[m'*23)
print('\33[1:34:40m{:^23}\33[m'.format('DESAFIO 090 - MUNDO 3 '))
print('\33[1:34:40m=\33[m'*23)
print('\33[1:34m-'*23)
print('{:^23}'.format('Situação escolar'))
print('\33[1:34m-\33[m'*23)

aluno = dict()

aluno['nome'] = str(input('Nome: ')).strip().capitalize()
aluno['media'] = float(input('Média: '))
if aluno['media'] < 5:
    aluno['situacao'] = 'Reprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situacao'] = 'Recuperação'
elif aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
print('+'*23)
for key, valor in aluno.items():
    print(f'{key.capitalize()}: {valor}')
