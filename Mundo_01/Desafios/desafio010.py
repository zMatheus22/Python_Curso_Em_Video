# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
# Cotação US$ 1.00 = R$ 4.79 (13/07/2023) (dolar)
# Cotação   € 1.00 = R$ 5.39 (13/07/2023) (euro)
# Cotação   ¥ 1.00 = R$ 0.67 (13/07/2023) (yuan china)

print('\33[1:32:40m===== Desafio 010 =====\33[m')
dolar = 4.79
euro = 5.39
yuan = 0.67
valor = float(input('\33[1:32mDigite o valor disponivel para a compra: R$ \33[m'))

print('\33[1:34mCom o valor de R$ {:.2f} e a cotação do dolar estando em R$ {:.2f} você tem \33[4mUS$ {:.2f}\33[m '
      '\33[1:34mdisponivel para a compra!\33[m'.format(valor, dolar, (valor/dolar)))

print('\33[1:36mCom o valor de R$ {:.2f} e a cotação do euro estando em R$ {:.2f} você tem \33[4m€ {:.2f}\33[m '
      '\33[1:36mdisponivel para a compra!\33[m'.format(valor, euro, (valor/euro)))

print('\33[1:31mCom o valor de R$ {:.2f} e a cotação do yuan chineis estando em R$ {:.2f} você tem \33[4m¥ {:.2f}\33[m '
      '\33[1:31mdisponivel para a compra!\33[m'.format(valor, yuan, (valor/yuan)))
