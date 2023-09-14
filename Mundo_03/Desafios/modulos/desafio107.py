# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobrar(), metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.

from menu import menu
from ex107 import moeda

menu('107', 'modeda v1.0')
preco = float(input('Digite o preço: R$ '))
print(f'A metade de {preco} é {moeda.metade(preco)}')
print(f'O dobro de {preco} é {moeda.dobrar(preco)}')
print(f'Aumentando 10%, temos {moeda.aumentar(preco, 10)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(preco, 13)}')
