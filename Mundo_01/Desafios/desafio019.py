# Um professor que sortear um dos seus quadro aluno para apagar o quadro. Faça um programa que ajude ele, lendo o nome
# deles e escrevendo o nome do escolhido.
from random import choice

print('===== Desafio 019 =====')
nome1 = input('Primeiro o nome: ')
nome2 = input('Segundo o nome: ')
nome3 = input('Terceiro o nome: ')
nome4 = input('Quarto o nome: ')

nomes = [nome1, nome2, nome3, nome4]
ganhador = choice(nomes)
print('O aluno(a) que teve apagar o quadro é {}'.format(ganhador))
