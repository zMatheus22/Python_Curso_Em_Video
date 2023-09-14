# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# Na final, mostre uma listagem de preços, organizando os dados em forma tabular.

print('\33[1:34:40m=\33[m'*23)
print('\33[1:34:40m{:^23}\33[m'.format('DESAFIO 076 - MUNDO 3 '))
print('\33[1:34:40m=\33[m'*23)
print('\33[1:34m-'*23)
print('{:^23}'.format('Listagem de Preços'))
print('\33[1:34m-\33[m'*23)

produtos = ('Mouse Gamer', 120.90, 'Monitor Gamer', 619, 'Cadeira Gamer', 439, 'Teclado Mecânico', 229.99,
            'Controle PS5', 424.99, 'Playstation 5', 3959.95, 'Volante G29', 1673.98, 'SSD 1 TB', 269.99)

for item in range(len(produtos)):
    if item % 2 == 0:
        print(f'\33[1:35m{produtos[item]:.<25}', end='')
    else:
        print(f'\33[32mR$ {produtos[item] :>5.2f}')
