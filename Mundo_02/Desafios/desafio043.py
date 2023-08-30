# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a
# tabela abaixo:
# - Abaixo de 18.5: Abaixo do Peso
# - Entre 18.5 e 25: Peso ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade mórbida

print('\33[1:34:40m=\33[m'*23)
print('\33[1:34:40m DESAFIO 043 - MUNDO 2 \33[m')
print('\33[1:34:40m=\33[m'*23)
print('\33[1:34m-'*23)
print('     Sistema IMC')
print('\33[1:34m-\33[m'*23)

peso = float(input('\33[1:36mPor gentileza informe o seu peso (Kg): '))
altura = float(input('Por gentileza informe a sua altura (m): \33[m'))
imc = peso / altura ** 2

if imc <= 18.5:
    print('\33[1:31m-'*23)
    print('     Abaixo do Peso')
    print(' O seu IMC esta em {:.1f}'.format(imc))
    print('\33[1:31m-\33[m' * 23)
elif imc > 18.5 and imc <= 25:
    print('\33[1:32m-' * 23)
    print('     Peso ideal')
    print(' O seu IMC esta em {:.1f}'.format(imc))
    print('\33[1:32m-\33[m'*23)
elif imc > 25 and imc <= 30:
    print('\33[1:35m-' * 23)
    print('     Sobrepeso')
    print(' O seu IMC esta em {:.1f}'.format(imc))
    print('\33[1:35m-\33[m' * 23)
elif imc > 30 and imc <= 40:
    print('\33[1:33m-' * 23)
    print('     Obesidade')
    print('O seu IMC esta em {:.1f}'.format(imc))
    print('\33[1:33m-\33[m' * 23)
else:
    print('\33[1:31m-' * 23)
    print('     Obesidade mórbida')
    print(' O seu IMC esta em {:.1f}'.format(imc))
    print('\33[1:31m-\33[m' * 23)
