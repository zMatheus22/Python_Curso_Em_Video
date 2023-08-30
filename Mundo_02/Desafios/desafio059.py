# Crie um programa que leia dois valores e mostre um menu na tela:
# [1] - Somar
# [2] - Multiplicar
# [3] - Maior
# [4] - Novos números
# [5] - Sair do programa
# Seu programa deverá realizar o operação solicitada em cada caso.

print('\33[1:34:40m=\33[m'*23)
print('\33[1:34:40m{:^23}\33[m'.format('DESAFIO 059 - MUNDO 2 '))
print('\33[1:34:40m=\33[m'*23)
print('\33[1:34m-'*23)
print('{:^23}'.format('Analise de número'))
print('\33[1:34m-\33[m'*23)

numero01 = int(input('\33[1:33mDigite o primeiro número: '))
numero02 = int(input('Digite o segundo número: '))
opcao = 0
while opcao != 5:
    print('\33[34m+'*23)
    print('[1] - Soma')
    print('[2] - Multiplicar')
    print('[3] - Maior número')
    print('[4] - Novos números')
    print('[5] - Sair do programa')
    opcao = int(input('\33[33mDigite a sua opcao: '))
    if opcao not in (1, 2, 3, 4, 5):
        print('\33[31m{:^23}'.format('Você informou uma opção inválida.'))
    elif opcao == 1:
        soma = numero01 + numero02
        print('{:^23}'.format(f'\33[32mA Soma de {numero01} + {numero02} é {soma}'))
    elif opcao == 2:
        multiplicacao = numero01 * numero02
        print('{:^23}'.format(f'\33[36mA multiplicação de {numero01} x {numero02} é {multiplicacao}'))
    elif opcao == 3:
        maior = numero01
        if numero01 == numero02:
            print('{:^23}'.format(f'\33[35mOs dois números informados, "{numero02}", são iguais.'))
        elif maior < numero02:
            print('{:^23}'.format(f'\33[35mO maior número é o {numero02}'))
        else:
            print('{:^23}'.format(f'\33[35mO maior número é o {numero01}'))
    elif opcao == 4:
        print('{:^23}'.format('Novos números.'))
        numero01 = int(input('\33[33mDigite o primeiro número: '))
        numero02 = int(input('Digite o segundo número: '))

print('\33[34m+'*23)
print('{:^23}'.format('Fim'))
