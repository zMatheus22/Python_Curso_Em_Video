# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesados.
# C) Uma listagem com as pessoas mais leves.

print('\33[1:34:40m=\33[m'*23)
print('\33[1:34:40m{:^23}\33[m'.format('DESAFIO 084 - MUNDO 3 '))
print('\33[1:34:40m=\33[m'*23)
print('\33[1:34m-'*23)
print('{:^23}'.format('Cadastro de peso'))
print('\33[1:34m-\33[m'*23)

dados = []
pessoas = []
while True:
    dados.append(str(input('\33[1:33mNome: ')).capitalize().split())
    dados.append(float(input('Peso: ')))
    pessoas.append(dados[:])
    dados.clear()

    continuar = ' '
    while continuar not in ('S', 'N'):
        continuar = str(input('\33[32mDeseja continuar? [S/N] ')).upper().split()[0]
    if continuar in 'N':
        break
print('\33[34m+'*23)
print(f'A quantidade de pessoas cadastradas {len(pessoas)}')

menorPeso = []
maiorPeso = []
for quantidade in range(len(pessoas)):
    if quantidade == 0:
        menorPeso.append(pessoas[quantidade])
        maiorPeso.append(pessoas[quantidade])
    else:
        # Menor Peso
        if pessoas[quantidade][1] <= menorPeso[len(menorPeso)-1][1]:
            if pessoas[quantidade][1] != menorPeso[len(menorPeso)-1][1]:
                menorPeso.clear()
            menorPeso.append(pessoas[quantidade])
        # Maior Peso
        elif pessoas[quantidade][1] >= maiorPeso[len(maiorPeso)-1][1]:
            if pessoas[quantidade][1] != maiorPeso[len(maiorPeso)-1][1]:
                maiorPeso.clear()
            maiorPeso.append(pessoas[quantidade])

print(f'\33[36mO menor peso é {menorPeso[0][1] :.1f} Kg. Peso de ', end='')
for indeceMenorPeso in range(len(menorPeso)):
    print(f'{menorPeso[indeceMenorPeso][0]}...', end='')

print(f'\n\33[35mO maior peso é {maiorPeso[0][1] :.1f} Kg. Peso de ', end='')
for indeceMaiorPeso in range(len(maiorPeso)):
    print(f'{maiorPeso[indeceMaiorPeso][0]}...', end='')

