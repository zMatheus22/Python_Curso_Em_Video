# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e
# mostre o comprimento da hipotenusa.
import math

print('===== Desafio 017 =====')
catetoOposto = float(input('Digite o cateto oposto: '))
catetoAdjacente = float(input('Digite o cateto adjacente: '))
hipotenusa = math.sqrt(catetoOposto ** 2 + catetoAdjacente ** 2)
print('Hipotenusa: {:.2f}'.format(hipotenusa))
