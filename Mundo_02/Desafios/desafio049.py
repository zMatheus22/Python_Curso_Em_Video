# Refaça o Desafio 009, mostrando a tabuada de um que o usuário escolher, só que agora utilizando um laço 'for'.

print('\33[1:34:40m=\33[m'*23)
print('\33[1:34:40m DESAFIO 049 - MUNDO 2 \33[m')
print('\33[1:34:40m=\33[m'*23)
print('\33[1:34m-'*23)
print('{:^23}'.format('Tabuada'))
print('\33[1:34m-\33[m'*23)

tabuada = int(input('\33[1:33mQual tabuada você quer? '))
print('\33[1:36m+'*23)
for multiplo in range(0, 11):
    resultado = tabuada * multiplo
    print('{:^23}'.format(f'{tabuada} x {multiplo} = {resultado}'))
print('+'*23)
