# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

print('\33[1:34:40m=\33[m'*23)
print('\33[1:34:40m DESAFIO 053 - MUNDO 2 \33[m')
print('\33[1:34:40m=\33[m'*23)
print('\33[1:34m-'*23)
print('{:^23}'.format('Análise Frase Palíndromo'))
print('\33[1:34m-\33[m'*23)

frase = str(input('Digite a frase para análise: ')).strip()
frase = frase.upper().split()
frase = ''.join(frase)
tamanho = len(frase) - 1
novaFrase = ''
for i in range(tamanho, -1, -1):
    novaFrase += frase[i]

if frase == novaFrase:
    print('\33[1:32m+'*23)
    print('{:^23}'.format('A Frase é Palíndromo'))
    print('{:^23}'.format(f'{frase} inversa {novaFrase}'))
else:
    print('\33[1:31m+'*23)
    print('{:^23}'.format('A Frase NÃO é Palíndromo'))
    print('{:^23}'.format(f'A frase: {frase} inversa {novaFrase}'))
print('+'*23)
