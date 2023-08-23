# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela sua porção Inteira.

print('===== Desafio 016 =====')
import math

numeroReal = float(input('Digite um número real: '))
numeroInteiro = math.floor(numeroReal)
print('O número {} tem a parte inteira {}'.format(numeroReal, numeroInteiro))
