# Escreva um progrma que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
# -> O primeiro valor é MAIOR
# -> O primeiro valor é MENOR
# -> Não existe valor maior, os dois são iguais

print('\33[1:34:40m=\33[m'*23)
print('\33[1:34:40m DESAFIO 038 - MUNDO 2 \33[m')
print('\33[1:34:40m=\33[m'*23)

num01 = int(input('\33[1:33mDigite o primeiro valor: '))
num02 = int(input('Digite o segundo valor: \33[m'))

if num01 == num02:
    print('\33[1:34mNão existe valor maior, \33[4:36mos valores são iguais\33[m')
elif num01 > num02:
    print('\33[1:34mO \33[4:36mprimeiro valor\33[m\33[1:34m é o Maior\33[m')
else:
    print('\33[1:34mO \33[4:36msegundo valor\33[m\33[1:34m é Maior\33[m')
