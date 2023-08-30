# Refaça o Desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão
# usando a estrutura while

print('\33[1:34:40m=\33[m'*23)
print('\33[1:34:40m{:^23}\33[m'.format('DESAFIO 061 - MUNDO 2 '))
print('\33[1:34:40m=\33[m'*23)
print('\33[1:34m-'*23)
print('{:^23}'.format('PA v2.0'))
print('\33[1:34m-\33[m'*23)

primeiroTermo = int(input('\33[1:33mDigite o número: '))
razaoPA = int(input('Digite a razão PA: '))
ultimoTermo = primeiroTermo + 10 * razaoPA
op = primeiroTermo
indice = 1
print('\33[1:36m+'*23)
print('{:^23}'.format(f'A PA, 1° termo {primeiroTermo}, razão {razaoPA}'))
while op != ultimoTermo:
    if indice < 10:
        print('{:^23}'.format(f'0{indice}°: {op}'))
    else:
        print('{:^23}'.format(f'{indice}°: {op}'))
    op += razaoPA
    indice += 1
print('+'*23)


