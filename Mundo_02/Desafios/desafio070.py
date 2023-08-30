# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar.
# No final, mostre:
# A) Qual é o total gasto na compra.
# B) Quantos produtos custam mais de R$ 1000,00
# C) Qual é o nome do produto mais barato.

from datetime import date
print('\33[1:34:40m=\33[m'*23)
print('\33[1:34:40m{:^23}\33[m'.format('DESAFIO 070 - MUNDO 2 '))
print('\33[1:34:40m=\33[m'*23)
print('\33[1:34m-'*23)
print('{:^23}'.format('Compras de Produtos'))
print('\33[1:34m-\33[m'*23)
quantidadeProduto = 1
somaGasto = quantidadeProdutoMais1000 = 0
data = date.today()
while True:
    print('{:^23}'.format(f'\33[1:34mProduto {quantidadeProduto}'))
    nomeProduto = str(input('\33[33mNome do produto: ')).capitalize().strip()
    valorProduto = float(input('Valor do produto: R$ '))
    if valorProduto > 1000:
        quantidadeProdutoMais1000 += 1
    if quantidadeProduto == 1 or valorProduto < valorProdutoBarato:
        nomeProdutoBarato = nomeProduto
        valorProdutoBarato = valorProduto
    quantidadeProduto += 1
    somaGasto += valorProduto

    continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    while continuar not in 'S':
        print('{:^23}'.format('\33[31mErro!'))
        continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if continuar in 'N':
        break

    print('\33[1:34m_'*23)

print('\33[1:36m+'*23)
print('{:^23}'.format(f'Data: {data}'))
print('{:^23}'.format('Total gasto: '))
print('{:^23}'.format(f'R$ {somaGasto:.2f}'))
print('-'*23)
print('{:^23}'.format('Acima de 1 mil reais:'))
print('{:^23}'.format(f'{quantidadeProdutoMais1000}'))
print('-'*23)
print('{:^23}'.format('Produto mais barato: '))
print('{:^23}'.format(f'{nomeProdutoBarato}, R$ {valorProdutoBarato:.2f}'))
print('+'*23)
