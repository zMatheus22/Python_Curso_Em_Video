# Desenvolva um programa que leia o primeiro termo e a razão de um PA. No final, mostre os 10 primeiros termos dessa
# progressão

print('\33[1:34:40m=\33[m'*23)
print('\33[1:34:40m DESAFIO 051 - MUNDO 2 \33[m')
print('\33[1:34:40m=\33[m'*23)
print('\33[1:34m-'*23)
print('{:^23}'.format('Razão PA'))
print('\33[1:34m-\33[m'*23)

primeiroTermo = int(input('\33[1:33mQual é o primeiro termo? '))
razao = int(input('Qual é a razão da PA? '))
ultimoTermo = primeiroTermo + 10 * razao
indice = 1

print('\33[1:36m+'*23)
for valor in range(primeiroTermo, ultimoTermo, razao):
    print('{:^23}'.format(f'{indice}°: {valor}'))
    indice += 1
print('+'*23)
