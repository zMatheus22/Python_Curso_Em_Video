# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente

print('===== Desafio 027 =====')
nome = str(input('Digite o nome completo: ')).strip()
nome = nome.split()

print('Primeito nome: {}'.format(nome[0]))
print('Último nome: {}'.format(nome[len(nome) - 1]))
