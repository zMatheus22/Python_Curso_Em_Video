# Crie um programa que leia o nome completo de uma pessoa e mostre:
# -> O nome com todas as letras maiúsculas
# -> O nome com todas minúsculas
# -> Quantas letras ao todo (sem considerar espaços)
# -> Quantas letras tem o primeiro nome

print('===== Desafio 022 =====')
nome = str(input('Digite o nome completo: ')).strip()
print('Nome em maiúsculas: '.format(nome.upper()))
print('Nome em minúsculas: '.format(nome.lower()))
print("Quantidade de letras: {}".format(len(nome.replace(" ", ""))))
print("Quantidade de letras de {} é {}".format(nome.split()[0], len(nome.split()[0])))
