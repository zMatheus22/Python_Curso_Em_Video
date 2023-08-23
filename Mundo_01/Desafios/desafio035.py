# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo

print('===== Desafio 035 =====')
r1 = float(input('Digite a primeira reta: '))
r2 = float(input('Digite a segunda reta: '))
r3 = float(input('Digite a terceira reta: '))

t1 = (r2 + r3) > r1
t2 = (r1 + r3) > r2
t3 = (r1 + r2) > r3

if t1 & t2 & t3:
    print('É possivel formar um triângulo.')
else:
    print('Não é possivel formar um triângulo.')
