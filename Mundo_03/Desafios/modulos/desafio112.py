# Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. Crie uma função chamada
# leiaDinheiro() que seja capaz de funcionar como a função input() mas com uma validação de dados para aceitar apenas
# valores que sejam monetários.

from menu import menu
from ex112.utilidadesCeV import dado
from ex112.utilidadesCeV import moeda

preco = dado.leiaDinheiro('\33[1:32mDigite o preço: R$ ')
moeda.resumo(preco, 80, 35)
