# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

print('===== Desafio 024 =====')
cidade = str(input('Digite o nome da cidade: ')).strip()
cidade = cidade.upper()
inicio = 'SANTO'
comecoCidade = inicio in cidade[:len(inicio)]
print('A sua cidade começa com "{}"? {}'.format(inicio, comecoCidade))
