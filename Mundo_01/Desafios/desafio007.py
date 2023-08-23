# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

print('\33[1:30:42m===== Desafio 007 =====\33[m')
nota01 = float(input('\33[1:34mDigite a primeira nota:\33[m '))
nota02 = float(input('\33[1:36mDigete a segunda nota:\33[m '))
media = (nota01 + nota02) / 2
print('A primeira nota do aluno foi \33[1:34m{:.2f}\33[m e a segunda foi \33[1:36m{:.2f}\33[m, '
      'o aluno ficou com a média de \33[1:35m{:.2f}\33[m'.format(nota01, nota02, media))
