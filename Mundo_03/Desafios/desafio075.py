# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

print('\33[1:34:40m=\33[m'*23)
print('\33[1:34:40m{:^23}\33[m'.format('DESAFIO 075 - MUNDO 3 '))
print('\33[1:34:40m=\33[m'*23)
print('\33[1:34m-'*23)
print('{:^23}'.format('Análise de números com Tuplas'))
print('\33[1:34m-\33[m'*23)

numeros = (int(input('\33[1:33mDigite o primeiro número: ')), int(input('Digite o segundo número: ')),
           int(input('Digite o terceiro número: ')), int(input('Digite o último número: ')))

quantidadeNove = 0
possicaoNumeroTres = 0
quatidadeImpar = 0
for possicao in range(len(numeros)):
    if numeros[possicao] == 9:
        quantidadeNove += 1
    if numeros[possicao] == 3:
        possicaoNumeroTres = possicao
    if numeros[possicao] % 2 == 1:
        quatidadeImpar += 1

print('\33[32m+'*23)
if quantidadeNove != 0:
    print(f'\33[32mO valor 9 foi digitado {quantidadeNove} vezes')
else:
    print('\33[31mO valor 9 não foi digitados')
if possicaoNumeroTres != 0:
    print(f'\33[32mO valor 3 esta na {possicaoNumeroTres + 1}° possition')
else:
    print('\33[31mO valor 3 não foi digitados')

for possicao in range(len(numeros)):
    if quatidadeImpar == 4:
        print('\33[31mNão tem número par.')
    else:
        print('\33[32mOs valores pares digitados foram:', end=' ')
        if numeros[possicao] % 2 == 0:
            print(numeros[possicao], end=' ')

