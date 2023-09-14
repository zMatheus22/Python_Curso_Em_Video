# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição
# correta de inserção (sem usar o sort())
# No final, mostre a lista ordenada na tela.

print('\33[1:34:40m=\33[m'*23)
print('\33[1:34:40m{:^23}\33[m'.format('DESAFIO 080 - MUNDO 3 '))
print('\33[1:34:40m=\33[m'*23)
print('\33[1:34m-'*23)
print('{:^23}'.format('Organização de lista'))
print('\33[1:34m-\33[m'*23)

valores = []
for i in range(0, 5):
    valores.append(int(input('Digite o valor: ')))
    if len(valores) != 1:
        cont = 1
        while valores[len(valores) - cont - 1] > valores[len(valores) - cont]:
            valores.insert(len(valores) - cont - 1, valores[len(valores) - cont])
            valores.pop(len(valores) - cont)
            if len(valores) - cont - 1 != 0:
                cont += 1

print(valores)
