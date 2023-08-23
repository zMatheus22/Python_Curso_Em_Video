# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

print('===== Desafio 025 =====')
nome = str(input('Digite o nome: ')).strip()
nome = nome.upper()
possui = "SILVA"
analise = possui in nome
print('O seu nome possui "{}"? {}'.format(possui, analise))
