# Crie um programa  onde o usuário possa digitar sete valores númericos e cadastre-os em uma lista única que mantenha
# separados os valores pares e impares. No final, mostre os valores pares e ímpares em ordem crecente.

print('\33[1:34:40m=\33[m'*23)
print('\33[1:34:40m{:^23}\33[m'.format('DESAFIO 085 - MUNDO 3 '))
print('\33[1:34:40m=\33[m'*23)
print('\33[1:34m-'*23)
print('{:^23}'.format('Pares e Ímpares'))
print('\33[1:34m-\33[m'*23)

impar = []
par = []
valores = []
for indece in range(1, 8):
    numeroUser = int(input(f'\33[1:33mDigite o {indece}° valor: '))
    if numeroUser % 2 == 0:
        par.append(numeroUser)
    elif numeroUser % 2 == 1:
        impar.append(numeroUser)

par.sort()
impar.sort()
valores.append(par[:])
valores.append(impar[:])

print('\33[36m+'*23)
print(f'Os valores pares são {valores[0]}')
print(f'\33[1:35mOs valores ímpares são {valores[1]}')
