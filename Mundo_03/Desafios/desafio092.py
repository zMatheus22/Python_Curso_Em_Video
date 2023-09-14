# Crie um programa que leia nome, ano de nascimento e carteiro de trabalho e cadastre-se (com idade) em um dicionário se
# por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e
# acrescente, além da idade com quantos anos a pessoa vai se aposentar.

from datetime import date
print('\33[1:34:40m=\33[m'*23)
print('\33[1:34:40m{:^23}\33[m'.format('DESAFIO 092 - MUNDO 3'))
print('\33[1:34:40m=\33[m'*23)
print('\33[1:34m-'*23)
print('{:^23}'.format('INSS'))
print('\33[1:34m-\33[m'*23)

anoAtual = date.today().year
contribuicaoINSS = 35
dados = dict()

print('\33[1:33m')
dados['nome'] = str(input('Nome: ')).strip().capitalize()
anoNascimento = int(input('Ano de nascimento: '))
dados['idade'] = anoAtual - anoNascimento
dados['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário: R$ '))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + contribuicaoINSS) - anoAtual)

print('\33[34m+'*23)
for key, valor in dados.items():
    print(f'{key.capitalize()}: {valor}')
