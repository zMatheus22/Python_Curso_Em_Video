# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um
# boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

print('\33[1:34:40m=\33[m'*23)
print('\33[1:34:40m{:^23}\33[m'.format('DESAFIO 089 - MUNDO 3 '))
print('\33[1:34:40m=\33[m'*23)
print('\33[1:34m-'*23)
print('{:^23}'.format('Sistema escolar'))
print('\33[1:34m-\33[m'*23)

aluno = list()
salaAula = list()
nota = list()
numeroAvaliacoes = 2
somaNotas = 0
while True:
    nomeAluno = str(input('\33[1:33mNome: ')).capitalize().split()
    aluno.append(nomeAluno)
    for avaliacao in range(0, numeroAvaliacoes):
        nota.append(float(input(f'Nota {avaliacao + 1}: ')))
    aluno.append(nota[:])
    nota.clear()
    salaAula.append(aluno[:])
    aluno.clear()
    continuar = ''
    while continuar not in ('S', 'N'):
        continuar = str(input('\33[32mDeseja continuar? [S/N] ')).upper().strip()[0]
    if continuar in 'N':
        break

for aluno in range(len(salaAula)):
    for quantidadeNotas in range(numeroAvaliacoes):
        somaNotas += salaAula[aluno][1][quantidadeNotas]
    mediaNotas = somaNotas / numeroAvaliacoes
    somaNotas = 0
    salaAula[aluno].append(mediaNotas)

print('\33[34m+'*26)
print(f'{"ID":<4}{"Nome":<10}{"Média":>8}')
print('-'*26)
for aluno in range(len(salaAula)):
    print(f'{aluno:<4}{salaAula[aluno][0][0]:<10}{salaAula[aluno][2]:>8.1f}')
print('-'*26)

while True:
    opecao = int(input('\33[35mDeseja ver as notas de qual aluno? [999 - Sair] '))
    if opecao == 999:
        print('\33[36m-'*30)
        break
    for aluno in range(len(salaAula)):
        if aluno == opecao:
            print('\33[32m-' * 30)
            print(f'Notas do aluno {salaAula[aluno][0][0]} são: {salaAula[aluno][1]}')
            print('-' * 30)
print('{:^27}'.format('Até a próxima'))
