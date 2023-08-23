# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e se antecessor.

print('\33[1:30:46m===== Desafio 005 =====\33[m')
num = int(input('Digite um número: '))
print('Você digitou \33[1:32m{}\33[m, o seu sucessor é \33[1:33m{}\33[m e seu antecessor \33[1:31m{}\33[m!'.format(num, num+1, num-1))
