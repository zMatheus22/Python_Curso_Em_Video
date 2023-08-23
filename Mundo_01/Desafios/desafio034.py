# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salário superiores a R$ 1.250,00, calcule um aumento de 10%.
# Para os inferiorres ou iguais, o aumento pe de 15%.

print('===== Desafio 034 =====')
salario = float(input('Digite o seu salário: R$ '))
minimo = 1250.00

if salario <= minimo:
    salario = salario + salario * 0.15
    print('O seu novo salário será de R$ {:.2f}, com um aumento de 15%'.format(salario))
else:
    salario = salario + salario * 0.10
    print('O seu novo salário será de R$ {:.2f}, com um aumento de 10%'.format(salario))
