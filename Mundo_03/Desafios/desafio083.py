# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a
# expressão passada está com os parênteses abertos e fechados na ordem correta.

print('\33[1:34:40m=\33[m'*23)
print('\33[1:34:40m{:^23}\33[m'.format('DESAFIO 083 - MUNDO 3 '))
print('\33[1:34:40m=\33[m'*23)
print('\33[1:34m-'*23)
print('{:^23}'.format('Analise de Expressão'))
print('\33[1:34m-\33[m'*23)

# Ler a expressão
expressao = str(input('\33[1:33mDigite a expressão para analise: '))

# Transformar a 'expressao' em uma lista
verificar = list(expressao)
# Organizar os elementos/caracteres
verificar.sort()

# Atribuindo pontos para a analise
pontosVerificacaoSimbolo = pontosVerificacaoParentesAbertura = pontosVerificacaoParentesFechamento = 0

# Analisando a Parentes, Colchetes, Chaves
for cont in range(len(verificar)-1):
    if verificar[cont] in ('(', '[', '{'):
        pontosVerificacaoParentesAbertura += 1
    elif verificar[cont] in (')', ']', '}'):
        pontosVerificacaoParentesFechamento += 1
# Analisando simbolos
if expressao[len(expressao) - 1] in ('+', '-', '*', '/', ':'):
    pontosVerificacaoSimbolo += 1

# Apresentação
print('\33[35m+'*23)
if pontosVerificacaoParentesAbertura != pontosVerificacaoParentesFechamento or pontosVerificacaoSimbolo % 2 != 0:
    print(f'\33[31mExpressão \33[4m{expressao}\33[m\33[1:31m está incompleta!')
else:
    print(f'\33[32mA Expressão \33[4m{expressao}\33[m\33[1:32m está completa!')
print('\33[35m+'*23)
