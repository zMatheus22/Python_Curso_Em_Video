# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# - A média de idade do grupo
# - Qual é o nome do homem mais velho.
# - Quantas mulheres têm menos de 20 anos

print('\33[1:34:40m=\33[m'*23)
print('\33[1:34:40m{:^23}\33[m'.format('DESAFIO 056 - MUNDO 2 '))
print('\33[1:34:40m=\33[m'*23)
print('\33[1:34m-'*23)
print('{:^23}'.format('Cadastro de Pessoas'))
print('\33[1:34m-\33[m'*23)

velho = 0
mulheresMenor = 0
somaIdade = 0

for i in range(1, 5):
    print('\33[1:32m{:^23}'.format(f'Dados da {i}° Pessoa\n'))
    nome = str(input('\33[1:33mQual é o seu nome? ')).strip()
    idade = int(input('Qual é a sua idade? '))
    sexo = str(input('Qual é o seu sexo (M) (F): ')).upper().strip()
    print('\33[1:34m-\33[m'*23)

    if idade > velho and sexo == 'M':
        homemVelho = nome.capitalize()
        velho = idade
    elif idade < 20 and sexo == 'F':
        mulheresMenor += 1
    somaIdade += idade

mediaGrupo = somaIdade / 4
print(f'\33[1:36mO homem mais velho é o {homemVelho}, com {velho} anos')
print(f'A Quantidade de mulheres com menos de 20 anos é de {mulheresMenor}')
print(f'A média de idade do Grupo é de {mediaGrupo} anos')
