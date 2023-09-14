# Adicione ao módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), que mostre na tela algumas
# informações geradas pelas funções que já temos no módulo criado até aqui.

from menu import menu
from ex110 import moeda

menu('110', 'modeda v4.0')
preco = float(input('Digite o preço: R$ '))
moeda.resumo(preco, 96, 35)
