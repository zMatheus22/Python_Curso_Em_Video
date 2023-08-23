# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

print('===== Desafio 033 =====')
num01 = int(input('Digite o primeiro número: '))
num02 = int(input('Digite o segundo número: '))
num03 = int(input('Digite o terceiro número: '))
numeros = sorted([num01, num02, num03])

print('O menor número é {}'.format(numeros[0]))
print('O maior número é {}'.format(numeros[2]))
