# Crie um pacote chamado utilidadesCeV que tenha dois módulos chamados moeda e dado.
# Transfira todas as funções utilizadas nos desafios 107, 108, e 109 para o primeiro pacote e mantenha tudo funcionando.

from menu import menu
from ex111.utilidadesCeV import moeda

menu('111', 'modeda v5.0')
preco = float(input('Digite o preço: R$ '))
moeda.resumo(preco, 80, 35)
