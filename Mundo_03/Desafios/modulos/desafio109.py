# Modifique as funções que foram criadas no desafio 107 para que elas acitem um parâmetro a mais, informando se o valor
# retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.

from menu import menu
from ex109 import moeda

menu('109', 'modeda v3.0')
preco = float(input('Digite o preço: R$ '))
print(f'A metade de {moeda.moeda(preco)} é {moeda.metade(preco, True)}')
print(f'O dobro de {moeda.moeda(preco)} é {moeda.dobrar(preco, True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(preco, 10, True)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(preco, 13, True)}')

