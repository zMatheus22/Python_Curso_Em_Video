# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

print('\33[1:34:40m=\33[m'*23)
print('\33[1:34:40m{:^23}\33[m'.format('DESAFIO 072 - MUNDO 3 '))
print('\33[1:34:40m=\33[m'*23)
print('\33[1:34m-'*23)
print('{:^23}'.format('Número por Extenso'))
print('\33[1:34m-\33[m'*23)

extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze',
           'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    numeroUser = int(input('\33[1:33mInforme o número entre 0 e 20: '))
    if numeroUser >= 0 and numeroUser <= 20:
        break
    print('\33[31mTente novamente!')

print('\33[36m+'*23)
print(f'O número {numeroUser} por extenso é \33[4m{extenso[numeroUser]}')
