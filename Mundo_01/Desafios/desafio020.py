# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalho dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
from random import randint

print('===== Desafio 020 =====')
nome1 = input('Primeiro nome do aluno: ')
nome2 = input('Segundo o nome do aluno: ')
nome3 = input('Terceiro o nome do aluno: ')
nome4 = input('Quarto o nome do aluno: ')
sorteio = randint(0, 3)
alunos = [nome1, nome2, nome3, nome4]

print('A ordem de apresentação será:')
print('1°-> {}'.format(alunos[sorteio]))
alunos.remove(alunos[sorteio])
sorteio = randint(0, 2)
print('2°-> {}'.format(alunos[sorteio]))
alunos.remove(alunos[sorteio])
sorteio = randint(0, 1)
print('3°-> {}'.format(alunos[sorteio]))
alunos.remove(alunos[sorteio])
print('4°-> {}'.format(alunos[0]))
