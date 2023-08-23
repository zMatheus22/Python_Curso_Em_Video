# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

print('\33[1:30:43m===== Desafio 013 =====\33[m')
aumento = 15
salario = float(input('\33[1:33mDigite o seu salário: R$ \33[m'))
valor = salario + salario * (aumento / 100)
print('\33[1:40mO seu salário possou de \33[33mR$ {:.2f}\33[1:37m para \33[32mR$ {:.2f}\33[1:37m, teve um aumento de '
      '\33[34m{}%, \33[32mParabéns!\33[m'.format(salario, valor, aumento))
