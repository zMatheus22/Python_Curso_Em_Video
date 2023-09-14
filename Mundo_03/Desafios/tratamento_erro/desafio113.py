# Reescreva a função leiaInt() que fizemos no desafio104, incluindo agora a possibilidade da digitação de um número de
# tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

from ex113 import dados
from menu import menu

menu('113', 'Analisando números')
numeroInteiro = dados.leiaInt('\33[1:32mDigite o número Inteiro: ')
numeroReal = dados.leiaReal('\33[1:32mDigite o número Real: ')
print('\33[36m-'*30)
print(f'O numero inteiro informado foi {numeroInteiro} \nO número real informado foi {numeroReal}')
