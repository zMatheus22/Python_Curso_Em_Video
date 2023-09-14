# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores ordenada de forma descrecente.
# C) Se o valor 5 foi digitado e está ou não na lista.

print('\33[1:34:40m=\33[m'*23)
print('\33[1:34:40m{:^23}\33[m'.format('DESAFIO 081 - MUNDO 3 '))
print('\33[1:34:40m=\33[m'*23)
print('\33[1:34m-'*23)
print('{:^23}'.format('Extração de dados'))
print('\33[1:34m-\33[m'*23)

valores = []
while True:
    valores.append(int(input('\33[1:33mDigite o valor: ')))

    continuar = ''
    while continuar not in ('S', 'N'):
        continuar = str(input('\33[36mDeseja continuar? [S/N] ')).upper().split()[0]
    if continuar in 'N':
        break
print('\33[32m+'*23)
valoresInvertidos = sorted(valores, reverse=True)
print(f'Você digitou {len(valores)} valores')
print(f'A ordem decresente é {valoresInvertidos}')
if 5 in valores:
    print(f'\33[32mO valores 5 foi digitado, na {valoresInvertidos.index(5) + 1}° posição')
else:
    print('\33[31mO valor 5 não foi digitado')
print('\33[32m+'*23)
