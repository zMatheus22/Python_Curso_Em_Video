# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

print('===== Desafio 018 =====')
import math

angulo = float(input('Digite o ângulo: '))
radiano = math.radians(angulo)

seno = math.sin(radiano)
cosseno = math.cos(radiano)
tangente = math.tan(radiano)

print('Com o ângulo de {}° temos \n O seno de {:.3f} \n O cosseno {:.3f} \n A tangente {:.3f}'
      .format(angulo, seno, cosseno, tangente))
