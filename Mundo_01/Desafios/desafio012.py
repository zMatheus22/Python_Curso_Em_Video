# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

print('\33[1:36:40m===== Desafio 012 =====\33[m')
valor = float(input('\33[1:36mDigite o valor do produto: R$ \33[m'))
desconto = 5
valorDesconto = valor - valor * (desconto / 100)
print('\33[1:36mO valor sem o desconto R$ {:.2f}, o valor com o desconto de \33[32m{}% \33[4mR$ {:.2f}\33[m'
      .format(valor, desconto, valorDesconto))
