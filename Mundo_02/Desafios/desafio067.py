# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será inteirrompido quando o número solicitado for negativo.

print('\33[1:34:40m=\33[m'*23)
print('\33[1:34:40m{:^23}\33[m'.format('DESAFIO 067 - MUNDO 2 '))
print('\33[1:34:40m=\33[m'*23)
print('\33[1:34m-'*23)
print('{:^23}'.format('Tabuada'))
print('\33[1:34m-\33[m'*23)

while True:
    tabuada = int(input('\33[1:33mDigite o valor: '))
    if tabuada <= 0:
        break
    indece = 0
    print('\33[35m+'*23)
    while indece <= 10:
        multiplicacao = tabuada * indece
        print('{:^23}'.format(f'{tabuada} x {indece} = {multiplicacao}'))
        indece += 1
    print('+' * 23)
print('{:^23}'.format('\33[32mSistema de Tabuada encerrado!'))
print('{:^23}'.format('Até a próxima!'))
